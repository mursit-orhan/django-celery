from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path('books/', admin.site.urls),
    # path('authors/', ReviewEmailView.as_view(), name='reviews'),
    # path('book/<id>', include('cafe_api.urls'), name='cafe'),
    # path('author/<id>', include('catalog.urls')),
]