from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

class TaskAPI(APIView):
    def post(request): # Create new task
        serializer = TaskSerializer(data=request.data) # serialize data
        if serializer.is_valid():
            serializer.save()
            context = {'resp' : 'Tast added successfully..!','acc_created' : True} # Successful response
        else:
            context = {'resp' : 'Invalid data.','acc_created' : False} # Error response
        return Response(context)

    def get(request,user_id): # get all task added by specific user
        tasks = Task.objects.filter(user_id=user_id) # get tasks from database
        serializer = TaskSerializer(tasks,many=True) # serialize it
        context = {'resp' : serializer.data} # return in response
        return Response(context)
    
    def patch(request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.is_completed = True # update is_completed field of Task model
            task.save() # save changes
            context = {'resp' : 'Task status changed to completed.','is_updated':True} # successfull response
        except Exception as e:
            context = {'resp' : 'Invalid task id.','is_updated':False} # Error Response
        return Response(context)
    
    def delete(request,task_id):
        try:
            task = Task.objects.get(id=task_id) # get specific task from db
            task.delete() # delete it
            context = {'resp' : 'Task is deleted.','is_deleted':True}  # successfull response
        except Exception as e:
            context = {'resp' : 'Invalid task id.','is_deleted':False} # Error Response - if task_id is invalid
        return Response(context)
