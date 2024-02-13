import pika
import sys
import json

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(
#         host='34.131.86.186',  # Replace 'vm_external_ip' with your VM's external IP address
#         credentials=pika.PlainCredentials('ElderDragon', 'chirag')  # Replace with your RabbitMQ credentials
#     )
# )

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

youtuber = sys.argv[1]
video_name = ' '.join(sys.argv[2:])

def publish_video(youtuber, video_name):
    channel.queue_declare(queue='youtuber_uploads')
    body = json.dumps({'youtuber': youtuber, 'videoName': video_name})
    channel.basic_publish(exchange='', routing_key='youtuber_uploads', body=body)
    print("SUCCESS")

publish_video(youtuber, video_name)
connection.close()
