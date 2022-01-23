from django.conf.urls import url
from tata_api import views

urlpatterns = [
    url(r'^api/tata_rec$', views.rec_list),
]