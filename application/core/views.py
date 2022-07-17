import json

from django.db import IntegrityError
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.views.generic.base import View

from application.core.models import ShortUrl


class CreateView(View):
    def post(self, request) -> JsonResponse:
        status = 400

        provided_data = json.loads(request.body)
        provided_url = provided_data.get("url")
        provided_shortcode = provided_data.get("shortcode")

        if provided_url is None:
            return JsonResponse(data={"error": "Url not present"}, status=400)

        if provided_shortcode is None:
            # If no code is given, generate one
            provided_shortcode = ShortUrl.generate_code()
        elif provided_shortcode is not None \
                and not ShortUrl.shortcode_is_valid(provided_shortcode):
            return JsonResponse(data={"error": "The provided shortcode is invalid"}, status=412)

        try:
            res = ShortUrl.objects.create(
                short=provided_shortcode,
                full_url=provided_url,
            )

            return JsonResponse(data={"shortcode": res.short}, status=201)

        except IntegrityError:
            # Could potentially catch other integrity errors, 
            # for now assuming they need to return the same error
            return JsonResponse(data={"error": "Shortcode already in use"}, status=409)


class ResolveView(View):
    def get(self, request, *args, **kwargs):
        shorturl = self.kwargs.get("shorturl")

        try:
            resolved_url = ShortUrl.objects.get(short=shorturl)
            resolved_url.hit_count += 1
            resolved_url.save()

            return HttpResponseRedirect(resolved_url.full_url)
        except ShortUrl.DoesNotExist:
            raise Http404("Shortcode not found")


class StatsView(View):
    def get(self, request, *args, **kwargs):
        shorturl = self.kwargs.get("shorturl")
        
        try:
            resolved_url = ShortUrl.objects.get(short=shorturl)
            
            return JsonResponse(data={
                "created": resolved_url.created_at,
                "lastRedirect": resolved_url.updated_at,
                "redirectCount": resolved_url.hit_count,
            })

        except ShortUrl.DoesNotExist:
            raise Http404("Shortcode not found")
