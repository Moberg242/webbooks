from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('bookshelf/<int:pk>', views.home, name='home'),
    path('bookshelf/remove/<book_id>/', views.remove, name='remove'),
    path('bookshelf/edit/', views.add, name='edit_bookshelf'),
    path('bookshelf/add/', views.add, name='added'),
    path('addbook/', views.AddBook.as_view(), name='add_book'),
    path('library/<int:page>/<sorted>/', views.Index.as_view(), name='index'),
    path('library/<sorted>/tbr/', views.Tbr.as_view(), name='tbr'),
    path('search/', views.SearchTitle.as_view(), name='search_title'),
    path('book/<int:pk>/', views.BookDetails.as_view(), name='book_details'),
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('book/<int:pk>/update', views.UpdateBook.as_view(), name='update_book'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/theme/', views.change_theme, name='change_theme'),
    path('accounts/color/', views.shelf_color, name='shelf_color'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Used this helpful youtube video as well as django docs to figure out images! https://youtu.be/GNsuF4xB80E?si=MYDA7E6ZrRfeikjK
