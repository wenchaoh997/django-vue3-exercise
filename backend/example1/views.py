from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def api(request):
    urls = {
        "testing1": "Here is an App without any model.",
        "testing2": "Just using the GET method to gain info.",
        "testing3": "/testing3/urls",
    }
    return Response(urls)