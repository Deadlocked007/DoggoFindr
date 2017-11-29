from django.conf.urls import url
from . import views
from .views import(
    home,
    about,

)


#For Web URL configuration
app_name = 'doggofindr'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
]
