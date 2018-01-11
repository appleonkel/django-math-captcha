from django.views.generic.edit import FormView
from .forms import Form


class View(FormView):
    template_name = 'form.html'
    form_class = Form
    success_url = '/valid/'

    def form_valid(self, form):
        return super().form_valid(form)
