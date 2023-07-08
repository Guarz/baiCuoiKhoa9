from django.urls import path, include
from django.contrib import admin 
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('/Home',views.list),
    path('/Contact',views.contact),
    path('/Error',views.error),
    path('/Students',views.list_student),
    path('/Home/<int:id>', views.list_id),
    path('/Students/<int:id>', views.list_id_student),
    path('/teachers/new/',views.Teachers_new, name='Teachers_new'),
    path('/accounts/', include('django.contrib.auth.urls')),
    # path('/login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # path('/logout/',auth_views.LogoutView.as_view(next_page='/myHome/login'),name='logout'),
]