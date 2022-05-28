# we use the include for path another url from blog to have multiple page on it 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

# for make new folder and help to show how show picturs
# we found this from djjango statics in website of django 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
