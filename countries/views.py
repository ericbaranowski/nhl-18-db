from django.http import JsonResponse
from django.views import View
from .models import Country

class CountryView(View):
    def get(self, request):
        return JsonResponse({
            'countries': [c.json for c in Country.objects.all()]
        })
