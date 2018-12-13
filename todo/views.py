from django.shortcuts import render, redirect
from django import forms
from todo.models import Posting
from .forms import PostingForm

# Create your views here.

def index(request):
    form = PostingForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    new_text = Posting.objects.all().order_by("-id")
    contexts = {"form":form, "new_text":new_text}
    return render(request, "todo/index.html", contexts)        