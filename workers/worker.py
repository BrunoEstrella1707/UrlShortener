import json
import sys
import os
from pathlib import Path
import django

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from shortener.messaging.connection import get_connection
from shortener.services.click_service import process_click


def on_message(channel, method, body):
    try:
        payload = json.loads(body)

        if payload.get("event") != "url.clicked":
            channel.basic_ack(method.delivery_tag)
            return

        print("Click Received")
        process_click(payload)
        print("Short URL:", payload["short_url"])
        print("Timestamp:", payload["timestamp"])

        channel.basic_ack(method.delivery_tag)

    except Exception as exc:
        print(f"Error processing the message: {exc}")
        channel.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=True
        )
    


def start():
    connection = get_connection()
    channel = connection.channel()

    
    channel.queue_declare(
        queue=settings.RABBITMQ_QUEUE_CLICKS,
        durable=True,
        auto_delete=False,
    )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue=settings.RABBITMQ_QUEUE_CLICKS,
        on_message_callback=on_message,
    )

    print("Worker running and listening...")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(f'Error: Failed to start connection {e}')