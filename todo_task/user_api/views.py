import pstats
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
key = 'todo_task_password_encryption_key' # Password encryption key
class UserAPI(APIView):
    def post(self,request):
        email = request.data.get('email')
        count = User.objects.filter(email=email).count() # check email id is already regestered?
        if count > 0: # If Email id already present dont save the user
            context = {
                'resp': 'Email id is already in use, Please use another email id and try again..!', 'acc_created': False
                }
            return Response(context)

        request.data._mutable = True 
        request.data['password'] = make_password(
            salt=key, password=request.data.get('password')) # replace plain password with encrypted password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {'resp' : 'Account Created Successfully.!','acc_created': True} # Account not created response
        else:
            context = {'resp' : 'Invalid Data..','acc_created': False}  # Account created successfully response
            print(serializer.errors)
        return Response(context)


class UserLogin(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = make_password(salt=key, password=request.data.get('password')) # convert plain password to encrypted
        print(email,password)
        try:
            user = User.objects.get(email=email, password=password) # check is user present or not
            context = {'is_valid': True,'user_id': user.id} # successfull response
        except Exception as e:
            context = {'is_valid': False} # Error response
            print(e)
        return Response(context)


