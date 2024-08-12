from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    
    return render(request,'list.html',{'tasks':tasks,'form':form})

def update(request,pk):
    pk = int(pk)
    task =Task.objects.get(id=pk)
    form =TaskForm(instance=task)
    if request.method =='POST':
        form=TaskForm(request.POST or None,instance=task)

        if form.is_valid():
            form.save()
        return redirect('/')
    
    return render(request,'update.html',{'form':form})


def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('list')


