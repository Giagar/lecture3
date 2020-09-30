from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewForm(forms.Form):
    todo = forms.CharField(label="New Task", min_length=2)

# Create your views here.
def index(request):
    if "todos" not in request.session:
        request.session["todos"] = []
    return render(request, "listtodo/index.html", {
        "todos": request.session["todos"]
    })

def add_task(request):
    if request.method == "POST":
        form = NewForm((request.POST))
        if form.is_valid():
            todo = form.cleaned_data["todo"]
            request.session["todos"] += [todo]
            return HttpResponseRedirect(reverse("listtodo:index"))
        else:
            return render(request, "listtodo/add_task.html", {
                "form": form
                })

    return render(request, "listtodo/add_task.html", {
        "form": NewForm(),
    })