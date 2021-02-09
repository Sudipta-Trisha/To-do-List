from django.urls import include, path
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('edit_item/<list_id>', v.edit_item, name="edit_item"),
    path('done_task/<list_id>', v.done_task, name="done_task"),
    path('undone/<list_id>', v.undone, name="undone"),
    path('delete/<list_id>', v.delete, name="delete"),
]
