from django.urls import path
from .views import UserList,UserCreate,UserDetail,UserUpdate,UserDelete

'''
API endpoint для СRUD методов
'''

urlpatterns = [
path('',UserList.as_view(),name='list'),
path('create/',UserCreate.as_view(),name='create'),
path('<int:id>/',UserDetail.as_view(),name='detail'),
path('<int:id>/delete',UserDelete.as_view(),name='delete'),
path('<int:id>/update',UserUpdate.as_view(),name='update')
]
