from django.urls import path

from application.core.views import CreateView, ResolveView, StatsView


urlpatterns = [
    path('shorten', CreateView.as_view()),
    path('<str:shorturl>', ResolveView.as_view()),
    path('<str:shorturl>/stats', StatsView.as_view()),
]
