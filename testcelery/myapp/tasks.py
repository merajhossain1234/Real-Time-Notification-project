# tasks.py

from celery import shared_task
from .models import Notification, Market, DayUserAssociation
from .serializers import NotificationSerializer, MarketSerializer
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

@shared_task
def send_market_notifications():
    tomorrow = (timezone.now() + timedelta(days=1)).strftime('%A')
    
    # Get users with market date as today
    users_with_market_today = DayUserAssociation.objects.filter(day=tomorrow )

    for association in users_with_market_today:
        user_instance = User.objects.get(username=association.user.username)
        
        # Create Notification instance
        notification_data = {'user': user_instance.pk, 'message': f"Reminder: Market for {user_instance.username} tomorrow."}
        notification_serializer = NotificationSerializer(data=notification_data)

        if notification_serializer.is_valid():
            notification_serializer.save()
            print("Successfully created notification for user with ID:", user_instance.username)
        else:
            print("Failed to create notification for user with ID:", user_instance.username, "Errors:", notification_serializer.errors)

        # Create Market instance
        market_data = {'marketuser': association.pk, 'market_items': 'Your market items here'}  # Add appropriate market_items data
        market_serializer = MarketSerializer(data=market_data)
        
        if market_serializer.is_valid():
            market_serializer.save()
            print("Successfully created market for user with ID:", user_instance.username)
        else:
            print("Failed to create market for user with ID:", user_instance.username, "Errors:", market_serializer.errors)

    print(f"Market notifications for {tomorrow} have been created.")
