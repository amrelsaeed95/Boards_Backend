from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter  


router = DefaultRouter()
router.register('boards', views.BoardViewset, basename='boards')


urlpatterns = [
    # path('', views.BoardList.as_view(), name='home'),
    # path('board_details/<int:id>/', views.BoardDetails.as_view(), name='board_details'),

    # path('boards/<int:board_id>/', views.BoardTopics.as_view(), name='board_topics'),
    # path('boards/<int:board_id>/new/', views.new_topic, name='new_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name='topic_posts'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]


urlpatterns = urlpatterns + router.urls  
