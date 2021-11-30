from django.shortcuts import render
from . import models
from . import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(APIView):

    """
        post: create a new user
    """

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if(serializer.is_valid()):
        # serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('success')
        else:
            return Response('A User with that Email already exists')

class UserDetails(APIView):

    """
        get: fetch user details
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user, many=False)
        return Response(serializer.data)


    def put(self, request):
        data = request.data
        if(data['address']):
            query = models.UserProfile.objects.get(username=request.user.username)
            query.address = data['address']
            query.save()
            return Response('success')

        else:
            return Response('New Address not provided!')