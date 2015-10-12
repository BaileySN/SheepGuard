from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Title, Profession, Customer
from SheepGuard.views import LoginRequiredMixin



class CustomerList(LoginRequiredMixin, ListView):
    model = Customer


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['fk_title','fname','lname','fk_profession','phone','phone2','fax','email','email2','postalcode','street','place','comments']
    success_url = reverse_lazy('customers:customer_list')


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['fk_title','fname','lname','fk_profession','phone','phone2','fax','email','email2','postalcode','street','place','comments']
    success_url = reverse_lazy('customers:customer_list')


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customers:customer_list')


class ProfessionList(LoginRequiredMixin, ListView):
    model = Profession


class ProfessionCreate(LoginRequiredMixin, CreateView):
    model = Profession
    fields = ['name']
    success_url = reverse_lazy('customers:profession_list')


class ProfessionUpdate(LoginRequiredMixin, UpdateView):
    model = Profession
    fields = ['name']
    success_url = reverse_lazy('customers:profession_list')


class ProfessionDelete(LoginRequiredMixin, DeleteView):
    model = Profession
    success_url = reverse_lazy('customers:profession_list')


class TitleList(LoginRequiredMixin, ListView):
    model = Title



class TitleCreate(LoginRequiredMixin, CreateView):
    model = Title
    fields = ['name']
    success_url = reverse_lazy('customers:title_list')


class TitleUpdate(LoginRequiredMixin, UpdateView):
    model = Title
    fields = ['name']
    success_url = reverse_lazy('customers:title_list')


class TitleDelete(LoginRequiredMixin, DeleteView):
    model = Title
    success_url = reverse_lazy('customers:title_list')



