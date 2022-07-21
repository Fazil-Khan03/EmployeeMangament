from django.contrib import admin
from django.urls import path,include
from Portal import views

urlpatterns = [
   path("",views.index,name='index'),
   path("all_emp",views.all_emp,name='all_emp'),
   path("rem_emp",views.rem_emp,name='rem_emp'),
   path("rem_emp/<int:emp_id>",views.rem_emp,name='rem_emp'),
   path("add_emp",views.add_emp,name='add_emp'),
   path("filter_emp",views.filter_emp,name='filter_emp')


]
