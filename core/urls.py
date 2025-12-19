from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterView, LoginView, LogoutView
from shortener.views import ShortUrlView, RedirectShortUrlView, ListUrlsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shortener/', ShortUrlView.as_view(), name='create_short_url'),
    path('shortener/<str:short_url>/', RedirectShortUrlView.as_view(), name='redirect_short_url'),
    path('shortener/register/', RegisterView.as_view(), name='register'),
    path('shortener/login/', LoginView.as_view(), name='login'),
    path('shortener/logout/', LogoutView.as_view(), name='logout'),
    path('shortener/<int:pk>/list/', ListUrlsView.as_view(), name='list_short_url'),
]
