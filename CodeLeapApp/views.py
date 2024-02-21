# from django.shortcuts import render
from .models import Carrers
from rest_framework import permissions, viewsets

from CodeLeapApp.serializers import CarrersSerializer

class CarrersViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows carrers to be viewed or edited.
	"""
	queryset = Carrers.objects.all()
	serializer_class = CarrersSerializer
	# permission_classes = [permissions.IsAuthenticated]
	def perform_update(self, CarrersSerializer):
		rem_field = CarrersSerializer.validated_data.pop('username', None)
		CarrersSerializer.save()