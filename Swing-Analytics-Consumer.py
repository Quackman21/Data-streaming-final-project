import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    attack_angle = float(data["Attack Angle (deg)"])  # Convert to float
    connection_at_impact = float(data["Connection at Impact (deg)"])  # Convert to float

    metrics = {
        "On Plane Efficiency (%)": data["On Plane Efficiency (%)"],
        "Attack Angle (deg)": attack_angle,
        "Early Connection (deg)": data["Early Connection (deg)"],
        "Connection at Impact (deg)": connection_at_impact,
        "Vertical Bat Angle (deg)": data["Vertical Bat Angle (deg)"],
        "Power (kW)": data["Power (kW)"],
        "Time to Contact (sec)": data["Time to Contact (sec)"],
        "Peak Hand Speed (mph)": data["Peak Hand Speed (mph)"]
    }
    print(f"Consumer 3 received: {metrics}")

    if attack_angle < 4:
        print("Late swing")

    if connection_at_impact < 70:
        print(f"\033[1mOut in front\033[0m")  # Bold text for "Out in front"

# Setup RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='csv_queue')
channel.basic_consume(queue='csv_queue', on_message_callback=callback, auto_ack=True)

print('Consumer 3 [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
