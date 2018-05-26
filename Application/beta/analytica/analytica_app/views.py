from django.template.response import SimpleTemplateResponse

from django.views.generic import TemplateView, View
from .twitter_api import search_by_hashtag
from django.shortcuts import render


class AppView(View):
    template_name = "analytica_app/index.html"

    def get(self, request):
        if request.GET.get('q'):
            context = {}
            tweets = search_by_hashtag(q=request.GET.get('q'))
            if tweets:
                context['tweets'] = tweets
            else:
                context['no_tweets'] = True
            return SimpleTemplateResponse(
                template=self.template_name,
                context=context
            )
        else:
            return SimpleTemplateResponse(
                template=self.template_name,
            )
            
            
def AboutUs(request):
    return  render(request, 'analytica_app/aboutus.html')
