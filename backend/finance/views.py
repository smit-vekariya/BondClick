from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from finance.serializers import FinUserSerializers, TransactionsSerializers, UserTransSerializers
from finance.models import FinUser, Transactions
from rest_framework.decorators import action
import json

class DashBoardView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = FinUser.objects.all()
    serializer_class = FinUserSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'finance/dashboard.html'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        user_data =  json.loads(json.dumps(serializer.data))
        income,expence = 0.0, 0.0
        for data in user_data:
            income += float(data["income"]) if data["income"] else 0.0
            expence += float(data["expence"]) if data["expence"] else 0.0
        return Response(template_name=self.template_name, data={"user_data":user_data,"income":round(income, 2),"expence":round(expence,2),"final":round(income-expence ,2)})

    @action(detail=True, methods=['GET'])
    def transactions_list(self, request, pk=None):
        serializer = UserTransSerializers(self.queryset.filter(id=pk), many=True)
        return Response(template_name='finance/transactions.html', data={"trans_data":json.loads(json.dumps(serializer.data))})

    @action(detail=False, methods=['POST'])
    def transactions_create(self, request):
        serializer = TransactionsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(template_name='finance/transactions.html')

    @action(detail=True, methods=['DELETE'])
    def transactions_delete(self, request, pk=None):
        Transactions.objects.get(id=pk).delete()
        return Response(template_name='finance/transactions.html')

    @action(detail=False, methods=['POST'])
    def split_amount(self, request):
        data = json.loads(request.POST.get("data"))
        insert_data=[]
        per_amount = float(data["split_amount"]) / len(data["checked_ids"])
        disc = f"(split with {len(data['checked_ids'])} of {data['split_amount']}) " + data["split_desc"]
        for id in data["checked_ids"]:
            insert_data.append({"fin_user":id, "amount":per_amount, "is_income":True, "disc":disc})
        serializer = TransactionsSerializers(data=insert_data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(template_name='finance/transactions.html')

