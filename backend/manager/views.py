from django.shortcuts import render
from manager.models import GroupPermission, AllPermissions, PageGroup, SystemParameter
from manager.serializers import SystemParameterSerializers
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.db import transaction
from django.db.models import F
from manager.manager import HttpsAppResponse, Util

# Create your views here.
class GroupPermissionView(viewsets.ViewSet):
    authentication_classes =[]
    permission_classes = []

    def user_groups(self, request):
        user_groups = list(Group.objects.values("id","name"))
        return HttpsAppResponse.send(user_groups, 1, "Get user group data successfully.")

    def get(self, request):
        try:
            group_id = request.GET.get("group_id")
            if group_id is None:
                group_list = list(Group.objects.values("id","name"))
                return HttpsAppResponse.send(group_list, 1, "")
            pages = list(PageGroup.objects.values("id", "page_name__name", "page_code"))
            group_permission = []
            for page in pages:
                permission = list(GroupPermission.objects.select_related('permissions').filter(group_id=group_id, permissions__page_group=page["id"]).annotate(act_name = F("permissions__act_name"), act_code = F("permissions__act_code")).values("id","act_name","act_code","has_perm"))
                page["permission"] = permission
                group_permission.append(page)
            return HttpsAppResponse.send(group_permission, 1, "Get group permission data successfully.")
        except  Exception as e:
            return HttpsAppResponse.exception(str(e))

    def post(self, request):
        try:
            with transaction.atomic():
                perm_data = request.data
                group_id = perm_data["group_id"]
                for data in perm_data["data"]:
                    for perm in data["permission"]:
                        set_perm = GroupPermission.objects.get(id=perm["id"],group_id=group_id)
                        set_perm.has_perm = perm["has_perm"]
                        set_perm.save()
                        
                return HttpsAppResponse.send([], 1, "Group permission update successfully.")
                
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


# All function is not require, write this function for customize response formate and learn (basically i overwrite those function to change response)
class SystemParameterView(viewsets.ModelViewSet):
    # authentication_classes =[]
    # permission_classes = []
    queryset = SystemParameter.objects.all()
    serializer_class = SystemParameterSerializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return HttpsAppResponse.send(serializer.data, 1, "Get system parameter sucessfully.")

    def create(self, request):
        try:
            if Util.has_perm(request.user,"can_add_system_parameter") is False:
                return HttpsAppResponse.send([], 0, "You don't have permission to perform this action.")
            serializer = self.get_serializer(data=request.data["form_data"])
            if serializer.is_valid():
                self.perform_create(serializer)
                return HttpsAppResponse.send([], 1, "Create system parameter sucessfully.")
            else:
                return HttpsAppResponse.send([], 0, str(serializer.errors))
        except Exception as e:
            return HttpsAppResponse.send([], 0, str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            if Util.has_perm(request.user,"can_delete_system_parameter") is False:
                return HttpsAppResponse.send([], 0, "You don't have permission to perform this action.")
            instance = self.get_object()
            self.perform_destroy(instance)
            return HttpsAppResponse.send([], 1, "Delete system parameter successfully.")
        except Exception as e:
            return HttpsAppResponse.send([], 0, str(e))

    def update(self, request, *args, **kwargs):
        try:
            if Util.has_perm(request.user,"can_edit_system_parameter") is False:
                return HttpsAppResponse.send([], 0, "You don't have permission to perform this action.")
            instance = self.get_object()
            serializer =self.get_serializer(instance, data=request.data["form_data"])
            if serializer.is_valid():
                self.perform_update(serializer)
                return HttpsAppResponse.send([], 1, "Update system parameter sucessfully.")
            else:
                return HttpsAppResponse.send([], 0, str(serializer.errors))
        except Exception as e:
            return HttpsAppResponse.send([], 0, str(e))


def bad_request(request,exception):
    response = render(request,'manager/400.html')
    response.status_code = 400
    return response

def permission_denied(request, exception):
    response = render(request,'manager/403.html')
    response.status_code = 403
    return response

def page_not_found(request, exception):
    response = render(request,'manager/404.html')
    response.status_code = 404
    return response

def server_error_view(request):
    response = render(request,'manager/500.html')
    response.status_code = 500
    return response

