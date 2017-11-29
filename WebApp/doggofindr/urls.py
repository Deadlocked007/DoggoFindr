from django.conf.urls import url
from . import views
from .views import(
    home,

)


#For Web URL configuration
app_name = 'doggofindr'
urlpatterns = [
    url(r'^$', home, name='home'),
]
