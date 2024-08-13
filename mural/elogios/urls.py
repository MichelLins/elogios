from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_elogios, name='lista_elogios'),
    path('adicionar/', views.adicionar_elogio, name='adicionar_elogio'),
    path('excluir/<int:id>/', views.excluir_elogio, name='excluir_elogio'),  # Nova rota para excluir elogio
]
