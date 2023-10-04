import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    bat_speed = float(data["Bat Speed (mph)"])  # Assuming the value in CSV is a string, convert to float
    metrics = {
        "Bat Speed (mph)": bat_speed,
        "Rotational Acceleration (g)": data["Rotational Acceleration (g)"]
    }
    print(f"Consumer 2 received: {metrics}")

    if bat_speed < 67:
        print(f"\033[1mPoor intent\033[0m")  # Bold text for "Poor intent"

# Setup RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='csv_queue')
channel.basic_consume(queue='csv_queue', on_message_callback=callback, auto_ack=True)

print('Consumer 2 [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
