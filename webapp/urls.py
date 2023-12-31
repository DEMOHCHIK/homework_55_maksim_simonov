from django.urls import path
from webapp.views import home, task_list, task_delete, add_task, task_detail, edit_task


urlpatterns = [
    path('', home),
    path('task_list/', task_list, name='task_list'),
    path('task_delete/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/<int:pk>/edit/', edit_task, name='edit_task'),
    path('add_task/', add_task, name='add_task'),
    path('task/<int:pk>/', task_detail, name='task_detail')
]