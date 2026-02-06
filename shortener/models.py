from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


class ShortenedUrl(models.Model):

    id = models.AutoField(primary_key=True)
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    last_access = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='shortened_urls'
    )


    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_random_string(length=8, allowed_chars='0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ')
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.short_url} -> {self.original_url}'