from django.shortcuts import render

tasks = ["foo", "bay", "baz"]

# Create your views here.
def practice_loop(request):
    return render(request, "todolist/practice_loop.html", {
        "tasks": tasks
    })