# support_tickets/serializers.py

from rest_framework import serializers
from .models import SupportTicket, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = SupportTicket
        fields = '__all__'
