from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from .models import todo_models
from .forms import todo_forms

def index(request):
	form = todo_forms
	data = todo_models.objects.order_by('-id')
	context = {'todo_list': data, 'form':form}
	return render(request, 'todo_app/index.html', context)


@require_POST
def addTo(request):
	form = todo_forms(request.POST)

	if form.is_valid():
		new_todo = todo_models(task = request.POST['task'])
		new_todo.save()

	return redirect('index')

def complete(request, todo_id):
	todo = todo_models.objects.get(pk = todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def delete_comp(request):
	todo_models.objects.filter(complete__exact=True).delete()

	return redirect('index')

def delete_all(request):
	todo_models.objects.all().delete()

	return redirect('index')