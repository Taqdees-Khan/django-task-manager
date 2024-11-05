from django.urls import path
from tasks.views import view_tasks, add_task, delete_task  # Import from tasks

urlpatterns = [
    path('view/', view_tasks, name='view_tasks'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:index>/', delete_task, name='delete_task'),
]
