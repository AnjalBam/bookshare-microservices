from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf import settings

client = settings.REDIS_INSTANCE


# Create your views here.
@api_view(["GET"])
def test(request, *args, **kwargs):
    client.set("name", "Anjal")
    name = client.get("name")
    print(name)
    return Response({"url": request.path, "name": name})
