from django.urls import path
from .import views

urlpatterns = [
    path('/Home',views.list),
    path('/Contact',views.contact),
    path('/Error',views.error),
    path('/Students',views.list_student),
    path('/Home/<int:id>', views.list_id),
    path('/Students/<int:id>', views.list_id_student),
]