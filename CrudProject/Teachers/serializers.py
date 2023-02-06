from rest_framework import serializers
from .models import TeachersModel


class TeacherSerializer(serializers.Serializer):
    tid = serializers.IntegerField()
    fnm = serializers.CharField(max_length=30)
    lnm = serializers.CharField(max_length=30)
    sal = serializers.FloatField()


    def create(self, validated_data):
        return TeachersModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tid = validated_data.get('tid', instance.tid)
        instance.fnm = validated_data.get('fnm', instance.fnm)
        instance.lnm = validated_data.get('lnm', instance.lnm)
        instance.sal = validated_data.get('sal', instance.sal)
        instance.save()
        return instance