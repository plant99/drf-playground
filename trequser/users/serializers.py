from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "full_name"]

    def get_full_name(self, user):
        return f"{user.first_name} {user.last_name}"

