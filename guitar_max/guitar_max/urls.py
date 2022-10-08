import django.contrib.admin
import django.urls


urlpatterns = [
    django.urls.path('', django.urls.include('main.urls')),
    django.urls.path('admin/', django.contrib.admin.site.urls),
]

if django.conf.settings.DEBUG:
    import django.conf
    import django.conf.urls.static
    import django.contrib.staticfiles.urls
    
    if django.conf.settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            prefix=django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    urlpatterns += django.contrib.staticfiles.urls.staticfiles_urlpatterns()
