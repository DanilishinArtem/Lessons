import redis


if __name__ == "__main__":
    conn = redis.Redis()
    topics = ['maine coon', 'persian']
    sub = conn.pubsub()
    sub.subscribe(topics)
    for msg in sub.listen():
        if msg['type'] == 'message':
            cat = msg['channel']
            hat = msg['data']
            print(f'[Subscriber] Subscribe: {cat} wears a {hat}')