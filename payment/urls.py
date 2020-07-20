from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('',views.charge, name='charge'),
    path('with-rave',views.flutterwave_rave_charge,name='rave-charge'),
    path('verify-rave',views.verify_rave,name='rave-verify'),
    # path('client-token',views.client_token,name='client-token'),
    # path('transact/<str:nonce>',views.transact,name='p-transact'),
    path('verify/<str:reference>', views.verify, name='verify'),

]