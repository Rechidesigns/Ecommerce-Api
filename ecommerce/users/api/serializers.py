from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name" "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }


class Account_Creation (  serializers.ModelSerializer ):

    password = serializers.CharField(write_only=True)

    email = serializers.EmailField(
        help_text=_("The primary email address of the user."))


    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password',]

    def get_cleaned_data(self):
        return {
                'first_name': self.validated_data.get('first_name'),
                'last_name': self.validated_data.get('last_name'),
                'email': self.validated_data.get('email'),
                'password': self.validated_data.get('password'),
        }


    def validate_email(self, value):
        user_exist= User.objects.filter(email=value).exists()
        if user_exist:
            return serializers.ValidationError('This email address used is already taken. Please login!')
        return value


    def validate_contact_number(self, value):
        contact_number= User.objects.filter(contact_number=value).exists()
        if contact_number:
            return serializers.ValidationError('The contact number already exist.')
        return value
    

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = User(**cleaned_data)
        user.set_password(cleaned_data["password"])
        user.save()

