from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.Serializer):
    rn = serializers.IntegerField()
    fnm = serializers.CharField()
    lnm = serializers.CharField()
    mk = serializers.FloatField()

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.rn = validated_data.get('rn',instance.rn)
        instance.fnm = validated_data.get('fnm',instance.fnm)
        instance.lnm = validated_data.get('lnm',instance.lnm)
        instance.mk = validated_data.get('mk', instance.mk)
        instance.save()
        return instance