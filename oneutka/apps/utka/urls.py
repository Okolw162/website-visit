from django.urls import path

from . import views

app_name = 'utka'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:utka_id>/', views.detail, name = 'detail'),
	path('<int:utka_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]

# /utka/
# /utka/1/