from django.urls import path

from . import views
app_name = 'polls'

#The DetailView generic view expects the primary key value captured from
# the URL to be called "pk", so we’ve changed question_id to pk for the generic views.

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),



]