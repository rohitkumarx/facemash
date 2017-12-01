from django.db.models import Q
from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
)

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType



User = get_user_model()
class UserCreateSerializer(ModelSerializer):
    email = EmailField(label = 'Email')
    email2 = EmailField(label = 'Confirm Email', allow_blank=False, write_only=True)#https://stackoverflow.com/questions/27591184/additional-serializer-fields-in-django-rest-framework-3
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        return data
    
    def validate_email(self, value):
        data = self.get_initial()
        print data
        email1 = data.get('email2')
        email2 = value
        if email1 != email2:
            raise ValidationError('Email must be same.') 
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError('User with this email is already present.')
        return value
    def validate_email2(self, value):
        data = self.get_initial()
        print data
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Email must be same.') 
        return value
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank = True, read_only = True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label = 'Email', required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'token',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)
        if not email and not username:
            raise ValidationError('A username or email is required.')

        user = User.objects.filter(
            Q(email = email) |
            Q(username = username)
        ).distinct()
        #user = user.exclude(email__is_null=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This email/username is not valid.')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect password.')

        data["TOKEN"] = "Some random token"
        return data

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]