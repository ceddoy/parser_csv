from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from parser_csv import settings
from parserapp.views import ItemCreateView, ItemListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_file/', ItemCreateView.as_view(), name='upload'),
    path('items/', ItemListView.as_view(), name='items_list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
