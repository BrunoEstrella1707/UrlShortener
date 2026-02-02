from django.db import transaction
from django.db.models import F
from django.utils import timezone
from shortener.models import ShortenedUrl


def process_click(payload: dict):
    short_url = payload["short_url"]

    with transaction.atomic():
        ShortenedUrl.objects.filter(short_url=short_url).update(clicks=F('clicks') + 1, last_access=timezone.now())

