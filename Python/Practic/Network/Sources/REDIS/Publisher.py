import redis
import random


if __name__ == "__main__":
    conn = redis.Redis()
    cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
    hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']
    for msg in range(10):
        cat = random.choice(cats)
        hat = random.choice(hats)
        print(f'[Publisher] Publish: {cat} wears a {hat}')
        conn.publish(cat, hat)