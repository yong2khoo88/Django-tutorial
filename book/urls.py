from book import views
from django.urls import re_path, path


#app_name = 'book'

urlpatterns=[
    path('',views.index, name='index'),
    path('create2/',views.create2, name='create-book'),
    path('update/<int:book_id>',views.update_book),
    path('delete/<int:book_id>',views.delete_book)
    # MEDIA
]
