from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from rest_framework import generics

from .serializers import URLSerializer
from .models import URL
from Slug_generator.slug_generator import slug_generator


class URLView(generics.ListCreateAPIView):
    serializer_class = URLSerializer

    def get_queryset(self):
        queryset = URL.objects.all()
        sort_keys = self.request.data.get('sort', [])
        for key in sort_keys:
            queryset = queryset.order_by(key)
        return queryset

    def perform_create(self, serializer):
        serializer.save(slug=slug_generator())


class URLRedirectView(RedirectView):
    permanant = True

    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        return url.address