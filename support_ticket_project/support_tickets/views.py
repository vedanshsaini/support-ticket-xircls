# support_tickets/views.py

from rest_framework import generics
from .models import SupportTicket, UserProfile
from .serializers import SupportTicketSerializer, UserProfileSerializer
from .forms import SupportTicketForm

class SupportTicketListCreateView(generics.ListCreateAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(user=user_profile)

class SupportTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
