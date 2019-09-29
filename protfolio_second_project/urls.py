import sys
sys.path.append('/root/python_workspace/')
from django.contrib import admin
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from Python_Django.protfolio_second_project.jobs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
# path('jobs/', include('jobs.urls')),
    path("", views.home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
