import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='user_requests')
channel.queue_declare(queue='youtuber_uploads')

subscriptions = {}  #dictionary of list of subscritpions with user as the key
notification_queues = {}  

def update_subscription(user, youtuber, subscribe=True):
    if user not in subscriptions:
        subscriptions[user] = []
    if subscribe:
        if youtuber not in subscriptions[user]:
            subscriptions[user].append(youtuber)
    else:
        if youtuber in subscriptions[user]:
            subscriptions[user].remove(youtuber)

def notify_users(youtuber, video_name):
    message = f"{youtuber} uploaded {video_name}"
    for user, subs in subscriptions.items():
        if youtuber in subs:
            user_queue = notification_queues.get(user, f"{user}_notifications")
            channel.queue_declare(queue=user_queue)
            channel.basic_publish(exchange='', routing_key=user_queue, body=message)
            print(f"Notified {user} about new video: {video_name}")

def consume_user_requests(ch, method, properties, body):
    request = json.loads(body)
    user = request['user']
    notification_queues[user] = f"{user}_notifications"
    if 'subscribe' in request:
        action = 'subscribed' if request['subscribe'] else 'unsubscribed'
        update_subscription(user, request['youtuber'], request['subscribe'])
        print(f"{user} {action} to {request['youtuber']}")
    else:
        print(f"{user} logged in")

def consume_youtuber_requests(ch, method, properties, body):
    upload = json.loads(body)
    youtuber = upload['youtuber']
    video_name = upload['videoName']
    print(f"{youtuber} uploaded {video_name}")
    notify_users(youtuber, video_name)

channel.basic_consume(queue='user_requests', on_message_callback=consume_user_requests, auto_ack=True)
channel.basic_consume(queue='youtuber_uploads', on_message_callback=consume_youtuber_requests, auto_ack=True)

print('YoutubeServer is running. Waiting for messages...')
channel.start_consuming()
