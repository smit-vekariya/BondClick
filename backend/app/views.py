from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from manager.manager import HttpsAppResponse, Util
from app.serializers import *
from django.contrib import messages
from django.shortcuts  import redirect
from django.urls import reverse

# Create your views here.
class MessageView(APIView):
    authentication_classes =[]
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/message.html"

    def get(self, request, *args, **kwargs):
        return Response(status=200, template_name=self.template_name, data={"messages":request.GET.get("messages")})

class Welcome(APIView):
    authentication_classes =[]
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/welcome.html"

    def get(self, request, *args, **kwargs):
        return Response(status=200, template_name=self.template_name)

class Home(APIView):
    authentication_classes =[]
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/home.html"

    def get(self, request, *args, **kwargs):
        return Response(status=200, template_name=self.template_name)

class AboutUs(APIView):
    authentication_classes = []
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/about_us.html"

    def get(self, request, *args, **kwargs):
        return Response(status=200, template_name=self.template_name)   


class ContactUs(APIView):
    authentication_classes = []
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/contact_us.html"
    serializer_class = ContactUsSerializers

    def get(self, request, *args, **kwargs):
        return Response(status=200, template_name=self.template_name) 

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect(reverse('app:message-page') + '?messages=We recived your query. We will contact you soon.')
            else:
                return redirect(reverse('app:message-page') + '?messages=Something went wrong! Try later.')
        except Exception as e:
            return HttpsAppResponse.exception(str(e))
            
