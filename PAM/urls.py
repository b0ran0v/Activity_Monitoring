from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "PAM Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Project_Activity_Monitoring.urls')),
]
