from kafka import KafkaProducer
import json
import time

# Initialize the Kafka producer
producer = None
while producer is None:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',  # Use the service name 'kafka'
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        time.sleep(5)

def generate_log_entry():
    # Replace this with your log generation logic
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": "INFO",
        "message": "This is a sample log entry"
    }

while True:
    log_entry = generate_log_entry()
    producer.send('log-entries', log_entry)
    print(f"Sent: {log_entry}")
    time.sleep(5)  # Adjust the frequency as needed
