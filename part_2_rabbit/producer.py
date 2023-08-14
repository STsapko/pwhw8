import src.connect_mongodb
from src.models import User
from part_2_rabbit.src.connect_rabbitmq import connect_rabbitmq
from seeds import seed_users

import time

channel = connect_rabbitmq()

def main():
    User.objects().delete()
    users = seed_users()
    
    for user in users:
        user.save()
        
    for user in User.objects.all():
        channel.basic_publish(exchange="", 
                              routing_key="emails", 
                              body = f"{user.id}.encode()")

        time.sleep(1)
        print(f"{user.fullname}")
    
    channel.close()

if __name__ == '__main__':
    main()