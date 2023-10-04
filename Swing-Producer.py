import csv
import pika
import json
import time
import webbrowser

webbrowser.get('safari').open('http://localhost:15672/')

# Setup RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='csv_queue')

# Updated Columns
columns = [
    "Plane Score", "Connection Score", "Rotation Score",
    "Bat Speed (mph)", "Rotational Acceleration (g)", "On Plane Efficiency (%)", 
    "Attack Angle (deg)", "Early Connection (deg)", "Connection at Impact (deg)", 
    "Vertical Bat Angle (deg)", "Power (kW)", "Time to Contact (sec)", 
    "Peak Hand Speed (mph)"
]

# Read CSV file
with open('Metrics - Klayton Kiser.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert each row to JSON for better structure and readability on the consumer side
        message = json.dumps({col: row[col] for col in columns})
        channel.basic_publish(exchange='', routing_key='csv_queue', body=message)
        print(f" [x] Sent {message}")
        time.sleep(5)  # Pause for 5 seconds before sending the next row

connection.close()

