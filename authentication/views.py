from rest_framework.exceptions import ValidationError, ParseError, NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.serializers import UserSerializer
from authentication.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse, reverse_lazy



# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=request.data['email'])

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token)}
        return response

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email must not be empty'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'password must not be empty'})

        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token)}
        return response
        
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def getUser(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)

    @action(methods=['PATCH'], detail=False,
            permission_classes=[IsAuthenticated], url_path='update')
    def user_update(self, request):
        user = request.user
        currentData = self.serializer_class(user).data
        # serializer.is_valid(raise_exception=True)
        data = request.data
        if 'email' in data and len(data.get('email')) > 0 and currentData["email"] != data["email"]:
            try:
                User.objects.get(
                    email=data['email'])
                raise ParseError({'message': 'Email already taken'})
            except User.DoesNotExist:
                pass
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.bio = data['bio']
        print(user.first_name)
        user.save()

        return Response({'message': "user updated"})
        

    @action(methods=['DELETE'], detail=False,
            permission_classes=[IsAuthenticated])
    def delete(self, request):
        user = request.user
        data = self.serializer_class(user).data
        instance = User.objects.get(email=data["email"])
        print(instance)
        instance.delete()

        return Response({'message': "user deleted"})