"""
Module that supplies all the views for the Lists app
"""
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    """
    Renders our simple home_page view and process POST requests
    """
    return render(request, "home.html")


def new_list(request):
    """
    Creates a new list
    """
    Item.objects.create(text=request.POST["item_text"])
    return redirect("/lists/the-first-list/")


def view_list(request):
    """
    Renders an specific list with all its items
    """
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})
