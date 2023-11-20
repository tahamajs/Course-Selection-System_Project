from rest_framework.routers import DefaultRouter
from . import views

app_name = 'course'
router = DefaultRouter()
router.register(r'registration-update', views.RegistrationUpdateViewSet)

urlpatterns = router.urls

# [<URLPattern '^registration-update/$' [name='registrationupdate-list']>, <URLPattern '^registration-update\.(
# ?P<format>[a-z0-9]+)/?$' [name='registrationupdate-list']>, <URLPattern '^registration-update/(?P<pk>[^/.]+)/$' [
# name='registrationupdate-detail']>, <URLPattern '^registration-update/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [
# name='registrationupdate-detail']>, <URLPattern '^$' [name='api-root']>, <URLPattern '^\.(?P<format>[a-z0-9]+)/?$'
# [name='api-root']>]
