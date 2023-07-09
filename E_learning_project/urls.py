from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('App_login.urls'), namespace='App_login')),
    path('', include(('App_student.urls'), namespace='App_student')),
    path('teacher/', include(('App_teacher.urls'), namespace='App_teacher'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
