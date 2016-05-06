from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_date']
    prepopulated_fields = {"slug": ("project_title",)}


admin.site.register(Portfolio, PortfolioAdmin)
