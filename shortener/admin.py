from django.contrib import admin
from .models import ShortenedUrl

# Register your models here.
class ShortenedUrlAdmin(admin.ModelAdmin):

    list_display = ('original_url', 'short_url', 'created_at', 'clicks', 'user',)

admin.site.register(ShortenedUrl, ShortenedUrlAdmin)


