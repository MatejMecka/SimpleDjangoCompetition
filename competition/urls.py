from django.conf.urls import url                                                                                                                      
from . import views                                                                                                                                   
from django.conf.urls import include                                                                                                                  
urlpatterns = [                                                                                                                                       
    url(r'^$', views.default, name='index'),                                                                                                          
    url(r'^app', views.application, name='formtofill'),                                                                                               
    url(r'^challenges',views.challengeslist, name='chl'),                                                                                                         
    url(r'^leaderboard',views.leaderlist,name="led"),                                                                                                 
    url(r'^entry',views.submitentry,name="compentry")                                                                                                 
]   
