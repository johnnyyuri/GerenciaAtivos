from django.contrib import admin
from django.urls import path
from crud_ativos.views import listagem, new_ativo, new_colab, updateativo, updatecolab, deleteativo, deletecolab

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listagem/', listagem, name='url_list'),
    path('addativo/', new_ativo, name='url_nuativo'),
    path('addcolab/', new_colab, name='url_nucolab'),
    path('updateativo/<int:pk>/', updateativo, name='url_updativo'),
    path('updatecolab/<int:pk>/', updatecolab, name='url_updcolab'),
    path('deleteativo/<int:pk>/', deleteativo, name='url_delativo'),
    path('deletecolab/<int:pk>/', deletecolab, name='url_delcolab')
]