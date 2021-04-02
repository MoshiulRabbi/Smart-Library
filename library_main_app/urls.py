from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('add_books/',views.add_books,name="add_books"),
    path('display_books/',views.display_books,name="display_books"),
    path('borrow/<str:isbn>/',views.borrow,name="borrow"),
    path('display_readers/',views.display_readers,name="display_readers"),
    path('display_donors/',views.display_donors,name="display_donors"),
    path('donate_books/',views.donate_books,name="donate_books")

]
