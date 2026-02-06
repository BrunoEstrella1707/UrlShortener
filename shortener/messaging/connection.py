import pika
from django.conf import settings


def get_connection():
    params = pika.URLParameters(settings.RABBITMQ_URL)
    return pika.BlockingConnection(params)


