from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "index.html"
    potato = "salad!!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "olaar"
        return context

    def say_bye(self):
        return "goodbye!"
