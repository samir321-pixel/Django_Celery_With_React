from .serializers import User_Mail_Serializer
from .models import User_mail
from rest_framework.response import Response
from rest_framework import generics, status
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'index'


class SendMail(generics.GenericAPIView):
    serializer_class = User_Mail_Serializer
    queryset = User_mail.objects.all()

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = User_mail.objects.all()
        serializer = User_Mail_Serializer(snippets, many=True)
        return Response(serializer.data)
