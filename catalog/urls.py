from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path('product/create/', ProductCreateView.as_view(), name='product_form'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_form'),
    path('<int:pk>/product_confirm_delete/', ProductDeleteView.as_view(), name='product_delete'),
]