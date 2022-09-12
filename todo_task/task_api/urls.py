from django.urls import path
from .views import TaskAPI

urlpatterns = [
    path('add_task/', TaskAPI.as_view()), # add new task
    path('delete_task/<int:task_id>/', TaskAPI.as_view()), # delete specific task
    path('complete_task/<int:task_id>/', TaskAPI.as_view()), # make is_completed field True for specific task
    path('get_all_tasks/<int:user_id>/', TaskAPI.as_view()), # get all task created by specific user
]
