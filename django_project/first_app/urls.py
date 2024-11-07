
#from django.urls import path
#from . import views
#urlpatterns = [
 #   path("",views.index,name="hi"),
  #  path("hel/",views.hel,name="hello")
#]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_list, name='journal_list'),
    path('index/',views.index,name='box'),
    path('new/', views.journal_create, name='journal_create'),
    path('notes/', views.notes_list, name='notes_list'),
    path('delete/<int:pk>/', views.journal_delete, name='journal_delete'),
]
