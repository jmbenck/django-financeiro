from django.contrib import admin

from .models import Movimentacao

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'data_hora', 'descricao', 'valor', 'anexo']
    list_filter = ['tipo', 'data_hora']

admin.site.register(Movimentacao, MovimentacaoAdmin)