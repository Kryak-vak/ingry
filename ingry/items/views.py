from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views
from rest_framework.response import Response

from items.models import Items
from items.serializer import ItemSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class MyView(views.APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = ['Hello hui']
        return Response(usernames)
    
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = ['Hello hui']
        return Response(usernames)