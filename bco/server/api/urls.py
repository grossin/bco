from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList
from .views import UserDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^users/$', UserList.as_view(), name="user_create"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)