from django.urls import path
from post.views import all_post, post_detail
# , all_post_api, article_list

urlpatterns = [
    path('', all_post, name="all_post"),
    path('post/<int:id>/', post_detail, name= "pots_detail"),
#     path('postapi/', all_post_api),
#     path('api/posts/', article_list),
]
