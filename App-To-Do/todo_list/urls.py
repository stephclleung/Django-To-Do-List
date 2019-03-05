from django.urls import path
from . import views

#WHERE things are

urlpatterns = [
	#path ('what-user-types', actual-urls)
    path('', views.home, name='home_page'),
    path('archive', views.archive, name='archive_page'),
    path('edit/<itemID>', views.edit, name='edit_page'),
    path('add', views.add, name='add_page'),
    path('delete/<itemID>', views.delete, name='delete_page'),
    path('markDone/<itemID>', views.mark_done, name="mark_done_page"),
	path('undoDone/<itemID>', views.undo_done, name="undo_done_page"),
	path('markArchive/<itemID>', views.mark_archive, name="mark_archive_page"),
	path('undoArchive/<itemID>', views.undo_archive, name="undo_archive_page"),
	
]
