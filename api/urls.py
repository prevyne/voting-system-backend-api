from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoterViewset, VoteViewset, CandidateViewset, PostViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('vote', VoteViewset, basename='vote_viewset')
router.register('voter', VoterViewset, basename='voter_viewset')
router.register('candidate', CandidateViewset, basename='candidate_viewset')
router.register('post', PostViewset, basename='post_viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token refresh'),
]