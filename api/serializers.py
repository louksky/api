from rest_framework import serializers
from .models import Messeages_H


class Messeages_HSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messeages_H
		fields ='__all__'