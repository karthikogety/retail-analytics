from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
def generate_sale():
    return {
        "transaction_id": fake.uuid4(),
        "timestamp": fake.date_time_this_year().isoformat(),
        "product_id": fake.random_int(min=1, max=100),
        "quantity": fake.random_int(min=1, max=10),
        "price": fake.random_number(digits=4) / 100,
        "customer_id": fake.uuid4(),
        "store_id": fake.random_int(min=1, max=5)
    }

def generate_interaction():
    return {
        "customer_id": fake.uuid4(),
        "timestamp": fake.date_time_this_year().isoformat(),
        "action": fake.random_element(elements=("click", "add-to-cart", "view")),
        "page_url": fake.url()
    }

for _ in range(10):
    sale = generate_sale()
    interaction = generate_interaction()
    producer.send('sales', sale)
    producer.send('interactions', interaction)
    print("Sent Sale:", json.dumps(sale))
    print("Sent Interaction:", json.dumps(interaction))
    producer.flush()
    time.sleep(1)  # Simulate real-time data
