from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('school.urls')),
                  path('auth/', include('home_auth.urls')),
                  path('student/', include('student.urls')),
                  path('teacher/', include('teacher.urls')),
                  path('department/', include('department.urls')),
                  path('subject/', include('subject.urls')),
                  path('class/', include('class_group.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
