from django.urls import path
from . import views

urlpatterns = [
	path('', views.TeacherListView.as_view(), name='list_teacher'),
	path('import/', views.BulkImportView.as_view(), name="import"),
	path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_details')
]