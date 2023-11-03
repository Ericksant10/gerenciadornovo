from django.urls import path
from . import views

urlpatterns = [
    path('materia/', views.materia_lista, name='materia_lista'),
    path('materia/remover/<int:materia_id>/', views.remover_materia, name='remover_materia'),

    # Defina URLs para outras views aqui
]
