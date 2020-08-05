from django.urls import path
from .views import home, post_detail,CategoryPostDetailView

urlpatterns = [
    path('', home, name="blog-home"),
    path('post/<int:pk>/', post_detail, name="post-detail"),
    path('category/<int:pk>/',CategoryPostDetailView.as_view(), name="cat-detail")
]
