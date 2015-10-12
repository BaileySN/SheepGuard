from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Sheep, Pasture
from SheepGuard.views import LoginRequiredMixin



class SheepList(LoginRequiredMixin, ListView):
    model = Sheep


class SheepCreate(LoginRequiredMixin, CreateView):
    model = Sheep
    fields = ['code','name','birthdate','date_of_death','state','fk_color','sex','fk_customer','fk_pasture_ground','comments']
    success_url = reverse_lazy('sheep:sheep_list')


class SheepUpdate(LoginRequiredMixin, UpdateView):
    model = Sheep
    fields = ['code','name','birthdate','date_of_death','state','fk_color','sex','fk_customer','fk_pasture_ground','comments']
    success_url = reverse_lazy('sheep:sheep_list')


class SheepDelete(LoginRequiredMixin, DeleteView):
    model = Sheep
    success_url = reverse_lazy('sheep:sheep_list')


class PastureList(LoginRequiredMixin, ListView):
    model = Pasture


class PastureCreate(LoginRequiredMixin, CreateView):
    model = Pasture
    fields = ['name','place','postalcode','comments']
    success_url = reverse_lazy('sheep:pasture_list')


class PastureUpdate(LoginRequiredMixin, UpdateView):
    model = Pasture
    fields = ['name','place','postalcode','comments']
    success_url = reverse_lazy('sheep:pasture_list')


class PastureDelete(LoginRequiredMixin, DeleteView):
    model = Pasture
    success_url = reverse_lazy('sheep:pasture_list')



