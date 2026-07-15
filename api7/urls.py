from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view(), name="product-list"),
    path("products/create/", views.ProductCreateAPIView.as_view(), name="product-create"),
    path("products/<int:pk>/", views.ProductRetrieveAPIView.as_view(), name="product-detail"),
    path("products/update/<int:pk>/", views.ProductUpdateAPIView.as_view(), name="product-update"),
    path("products/delete/<int:pk>/", views.ProductDestroyAPIView.as_view(), name="product-delete"),\
    path("products/detail-update/<int:pk>/", views.ProductRetrieveAPIView.as_view(), name="product-detail-update"),

]