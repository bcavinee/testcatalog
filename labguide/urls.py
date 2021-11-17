from django.urls import path
from . import views
from users import views as user_views
from testinformation import views as testinformation_views




urlpatterns = [
    path('', testinformation_views.getinfo,name='getinfo'),

]
