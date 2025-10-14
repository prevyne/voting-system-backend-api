<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import viewsets
from .serializers import VoteSerializer, VoterSerializer, CandidateSerializer, PostSerializer
from .models import Vote, Voter, Candidate, Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class VoteViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer 
    permission_classes = [ IsAuthenticatedOrReadOnly, ]
    
class VoterViewset(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer 
    permission_classes = [ IsAuthenticatedOrReadOnly, ]
    
class CandidateViewset(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer 
    permission_classes = [ IsAuthenticatedOrReadOnly, ]
    
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [ IsAuthenticatedOrReadOnly, ]
    
>>>>>>> 722c5be (api endpoints)
