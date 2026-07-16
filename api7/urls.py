from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.ProductListAPIView.as_view()),
    path("create/", views.ProductCreateAPIView.as_view()),
    path("<int:pk>/retrieve/", views.ProductRetrieveAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),
    path("list-create/", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/retrieve-update/", views.ProductRetrieveUpdateAPIView.as_view()),
    path("<int:pk>/retrieve-delete/", views.ProductRetrieveDestroyAPIView.as_view()),
    path("<int:pk>/retrieve-update-delete/", views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]
