from django.urls import path

from . import views

app_name = 'ComicCozy'
urlpatterns = [
    path('', views.ComicView.as_view(), name='index'),
    path('<int:pk>/', views.ComicView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
