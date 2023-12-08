from django.contrib import admin
from .models import UserProfile, SupportTicket

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar')

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'status')
