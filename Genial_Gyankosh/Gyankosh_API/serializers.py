from rest_framework import serializers
from .models import *


class UserMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        feilds = '__all__'


class ProblemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemMaster
        feilds = '__all__'
