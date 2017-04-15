from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'dob', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')