# third-party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class FooView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"foo": "bar"})
