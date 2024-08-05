import time
from kafka import KafkaConsumer
import json

consumer = None
while consumer is None:
    try:
        consumer = KafkaConsumer(
            'log-entries',
            bootstrap_servers='kafka:9092',  # Use the service name 'kafka'
            group_id='log-consumer-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        time.sleep(5)

for message in consumer:
    log_entry = message.value
    print(f"Received: {log_entry}")
    # Add your log processing logic here
