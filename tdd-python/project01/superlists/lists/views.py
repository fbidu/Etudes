"""
Module that supplies all the views for the Lists app
"""
from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    """
    Renders our simple home_page view and process POST requests
    """
    return render(request, "home.html")


def new_list(request):
    """
    Creates a new list
    """
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def view_list(request, list_id):
    """
    Renders an specific list with all its items
    """
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, "list.html", {"list": list_})
