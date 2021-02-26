from django.urls import include, path
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('add_item/', v.add_item, name="add_item"),
    path('edit_item/<task_id>', v.edit_item, name="edit_item"),
    path('done_task/<task_id>', v.done_task, name="done_task"),
    path('undone/<task_id>', v.undone, name="undone"),
    path('delete/<task_id>', v.delete, name="delete"),
]
