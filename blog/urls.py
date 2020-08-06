from django.urls import path
from .views import home, post_detail,CategoryPostDetailView,category_post_list

urlpatterns = [
    path('', home, name="blog-home"),
    path('post/<int:pk>/', post_detail, name="post-detail"),
    path('category/<int:pk>/',category_post_list,name="category"),
    #path('category/<int:pk>/',CategoryPostDetailView.as_view(), name="cat-detail")
]
