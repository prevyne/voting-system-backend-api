from django.db import models


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    jurisdiction = models.CharField(max_length=200)

    def __str__(self):
        return f"ID: {self.post_id} , Title: {self.title} , Jurisdiction: {self.jurisdiction}"


class Candidate(models.Model):

    candidate_id = models.IntegerField(primary_key=True)
    candidate_name = models.CharField(max_length=200)
    party = models.CharField(max_length=50)
    office = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_sought')

    def __str__(self):
        return self.candidate_name


class Voter(models.Model):
    voter_id = models.IntegerField(primary_key=True)
    voter_name = models.CharField(max_length=50)

    def __str__(self):
        return self.voter_id


class Vote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    voter = models.ForeignKey(
        Voter, on_delete=models.CASCADE, related_name='vote_caster')
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='voted_candidate')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='voted_office')

    def __str__(self):
        return self.vote_id
