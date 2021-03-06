from django.urls import path

from docsearch import views

urlpatterns = [
    path('<int:pk>/', views.LicenseDetail.as_view(), name="license-detail"),
    path('create/', views.LicenseCreate.as_view(), name="license-create"),
    path('search/', views.LicenseSearch.as_view(), name="license-search"),
    path('data/', views.LicenseData.as_view(), name="license-data"),
    path('update/<int:pk>/', views.LicenseUpdate.as_view(), name="license-update"),
    path('delete/<int:pk>/', views.LicenseDelete.as_view(), name="license-delete"),
]
