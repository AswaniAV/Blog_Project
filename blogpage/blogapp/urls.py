from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recentpost/', views.recentpost, name='recentpost'),
    path('addpost/', views.addpost, name='addpost'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/update/<int:article_id>/', views.article_update, name='article_update'),
    path('article/delete/<int:article_id>/', views.article_delete, name='article_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)