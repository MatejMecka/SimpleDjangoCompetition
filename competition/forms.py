from django import forms                                                                                                                              
                                                                                                                                                      
from .models import Participant                                                                                                                       
from .models import Entry                                                                                                                             
class SignUp(forms.ModelForm):                                                                                                                        
        class Meta:                                                                                                                                   
                model = Participant
                fields = ('participant', 'redditusername', 'slackusername')
        def __init__(self, *args, **kwargs):
                super(SignUp, self).__init__(*args, **kwargs)
class Submission(forms.ModelForm):
        class Meta:
                model = Entry
                fields = ('uuid','challenge','document')
        def __init__(self, *args, **kwargs):
                super(Submission, self).__init__(*args, **kwargs)
                self.fields['uuid'].widget.attrs['placeholder'] = 'UUID'
                self.fields['document'].label = "Submission"
