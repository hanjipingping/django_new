from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def user(request):
    return HttpResponse("<h1>1111</h1>")


class MO(View):
    def get(self, request):
        data = {
            "aa": 11
        }
        return JsonResponse(data=data,safe=False)
