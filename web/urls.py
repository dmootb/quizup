from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.core.urls', namespace='core')),  # Include the core app URLs
    # Add more paths as needed
]
