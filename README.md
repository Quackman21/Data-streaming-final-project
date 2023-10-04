# Data-Streaming-Final-Project
- Author: Ivan Quackenbush
- Date: October 4th, 2023

This module takes baseball swings that have been captured in real life using a blat motion hitting sensor and turns it into a digital stream. The swings are 5 seconds aprt which is close to the pace that you would get in a normal practice. Within the code are some perameters that will show up that will help a coach understand what he hitter is doing. 

If the hitter swings below a certain batspeed a message will appear in bold that will tell them that the hitters intent was poor. If the attack angle is below a certain range then it will tell them if they were late or not. Finally If a hitter does not have a connection at impact below 75 degrees it will say that the hitter was out in front when they struck the baseball.

The consumer and producers are broken up to where each window will help show certain aspects of the swing making it esasier for a caoch to find information that is relevent to them. 

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

The following modules are required: 


| Module          |
|-----------------|
| csv             |
| webbrowser      |
| Json            |
| time            |
| pika            |


## Suggested Readings

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
1. Read the code and comments in this repo.


- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

## Consumers and Producers Explained 

1. Swing-Producer
The producer takes the information from the CSV file and spits out the metrics that are related to real swings from a hitter

2. Swing-Analytics-Consumer:
This takes all of the information related to angles within the siwng and packages it into one consumer.

3. Swing-Score-Consumer:
This consumer grades the quality of the players swing. It uses the MLB scouting scale of 20-80 to produces a grade on how well they did a certain motin in thier swing.

4. Swing-Speed-Consumer
This consumer takes all of the information reguarding the speed of the swing and how fast the players body is turning. 

## Producers and Consumers at work
![Alt text](<Working Terminal.png>)

## Rabbitmq at work
![Alt text](<RabbitMq SS.png>)