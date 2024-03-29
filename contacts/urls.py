from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name="home"),
    path('contact/add', views.contact_add, name="contact_add"),
    # path('contact/delete/<int:pk>', views.contact_delete, name="contact_delete"),
    path('contact/edit/<int:pk>', views.contact_edit, name="contact_edit"),

]