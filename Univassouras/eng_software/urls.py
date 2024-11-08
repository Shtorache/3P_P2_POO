from django.urls import path
from . import views 

urlpatterns = [

    path('', views.index, name='index'),
    path('curso/', views.curso, name='curso'),  
    path('processo-seletivo/', views.processo_seletivo, name='processo_seletivo'),  
    path('publico-alvo/', views.publico_alvo, name='publico_alvo'),  
    path('investimento/', views.investimento, name='investimento'), 
    path('onde-fazer/', views.onde_fazer, name='onde_fazer'),  
]
