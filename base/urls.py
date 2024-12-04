from django.urls import path
from .views import ProductTypeViewSet, ProductViewSet, PurchaseViewSet, SellViewSet, CustomersViewSet, SupplierViewSet, DepartmentViewSet, login, register

urlpatterns = [
    path('product-type/',ProductTypeViewSet.as_view({'get':'list','post':'create'})),
    path('product-type/<int:pk>/',ProductTypeViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('product/',ProductViewSet.as_view({'get':'list','post':'create'})),
    path('product/<int:pk>/',ProductViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('purchase/',PurchaseViewSet.as_view({'get':'list','post':'create'})),
    path('purchase/<int:pk>/',PurchaseViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('sell/',SellViewSet.as_view({'get':'list','post':'create'})),
    path('sell/<int:pk>/',SellViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('customers/',CustomersViewSet.as_view({'get':'list','post':'create'})),
    path('customers/<int:pk>/',CustomersViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('supplier/',SupplierViewSet.as_view({'get':'list','post':'create'})),
    path('supplier/<int:pk>/',SupplierViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('department/',DepartmentViewSet.as_view({'get':'list','post':'create'})),
    path('department/<int:pk>/',DepartmentViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('login/',login),
    path('register/',register, name ='register')
]