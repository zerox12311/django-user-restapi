from rest_framework import viewsets
from app.authorization.serializers import UserSerializer
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    使用者


    ---
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer