from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    category_filter = request.GET.get('category', '')

 # Filter berdasarkan title (search)
    if query:
        todos = todos.filter(title__icontains=query)

    # Filter berdasarkan status (completed/pending)
    if status_filter:
        todos = todos.filter(status=status_filter)

    # Filter berdasarkan priority jika ada field priority 
    if priority_filter:
        todos = todos.filter(priority=priority_filter)
    # Filter berdasarkan priority jika ada field category
    if priority_filter:
        todos = todos.filter(category=category_filter)

    paginator = Paginator(todos, 5)
    page_number = request.GET.get('page')
    todos_page = paginator.get_page(page_number)
    
    return render(request, 'todo/list.html', {
        'todos': todos_page,
        'query': query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
    })

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/create.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/confirm_delete.html', {'todo': todo})