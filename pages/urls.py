from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name="landing-page"),
    path('where-your-money-goes',views.target,name='target'),
]