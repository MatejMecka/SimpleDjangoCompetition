from django.contrib import admin                                                                                                                      
                                                                                                                                                      
from competition.models import *                                                                                                                      
                                                                                                                                                      
# Register your models here.                                                                                                                          
                                                                                                                                                      
class ParticipantAdmin(admin.ModelAdmin):                                                                                                             
    fieldsets = [                                                                                                                                     
        ('Participant Information', {'fields': ('participant','redditusername','slackusername')}),                                                    
        ('Challenges information', {'fields': ('challengeone','challengetwo','challengethree','challengefour','totalpoints')}),                       
    ]                                                                                                                                                 
                                                                                                                                                      
class EntryAdmin(admin.ModelAdmin):                                                                                                                   
    fieldsets = [                                                                                                                                     
        ('Participant Information', {'fields': ('uuid','participant',)}),                                                                             
        ('Entry Information', {'fields': ('challenge','document','maxpoints',)}),                                                                     
    ]                                         
