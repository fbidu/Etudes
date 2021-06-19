from django.views.generic import CreateView, ListView, DetailView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese


class CheeseCreateView(CreateView):
    model = Cheese
    fields = ["name", "description", "firmness", "country_of_origin"]