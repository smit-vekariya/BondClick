from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from manager.manager import HttpsAppResponse, Util
from app.serializers import *
from django.contrib import messages
from django.shortcuts  import redirect
from django.urls import reverse
from app.serializers import CommentQuestionsSerializers, CommentAnswerSerializers, ContactUsSerializers
from app.models import CommentQuestions, CommentAnswer
from rest_framework import viewsets
import json
from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import action

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

class AskAnything(viewsets.ModelViewSet):
    authentication_classes =[]
    permission_classes = []
    queryset = CommentQuestions.objects.all()
    serializer_class = CommentQuestionsSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "app/ask_anything.html"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True)
        return Response(status=200, template_name=self.template_name,data={"question_answer":json.loads(json.dumps(serializer.data))})

    def create(self, request, *args, **kwargs):
        if "answer_textarea" in request.POST:
            answer_textarea = request.POST.get("answer_textarea")
            question_id = request.POST.get("question_id")
            serializer = CommentAnswerSerializers(data={"answer":answer_textarea, "created_on":timezone.now(),'questions':question_id})
        else:
            question_textarea = request.POST.get("question_textarea")
            serializer = self.serializer_class(data={"question":question_textarea,"created_on":timezone.now()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return redirect(reverse('app:ask-anything-page'))

    def destroy_answer(self, request, *args, **kwargs):
        instance = CommentAnswer.objects.get(pk=kwargs['pk'])
        instance.delete()
        return HttpsAppResponse.send([], 1, "Delete Answer successfully.")

    def update_answer(self, request, *args, **kwargs):
        instance = CommentAnswer.objects.get(pk=kwargs['pk'])
        serializer = CommentAnswerSerializers(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return HttpsAppResponse.send([], 1, "Update answer sucessfully.")




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
    serializer_class = ContactUsSerializers
    template_name = "app/contact_us.html"

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
            

