from django.contrib import admin
from .models import Usuario


class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_filter = ('username',)
    list_editable = ('is_active',)
    list_per_page = 10


admin.site.register(Usuario, ListandoUsuarios)
