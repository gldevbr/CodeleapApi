from django.contrib.auth.models import Group, User
from .models import Carrers
from rest_framework import serializers

class CarrersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carrers
		fields = ['id', 'username', 'created_datetime', 'title', 'content']