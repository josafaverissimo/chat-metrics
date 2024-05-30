from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class MyMessagesView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        file = request.FILES

        print(file)

        return Response({"message": "Hello World"})
