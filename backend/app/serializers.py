from  app.models import ContactUs
from rest_framework import serializers
from app.models import CommentQuestions,CommentAnswer
 
class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class CommentAnswerSerializers(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = CommentAnswer
        fields = ['id', 'answer','created_on','questions']
    

class CommentQuestionsSerializers(serializers.ModelSerializer):
    answers = CommentAnswerSerializers(many=True,read_only=True)
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = CommentQuestions
        fields = ["id", "answers","question","created_on"]

