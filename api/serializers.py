from rest_framework import serializers
from .models import Task, Item

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields ='__all__'

class ScheduleSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='name')
	start = serializers.CharField(source='datetime')
	id = serializers.CharField(source='doctor')
	class Meta:
		model = Item
		fields = ['title','start','id']