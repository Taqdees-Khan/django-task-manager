from django.shortcuts import render
from django.http import HttpResponse

def view_tasks(request):
    # Example response
    return HttpResponse("Here are your tasks.")

def add_task(request):
    # Your logic for adding a task
    return HttpResponse("Task added.")

def delete_task(request, index):
    # Your logic for deleting a task
    return HttpResponse(f"Task {index} deleted.")
