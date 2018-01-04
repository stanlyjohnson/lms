from django.conf.urls import url
from . import views
urlpatterns = [
# url(r'^$', views.welcome, name = "welcome"),
url(r'^author/', views.Author.as_view(), name = "authorpage"),
url(r'^book/', views.Book.as_view(), name = "bookpage"),
url(r'^authorDetails$', views.authordetails, name = "authordetails"),
url(r'^bookDetails$', views.bookdetails, name = "bookdetails"),
]
