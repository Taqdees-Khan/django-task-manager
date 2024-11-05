from django.contrib import admin
from django.urls import path, include
from task_manager import views  # Ensure you have imported your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task_manager.urls')),  # Assuming you have other task-related URLs
    path('', views.home, name='home'),  # Root URL mapping to home view
]
