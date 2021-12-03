from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ItemSerializer, ScheduleSerializer

from .models import Task, Item
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		
		'Create clinet':'/client-create/',
		'Clinets list':'/client-list/',
		'Edit client':'/cleint-edit/<str:pk>/',
		'clientDetail':'/client-detail/<str:pk>/',
		'schedules List':'/schedule-list/<str:pk>/'
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
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
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


@api_view(['POST'])
def clientCreate(request):
	serializer = ItemSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def clientsList(request):
	clients = Item.objects.all().order_by('-id')
	serializer = ItemSerializer(clients, many=True)
	return Response(serializer.data)


@api_view(['POST','PUT'])
def clientEdit(request, pk):
	client = Item.objects.get(id=pk)
	serializer = ItemSerializer(instance=client, data=request.data)
	print(request.data)
	if serializer.is_valid():
		
		print(serializer)
		serializer.save()
	else:
		print('error')

	return Response(serializer.data)

@api_view(['GET'])
def clientDetail(request, pk):
	client = Item.objects.get(id=pk)
	serializer = ItemSerializer(client, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def schedulesList(request, pk):
	schedule = Item.objects.filter(doctor=pk)
	serializer = ScheduleSerializer(schedule, many=True)
	return Response(serializer.data)