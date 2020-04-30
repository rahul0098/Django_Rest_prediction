from django.conf.urls import url
from .views import FileView,ForUserCreationView
urlpatterns = [
    url('upload', FileView.as_view(), name='file-upload'),
    url('signup/',ForUserCreationView.as_view(),name='usercreation')
]