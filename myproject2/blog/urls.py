from django.urls import path,re_path
from . import views
urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$',views.archive_by_year, name='archive'),
    path('article/<int:year>/<int:month>/', views.article_details, name='article_details'),
]