import pika

def connect_rabbitmq():
    credentials = pika.PlainCredentials('guest','guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost',
                                  port = 5672,
                                  credentials= credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue="emails")
    return channel