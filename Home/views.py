from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import companyInformation

# Create your views here.
class CompanyList(ListView):
    model = companyInformation
    template_name = 'company_list.html'
    context_object_name = 'companies'
    
    def get_queryset(self):
        return companyInformation.objects.all()
    
class CompanyDetail(DetailView):
    model = companyInformation
    template_name = 'company_detail.html'
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'

class CompanyCreate(CreateView):
    model = companyInformation
    template_name = 'company_form.html'
    fields = ['name', 'email', 'phone', 'address', 'city', 'country', 'website', 'industry', 'employee_count', 'description', 'logo']
    success_url = reverse_lazy('home:company_list')
    
class CompanyUpdate(UpdateView):
    model = companyInformation
    template_name = 'company_form.html'
    fields = ['name', 'email', 'phone', 'address', 'city', 'country', 'website', 'industry', 'employee_count', 'description', 'logo']
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'
    success_url = reverse_lazy('home:company_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Company'
        return context

class CompanyDelete(DeleteView):
    model = companyInformation
    template_name = 'company_confirm_delete.html'
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'
    success_url = reverse_lazy('home:company_list')