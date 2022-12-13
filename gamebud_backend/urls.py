from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('user/', include('user_profile.urls')),
    path('game/', include('games.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
