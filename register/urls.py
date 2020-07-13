from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fez-a-escolha-certa', views.welcome, name='welcome'),
    path('lideres', views.leaderboard, name='leaderboard'),
    path('<str:vector_id>/:)', views.regi, name='regi'),
    path('<str:vector_id>/:)/<str:client_id>', views.regi2, name='regi2'),
    path('<str:vector_id>/OwO', views.subm, name='subm'),
    path('acompanhar/<str:vector_id>', views.vec_page, name='vec_page'),
]
