from django.contrib import admin
from .models import Service, ServicesImage
from ckeditor.widgets import CKEditorWidget
from django import forms


class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'display']
    prepopulated_fields = {"slug": ("title",)}
    form = ServiceAdminForm


class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicesImage, ServiceImageAdmin)
