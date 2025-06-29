from django.contrib import admin
from django.utils.html import format_html
from .models import CompanyInformation, Employee

@admin.register(CompanyInformation)
class CompanyInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'country', 'industry', 'logo_preview')
    list_filter = ('industry', 'country', 'city')
    search_fields = ('name', 'email', 'phone', 'address', 'description')
    readonly_fields = ('created_at', 'updated_at', 'logo_preview')
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "No Logo"
    logo_preview.short_description = 'Logo Preview'

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'phone', 'website', 'logo', 'logo_preview')
        }),
        ('Location', {
            'fields': ('address', 'city', 'country')
        }),
        ('Company Details', {
            'fields': ('industry', 'employee_count', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_name', 'position', 'department', 'company', 'employment_status', 'hire_date', 'is_active', 'profile_preview')
    list_filter = ('department', 'employment_status', 'company', 'is_active', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'employee_id', 'position')
    readonly_fields = ('created_at', 'updated_at', 'profile_preview')
    list_editable = ('is_active',)
    date_hierarchy = 'hire_date'
    
    def profile_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.profile_picture.url)
        return "No Photo"
    profile_preview.short_description = 'Profile Photo'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'birth_date', 'address')
        }),
        ('Employment Details', {
            'fields': ('company', 'employee_id', 'position', 'department', 'employment_status', 'hire_date', 'salary', 'is_active')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact', 'emergency_phone'),
            'classes': ('collapse',)
        }),
        ('Profile & Notes', {
            'fields': ('profile_picture', 'profile_preview', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

# Register your models here.
