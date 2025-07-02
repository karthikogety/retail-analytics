from faker import Faker
import json
import time

fake = Faker()

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
    print("Sale:", json.dumps(sale))
    print("Interaction:", json.dumps(interaction))
    time.sleep(1)  # Simulate real-time data
