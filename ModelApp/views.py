
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics

from .models import Person
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PersonSerializer,UserSerializer
from .ownpermissions import ProfilePermission

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    
    def get_object(self):
        return self.request.user

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(IsAuthenticated,)
