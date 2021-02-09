from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added to list.')
            return redirect('/')
    else:
        all_items = List.objects.all
        context = {'all_items': all_items}
        return render(request, 'home.html', context)

def edit_item(request, list_id):
    item = List.objects.get(id=list_id)

    if request.method == 'POST':
        item = List.objects.get(id=list_id)
        item.item = request.POST['item']
        item.save()
        return redirect('/')
    context = {'item': item}
    #messages.warning(request, 'Item has been Updated.')
    return render(request, 'edit_item.html', context)

def undone(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('/')

def done_task(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('/')

def delete(request, list_id):
    item = List.objects.get(pk=list_id)

    if request.method == 'POST':
        item.delete()
        messages.error(request, 'Selected item has been deleted.')
        return redirect('/')

    return render(request, 'delete.html')


