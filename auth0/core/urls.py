from django.contrib import admin
from django.urls import path, include
from auth.views import GoogleLogin, UserList, UserDetails, GroupList



urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]