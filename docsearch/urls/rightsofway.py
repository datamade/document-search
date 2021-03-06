from django.urls import path

from docsearch import views

urlpatterns = [
    path('<int:pk>/', views.RightOfWayDetail.as_view(), name="rightofway-detail"),
    path('create/', views.RightOfWayCreate.as_view(), name="rightofway-create"),
    path('search/', views.RightOfWaySearch.as_view(), name="rightofway-search"),
    path('data/', views.RightOfWayData.as_view(), name="rightofway-data"),
    path('update/<int:pk>/', views.RightOfWayUpdate.as_view(), name="rightofway-update"),
    path('delete/<int:pk>/', views.RightOfWayDelete.as_view(), name="rightofway-delete"),
]
