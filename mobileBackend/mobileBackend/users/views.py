from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def fetch_users(request):
    #fetch all the actor objects
    users = User.objects.all()
    #serialize the actors
    serializer = UserSerializer(users, many=True)
    #return Response using rest_framework's response
    return Response(serializer.data)