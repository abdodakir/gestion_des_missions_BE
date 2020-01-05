from rest_framework import serializers

from soa.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'last_login', 'username',
        'first_name', 'last_name', 'email', 'date_joined', 'type')
