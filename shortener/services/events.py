from django.conf import settings
from shortener.messaging.publisher import publish


def publish_click_event(
    *,
    short_url: str,
    url_id: int | None = None,
    user_id: int | None = None,
    ip: str | None = None,
    user_agent: str | None = None,
    timestamp=None,
):

    payload = {
        "event": "url.clicked",
        "short_url": short_url,
        "url_id": url_id,
        "user_id": user_id,
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": timestamp.isoformat() if timestamp else None,
    }

    publish(
        exchange=settings.RABBITMQ_EXCHANGE,
        queue=settings.RABBITMQ_QUEUE_CLICKS,
        routing_key=settings.RABBITMQ_ROUTING_KEY,
        payload=payload,
    )
