from django.contrib import admin
from django.urls import path, include

from user.views import show_not_found_error

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tasks/', include('task.urls')),
    path('users/', include('user.urls')),

    path('error/not_found/', show_not_found_error, name='error.not_found')
]
