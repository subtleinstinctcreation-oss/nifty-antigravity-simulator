from celery import Celery

# Initialize Celery
app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# Configure periodic tasks
app.conf.beat_schedule = {
    'task-name': {
        'task': 'tasks.task_name',  # name of the task to execute
        'schedule': 30.0,          # every 30 seconds
    },
}

# Additional configurations
app.conf.timezone = 'UTC' 
