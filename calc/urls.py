# from django.urls import path

# from . import views

# urlpatterns = [
#     path('',views.home, name='home'),
#     path('add',views.add, name="add")
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('travello.urls')),
    path('admin/', admin.site.urls),
]
