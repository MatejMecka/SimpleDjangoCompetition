import datetime                                                                                                                                       
                                                                                                                                                      
from django.db import models                                                                                                                          
                                                                                                                                                      
import uuid                                                                                                                                           
                                                                                                                                                      
from django.db import models                                                                                                                          
                                                                                                                                                      
# Create your models here.                                                                                                                            
                                                                                                                                                      
class Participant(models.Model):                                                                                                                      
        def __unicode__(self):                                                                                                                        
                return "Participant: " +  str(self.uuid)                                                                                              
        uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)                                                                 
        participant = models.CharField(max_length=30, blank=False)                                                                                    
        redditusername = models.CharField("Reddit Username",max_length=21)                                                                            
        slackusername = models.CharField("Slack Username", max_length=21)                                                                             
        challengeone = models.IntegerField("Points for challenge 1", blank=True)      # I suck At Designing Models.                                                                
        challengetwo = models.IntegerField("Points for challenge 2", blank=True)                                                                      
        challengethree = models.IntegerField("Points for challenge 3",blank=True)                                                                     
        challengefour = models.IntegerField("Points for challenge 4",blank=True)
        totalpoints = models.IntegerField("Points for all challenges ",blank=True)
        def save(self, *args, **kwargs): 
            self.totalpoints = int(self.challengeone) + int(self.challengetwo) + int(self.challengethree) + int(self.challengefour)
            super(Participant, self).save(*args, **kwargs)


class Challenge(models.Model):
        def __unicode__(self):
                return "Challenge: " + self.nameofchallenge
        nameofchallenge = models.CharField("Name of Challenge", max_length=50, blank=False)
        description = models.TextField("Description",max_length=2100)
        maximumpoints = models.CharField("Maximum Points", max_length=21)
        completed = models.CharField("People that completed it",max_length=150)

class Entry(models.Model):
        def __unicode__(self):
                return "Entry by: " + self.uuid
        uuid = models.CharField(max_length=30,null=True,blank=True)
        challenge = models.ForeignKey('competition.Challenge',related_name="challen")
        participant = models.ForeignKey('competition.Participant',related_name="particip",null=True,blank=False)
        maxpoints = models.CharField("Points earned",max_length=150,blank=False)
        document = models.FileField(upload_to='entries/%d/',null=True,blank=True)
