# admin.py

from django.contrib import admin
from .models import  Notification, DayUserAssociation, Market

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'created_at')

@admin.register(DayUserAssociation)
class DayUserAssociationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'day')

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'marketuser', 'market_items', 'date')
