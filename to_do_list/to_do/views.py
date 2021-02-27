from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    context = {}
    item_number = Task.objects.filter()
    if len(item_number) > 0:
        allTasks = Task.objects.all()
        context = {'allTasks': allTasks}
        return render(request, 'home.html', context)
    else:
        context['start'] = "Free up your mental space adding task in TO-DO List !"
        return render(request, 'home.html', context)


def add_item(request):
    context = {'success': False}
    if request.method == 'POST':
        item = request.POST['item']
        details = request.POST['details']
        print(item, details)
        form = Task(item=item, details=details)
        form.save()
        messages.success(request, 'Item has been added to list.')
        return redirect('/')
    else:
        allTasks = Task.objects.all()
        context = {'allTasks': allTasks}
        return render(request, 'add_item.html', context)

def edit_item(request, task_id):

    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.item = request.POST['item']
        task.details = request.POST['details']
        task.save()
        return redirect('/')

    task = Task.objects.get(id=task_id)
    context = {'task': task}
    # messages.warning(request, 'Item has been Updated.')
    return render(request, 'edit_item.html', context)

def done_task(request, task_id):
    item = Task.objects.get(pk=task_id)
    item.completed = True
    item.save()
    return redirect('/')

def undone(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return redirect('/')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.delete()
        messages.error(request, 'Selected item has been deleted.')
        return redirect('/')

    return render(request, 'delete.html')