from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    group_id = serializers.IntegerField()
    full_name = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
