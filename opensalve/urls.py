"""opensalve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from opensalve.views import index


schema_view = get_schema_view(
    openapi.Info(
        title='OpenSalve API',
        default_version='v0.1',
        description='OpenSalve API https://github.com/subins2000/OpenSalve',
        license=openapi.License(name='GPL-3.0'),
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', index),
    path('api/accounts/', include('accounts.urls')),
    path('api/help/', include('help.urls')),
    url(
        '^docs/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
