
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from todolist_app import views as todolist_views
from django.conf import settings # type: ignore # new
from django.conf.urls.static import static # type: ignore #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('account/', include('users_app.urls')),
    path('todolist/', include('todolist_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)