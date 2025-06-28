from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.CompanyList.as_view(), name='company_list'),
    path('companies/', views.CompanyList.as_view(), name='companies'),
    path('company/<int:company_id>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/<int:company_id>/edit/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:company_id>/delete/', views.CompanyDelete.as_view(), name='company_delete'),
    path('company/add/', views.CompanyCreate.as_view(), name='company_add'),
]