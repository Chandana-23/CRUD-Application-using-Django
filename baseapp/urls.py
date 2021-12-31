from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('add',views.add,name='add'),
    path('read',views.read,name='read'),
    path('update',views.update,name='update'),
    path('delete/<str:roll>',views.delete,name='delete'),
    path('deleteall',views.deleteall,name='deleteall'),
]
