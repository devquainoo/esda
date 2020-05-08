from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('',views.charge, name='charge'),
    # path('client-token',views.client_token,name='client-token'),
    # path('transact/<str:nonce>',views.transact,name='p-transact'),
    path('verify/<str:reference>', views.verify, name='verify'),

]