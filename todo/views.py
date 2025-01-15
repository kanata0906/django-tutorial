from django.shortcuts import render
from django.http import HttpResponse

from todo import models


def list(request):
    # 　データの登録
    new_todo = models.todo()
    new_todo.todo_title = "New Todo"
    new_todo.save()

    # 　データの取得
    all_todo = models.todo.objects.all()
    context = {"todos": all_todo}
    return render(request, "index.html", context)


def edit(request):
    return HttpResponse("edit")


# def delete(request, todo_id):
#     target_todo = models.Todo.objects.get(id=todo_id)
#     todo_id =
#     return HttpResponse

