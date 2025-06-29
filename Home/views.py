from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
import json
from decimal import Decimal
from .models import CompanyInformation, Employee

# Create your views here.
class CompanyList(ListView):
    model = CompanyInformation
    template_name = 'company_list.html'
    context_object_name = 'companies'
    
    def get_queryset(self):
        return CompanyInformation.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.select_related('company')[:10]  # Latest 10 employees
        context['total_companies'] = CompanyInformation.objects.count()
        context['total_employees'] = Employee.objects.filter(is_active=True).count()
        context['recent_employees'] = Employee.objects.select_related('company').filter(is_active=True).order_by('-created_at')[:5]
        return context
    
class CompanyDetail(DetailView):
    model = CompanyInformation
    template_name = 'company_detail.html'
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'

class CompanyCreate(CreateView):
    model = CompanyInformation
    template_name = 'company_form.html'
    fields = ['name', 'email', 'phone', 'address', 'city', 'country', 'website', 'industry', 'employee_count', 'description', 'logo']
    success_url = reverse_lazy('home:company_list')
    
class CompanyUpdate(UpdateView):
    model = CompanyInformation
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
    model = CompanyInformation
    template_name = 'company_confirm_delete.html'
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'
    success_url = reverse_lazy('home:company_list')

# Employee Views
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    paginate_by = 20
    
    def get_queryset(self):
        return Employee.objects.select_related('company')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all employees for JSON (not paginated for Alpine.js functionality)
        all_employees = Employee.objects.select_related('company').all()
        
        # Convert employees to JSON for Alpine.js
        employees_data = []
        for employee in all_employees:
            emp_dict = model_to_dict(employee)
            # Handle date fields
            emp_dict['hire_date'] = employee.hire_date.isoformat() if employee.hire_date else None
            emp_dict['birth_date'] = employee.birth_date.isoformat() if employee.birth_date else None
            # Handle Decimal fields (salary)
            emp_dict['salary'] = float(employee.salary) if employee.salary else None
            # Handle profile picture
            if employee.profile_picture:
                emp_dict['profile_picture'] = employee.profile_picture.url
            else:
                emp_dict['profile_picture'] = None
            # Handle company relationship
            if employee.company:
                emp_dict['company_name'] = employee.company.name
            else:
                emp_dict['company_name'] = None
            # Ensure boolean fields are properly handled
            emp_dict['is_active'] = bool(employee.is_active)
            employees_data.append(emp_dict)
        
        context['employees_json'] = json.dumps(employees_data)
        return context


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['company', 'first_name', 'last_name', 'email', 'phone', 'employee_id', 'position', 'department', 'employment_status', 'salary', 'hire_date', 'birth_date', 'address', 'emergency_contact', 'emergency_phone', 'profile_picture', 'notes']
    success_url = reverse_lazy('home:employee_list')
    
class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['company', 'first_name', 'last_name', 'email', 'phone', 'employee_id', 'position', 'department', 'employment_status', 'salary', 'hire_date', 'birth_date', 'address', 'emergency_contact', 'emergency_phone', 'profile_picture', 'is_active', 'notes']
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'
    success_url = reverse_lazy('home:employee_list')
    
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'
    success_url = reverse_lazy('home:employee_list')
