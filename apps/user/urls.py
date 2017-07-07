from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
# import para ver el token jwt
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^usuario/$', UsuarioDetail.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)