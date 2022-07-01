""" 
    URLconf: 
                Aseguradora de vistas a URLs 
"""

from django.urls import path
from . import views

app_name = 'app'
"""" Default view """
urlpatterns = [
    # ex: /app/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /app/<id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /app/<id>/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /app/<id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]