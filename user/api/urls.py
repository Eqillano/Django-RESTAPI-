from django.urls import path
from .views import UserList,UserCreate,UserDetail,UserUpdate,UserDelete

'''
API endpoint для СRUD методов
'''

urlpatterns = [
path('',UserList.as_view(),name='list'),
path('create/',UserCreate.as_view(),name='create'),
path('<int:id>/',UserDetail.as_view(),name='detail'),
path('delete/<int:id>',UserDelete.as_view(),name='delete'),
path('update/<int:id>',UserUpdate.as_view(),name='update')
]
