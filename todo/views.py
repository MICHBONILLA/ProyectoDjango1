from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas}
    return render(request, 'todo/home.html', context)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    return render(request, 'todo/agregar.html', {'form': form})

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("home")

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=tarea)
    context = {"form": form}
    return render(request, 'todo/editar.html', context)


# Create your views here.
