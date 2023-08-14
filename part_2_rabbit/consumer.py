import src.connect_mongodb
from src.models import User
from part_2_rabbit.src.connect_rabbitmq import connect_rabbitmq
from seeds import seed_users
from bson.objectid import ObjectId

import time

channel = connect_rabbitmq()

def consume_email(ch, method, properties, body):
    
    user = User.objects.get(id = ObjectId(body.decode()))
    
    if not user.sent:
        print(f'{user.fullname}')
        user.sent = True
        user.save()
        time.sleep(1)
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="email", on_message_callback=consume_email)

if __name__ == "__main__":
    channel.start_consuming()