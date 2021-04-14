from django.contrib import admin
from .models import Produto, Grupo


class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'grupo_produto', 'status_produto')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('nome_produto',)
    list_filter = ('grupo_produto',)
    list_editable = ('status_produto',)
    list_per_page = 10


admin.site.register(Produto, ListandoProdutos)
admin.site.register(Grupo)
