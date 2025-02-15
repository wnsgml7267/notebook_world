from django.urls import path
from note_book_service import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<prod_id>/', views.product, name='prod_info'),
    path('recommend/', views.cmd, name='recommend'),
    path('recommend/result/', views.recr, name='rec_result'),
    path('recommend/result/<prod_id>', views.product, name='rec_result_info'),
]
