from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import table_reservation, success_page, menu, menu_recipe

urlpatterns = [
    path('', table_reservation, name='table_reservation'),
    path('table-reservation', table_reservation, name='table_reservation'),
    path('success-page', success_page, name='success_page'),
    path('menu', menu, name='menu'),
    path('recipes/<int:recipe_id>/', menu_recipe, name='menu_recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
