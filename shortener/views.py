from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedUrl
from .forms import ShortUrlForm
from django.views import View
from django.views.generic import ListView


class ShortUrlView(View):
    form_class = ShortUrlForm
    template_name = 'home.html'


    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            short_url = form.save(commit=False)
            if request.user.is_authenticated:
                short_url.user = request.user
                
            short_url.save()
            
        return render(request, self.template_name, {'form': form, 'short_url': short_url})


class RedirectShortUrlView(View):

    def get(self, request, short_url):
        link = get_object_or_404(ShortenedUrl, short_url=short_url)
        link.clicks += 1
        link.save(update_fields=['clicks'])
        # ShortenedUrl.objects.filter(pk=link.pk).update(clicks=F('clicks') + 1)
        return redirect(link.original_url)


class ListUrlsView(ListView):

    model = ShortenedUrl
    template_name='urls_list.html'
    context_object_name='shortened_url'
    login_url = '/accounts/login/'

    def get_queryset(self):
        return ShortenedUrl.objects.filter(user_id=self.request.user.id)
