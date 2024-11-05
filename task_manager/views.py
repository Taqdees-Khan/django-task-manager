from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")


task_list = []

@require_http_methods(["GET"])
def view_tasks(request):
    return JsonResponse({'tasks': task_list})

@require_http_methods(["POST"])
def add_task(request):
    task = request.POST.get('description')
    if task:
        task_list.append(task)
    return JsonResponse({'tasks': task_list})

@require_http_methods(["DELETE"])
def delete_task(request, index):
    try:
        del task_list[int(index)]
        return JsonResponse({'tasks': task_list})
    except IndexError:
        return JsonResponse({'error': 'Index out of range'}, status=400)
