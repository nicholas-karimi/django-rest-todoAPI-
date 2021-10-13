from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .models import Task 
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
	# endpoints to be returned

	api_urls ={
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/'
	}
	return Response(api_urls)


# list endpoint

@api_view(['GET'])
def listView(request):
	tasks =  Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskView(request, pk):
	tasks =  Task.objects.get(pk=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task =  Task.objects.get(pk=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def taskDelete(request, pk):
	task =  Task.objects.get(pk=pk)

	task.delete()

	return Response("Item deleted successfully!")