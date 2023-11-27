from django.urls import path
from webapp.views import home, task_list, task_delete


urlpatterns = [
    path('', home),
    path('task_list/', task_list, name='task_list'),
    path('task_delete/<int:task_id>/', task_delete, name='task_delete')
]