from django.conf.urls import url

urlpatterns = [
    # Index Page
    url(r'^$', views.index, name='index'),

    # Sign Up Page
    url(r'^signup$', views.signup, name='signup'),
    # Login Page
    url(r'^login$', views.login, name='login'),
    # User Page
    url(r'^user/(?P<user_id>[0-9]+)$', views.user, name='user'),

    # Article Page
    url(r'^article/(?P<article_id>[0-9]+)$', views.article, name='article'),
    # Article filter by Category (Return list of Article IDs)
    url(r'^ajax/article/category/(?P<category_name>[a-zA-Z]+$', views.article_category, name='article_category'),

    # GET Like Object <- Fixed Regex
    url(r'^ajax/article/(?P<article_id>[0-9]+)/likes$', views.likes, name='get_likes'), # GET - All Likes, POST - New Likes
    # UPDATE (POST|DELETE) Like Object
    url(r'^ajax/article/(?P<article_id>[0-9]+)/likes/(?P<isLike>^-1|[0|1])$', views.update_likes, name='update_likes'), # POST - New Comment, DELETE -  Comment (Put Comment ID in Body)

    # GET Comment Object
    url(r'^ajax/article/(?P<article_id>[0-9]+)/comments$', views.comment, name='comment'), # GET - All Comments, POST - New Comment
    # UPDATE (POST|DELETE) Comment Object
    url(r'^ajax/article/(?P<article_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)$', views.update_comment, name='update_comment'), # POST - New Comment, DELETE -  Comment (Put Comment ID in Body)
]
