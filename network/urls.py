from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)
router.register('followup', views.FollowUpViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("index/", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts/<int:pk>/comments", views.PostComments),
    path('api-auth', include('rest_framework.urls')),
    path('api-token-auth', CustomAuthToken.as_view()),
    # path("posts/", views.PostViewLC.as_view()),
    # path("posts/<int:pk>", views.PostViewRUD.as_view()),
    # path("comments", views.CommentViewLC.as_view()),
    # path("comments/<int:pk>", views.CommentViewRUD.as_view()),
    # path("postsq/<int:pk>", views.PostCommentViewRUD.as_view()),

]
