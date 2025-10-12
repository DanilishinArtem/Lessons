import csv

if __name__ == "__main__":
    villains = [
        {'first': 'Doctor', 'last': 'No'},
        {'first': 'Rosa', 'last': 'Klebb'},
        {'first': 'Mister', 'last': 'Big'},
        {'first': 'Auric', 'last': 'Goldfinger'},
        {'first': 'Ernst', 'last': 'Blofeld'},
    ]
    # part of writing
    with open('villains.csv', 'wt') as fout:
        cout = csv.DictWriter(fout, ['first', 'last'])
        cout.writeheader()
        cout.writerows(villains)
    # part of reading
    with open('villains.csv', 'rt') as fin:
        cin = csv.DictReader(fin)
        output = [row for row in cin]
    print(f'[INFO] Result of reading: {output}')