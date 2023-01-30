from django.contrib import admin
from django.urls import path, include
from myapp import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('account/', include('django.contrib.auth.urls')),
    

]

urlpatterns += staticfiles_urlpatterns()