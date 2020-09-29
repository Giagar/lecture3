from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# tasks = []

class PracticeAddForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value = 1, max_value= 15)

# Create your views here.
def practice_loop(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "todolist/practice_loop.html", {
        "tasks": request.session["tasks"]
    })

def practice_template_page1(request):
    return render(request, "todolist/practice_template_page1.html")


def practice_template_page2(request):
    return render(request, "todolist/practice_template_page2.html")

def practice_add(request):
    if request.method == "POST":
        form = PracticeAddForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todolist:practice_loop"))
        else:
            return render(request, "todolist/practice_add.html", {
                "form": form
            })

    return render(request, "todolist/practice_add.html", {
        "form": PracticeAddForm(),
    })