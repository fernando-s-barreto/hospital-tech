from django.contrib import admin
from django.urls import path, include
from hospitalCC.views import login_view 

urlpatterns = [
    path('admin/', admin.site.urls),

 
    path('', login_view, name='login'),

   
    path('sistema/', include('hospitalCC.urls')),
]
