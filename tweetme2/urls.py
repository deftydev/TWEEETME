from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
from tweets.views  import (
home_view,
tweets_list_view,
tweets_detail_view,
)

from django.views.generic import TemplateView

urlpatterns = [
path('', home_view),
    path('admin/', admin.site.urls),
    path('global/', tweets_list_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('<int:id>',tweets_detail_view),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/tweets/', include('tweets.api.urls')),
    re_path(r'api/profiles?/', include('profiles.api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
