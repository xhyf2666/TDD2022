from lists import views
from django.urls import path

urlpatterns = [
    path ('',views.home_page,name='home'),
    path ('lists/the-only-list-in-the-world/',views.view_list,name='view_list'),
    path ('lists/new',views.new_list,name='new_list'),
]
