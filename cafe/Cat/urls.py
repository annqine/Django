from django.urls import path
from .views import table_reservation, success_page

urlpatterns = [
    path('', table_reservation, name='table_reservation'),
    path('table-reservation', table_reservation, name='table_reservation'),
    path('success-page', success_page, name='success_page'),
]
