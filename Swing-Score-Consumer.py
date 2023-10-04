import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    metrics = {
        "Plane Score": data["Plane Score"],
        "Connection Score": data["Connection Score"],
        "Rotation Score": data["Rotation Score"]
    }
    print(f"Consumer 1 received: {metrics}")

# Setup RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='csv_queue')
channel.basic_consume(queue='csv_queue', on_message_callback=callback, auto_ack=True)

print('Consumer 1 [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
