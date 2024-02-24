# views.py

from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .tasks import send_market_notifications


def notifiction_view_function(request):
    try:
        
        send_market_notifications.apply_async()

        print("Successfully sent notification asynchronously.")
        return HttpResponse("Task triggered successfully")
    except Exception as e:
        print("Error:", str(e))
        return HttpResponse("Error triggering task. Check logs for details.", status=500)
