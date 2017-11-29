from django.conf.urls import url
from . import views
from .views import(
    home,
    myPage,
    about,
    signup,
    deleteImg,
)


#For Web URL configuration
app_name = 'doggofindr'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^myPage/$', myPage, name='myPage'),
    url(r'^about/$', about, name='about'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^deleteImg/$', deleteImg, name='deleteImg'),
]
