from rest_framework import serializers
from .models import Post, Candidate, Vote, Voter

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 
        
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__' 
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__' 
        
class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__' 
        