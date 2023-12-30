from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import table_reservation, success_page, menu, menu_recipe, register, login_view, logout_view

urlpatterns = [
    path('', table_reservation, name='table_reservation'),
    path('table-reservation', table_reservation, name='table_reservation'),
    path('table-reservation/<str:date>/', table_reservation, name='table_reservation_with_date'),
    path('success-page', success_page, name='success_page'),
    path('menu', menu, name='menu'),
    path('recipes/<int:recipe_id>/', menu_recipe, name='menu_recipe'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
