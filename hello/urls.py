
from django.contrib import admin
from django.urls import path ,include


admin.site.site_header = "PHARMASOURCE Admin"
admin.site.site_title = "PHARMASOURCE Admin Portal"
admin.site.index_title = "DATABASE"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

]



