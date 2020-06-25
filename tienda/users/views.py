from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, TemplateView

from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

import conekta

User = get_user_model()

conekta.api_key = "key_eYvWV7gSDkNYXsmr"
conekta.locale = 'es'


class Indice(TemplateView):
    template_name = 'index.html'


class Salir(LogoutView):
    next_page = reverse_lazy('indice')


class Ingresar(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('indice'))
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse('indice')


class CambiarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('telefono', 'last_name', 'first_name', 'email',)
    success_url = '/'
    template_name = 'perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
