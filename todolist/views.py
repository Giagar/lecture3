from django.shortcuts import render

tasks = ["foo", "bay", "baz"]

# Create your views here.
def practice_loop(request):
    return render(request, "todolist/practice_loop.html", {
        "tasks": tasks
    })

def practice_template_page1(request):
    return render(request, "todolist/practice_template_page1.html")


def practice_template_page2(request):
    return render(request, "todolist/practice_template_page2.html")