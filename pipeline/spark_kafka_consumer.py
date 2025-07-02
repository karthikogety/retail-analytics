from kafka import KafkaConsumer
import json
import threading

def consume_data(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    print(f"Listening to topic: {topic}")
    for message in consumer:
        print(f"Received from {topic}: {message.value}")

if __name__ == "__main__":
    topics = ['sales', 'interactions']
    threads = []
    for topic in topics:
        thread = threading.Thread(target=consume_data, args=(topic,))
        thread.daemon = True  # Stops threads when main program exits
        threads.append(thread)
        thread.start()

    try:
        while True:
            pass  # Keep main thread running
    except KeyboardInterrupt:
        print("Stopping consumer...")
