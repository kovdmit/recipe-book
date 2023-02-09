from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from recipe.sitemap import RecipeSitemap

sitemaps = {
    'posts': RecipeSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns = [
    #     path('__debug__/', include('debug_toolbar.urls')),
    # ] + urlpatterns

