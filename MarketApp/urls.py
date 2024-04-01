from django.urls import re_path
from . import views

urlpatterns = [
    re_path('material$', views.material_api),
    re_path('material/([0-9]+)$', views.material_api),

    re_path('seller$', views.seller_api),
    re_path('seller/([0-9]+)$', views.seller_api),
]
