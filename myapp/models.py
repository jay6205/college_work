from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    # You can add more options if you want

    def __str__(self):
        return self.title

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    vote_option = models.CharField(max_length=255)

    def __str__(self):
        return f"Vote for {self.poll.title} - {self.vote_option}"
