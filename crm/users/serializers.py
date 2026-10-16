from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from academics.models import Group
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        validators=[validate_password],
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.filter(is_active=True),
        allow_null=True,
        required=False,
    )
    group_name = serializers.CharField(source='group.name', read_only=True, default=None)

    class Meta:
        model = Student
        fields = [
            'id', 'username', 'password',
            'first_name', 'last_name', 'middle_name', 'email',
            'birth_date', 'phone', 'student_id',
            'group', 'group_name',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.set_password(password)
        student.save()
        return student

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
