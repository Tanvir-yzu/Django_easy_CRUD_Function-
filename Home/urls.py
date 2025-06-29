from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Company URLs
    path('', views.CompanyList.as_view(), name='company_list'),
    path('companies/', views.CompanyList.as_view(), name='companies'),
    path('company/<int:company_id>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/<int:company_id>/edit/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:company_id>/delete/', views.CompanyDelete.as_view(), name='company_delete'),
    path('company/add/', views.CompanyCreate.as_view(), name='company_add'),
    
    # Employee URLs
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('employee/<int:employee_id>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('employee/<int:employee_id>/edit/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<int:employee_id>/delete/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/add/', views.EmployeeCreate.as_view(), name='employee_add'),
]
