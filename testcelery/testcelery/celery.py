# celery.py

import os
from celery import Celery
from celery.schedules import crontab



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testcelery.settings')

# Create a Celery instance and configure it with the Django settings.
app = Celery('testcelery')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule={
    'send-market-notifications': {
        'task': 'myapp.tasks.send_market_notifications',
        'schedule': crontab(hour=20, minute=30)
        
    },
    
}
# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')




