from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.ProductListAPIView.as_view()),
    path("api/<int:pk>/", views.ProductRetrieveAPIView.as_view()),
    path("api/create/", views.ProductCreateAPIView.as_view()),
    path("api/update/<int:pk>/", views.ProductUpdateAPIView.as_view()),
    path("api/delete/<int:pk>/", views.ProductDestroyAPIView.as_view()),
    path("api/", views.ProductListCreateAPIView.as_view()),
    path("api/<int:pk>/", views.ProductRetrieveUpdateAPIView.as_view()),
    path("api/<int:pk>/", views.ProductRetrieveDestroyAPIView.as_view()),
    path("api/<int:pk>/", views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]
