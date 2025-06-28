from django.contrib import admin
from django.utils.html import format_html
from .models import companyInformation

@admin.register(companyInformation)
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

# Register your models here.
