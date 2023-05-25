from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


from rest_framework.generics import CreateAPIView
from .serializers import Account_Creation
from rest_framework import status
from ecommerce.users.api.serializers import UserSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)



class Register_Account ( CreateAPIView ) :
    
    """
    this is the endpoint for account creation , which includes 
    the landlord and tenant information
    """
    permission_classes = [ AllowAny, ]
    serializer_class = Account_Creation

    def post (self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid():
            serializer.save(request)
            # return response
            return Response( {'status':'successful', 'message':'your account is created succesfully', 'data':serializer.data } , status = status.HTTP_201_CREATED )

        return Response( {'status':'error', 'message':'check your input and try again',} , status = status.HTTP_400_BAD_REQUEST )

