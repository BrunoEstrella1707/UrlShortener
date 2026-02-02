import json
import pika
from .connection import get_connection


def publish(*, exchange, queue, routing_key, payload):

    conn = get_connection()
    try:
        channel = conn.channel()

        channel.exchange_declare(
            exchange=exchange,
            exchange_type='direct',
            durable=True
        )

        channel.queue_declare(
            queue=queue,
            durable=True
        )

        channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key
        )

        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(payload),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        
    finally:
        conn.close()