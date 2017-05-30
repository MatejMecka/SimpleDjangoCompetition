# -*- coding: utf-8 -*-

import django
import os
from slackclient import SlackClient
import random

os.environ["DJANGO_SETTINGS_MODULE"] = 'Competition.settings'
django.setup()
from competition.models import Participant

greets = ['Hello','Hallo','Hola','Привиет','Здраво']

slack_token = "slacktoken"
sc = SlackClient(slack_token)

participants = Participant.objects.all()

for Participant in participants:

	greet = random.choice(greets)
	participant = Participant.participant
	uuid = Participant.uuid
	slackusername = "@" + Participant.slackusername
	print "Messaging: " + participant  + "on Slack with the username: " + slackusername + " with UUID " + str(uuid)

	sc.api_call(
	        "chat.postMessage",
	        channel=slackusername,
	        text="*" + greet + "* I am the @namehere bot. I'll be the one sending you announcments and information during the Competition. I don't recieve direct commands so please don't message me.\n This is your UUID key: " + str(uuid) + ". You’ll use it during the competition. When you fill out the Entry form or submitting a project you have to have the UUID else your entry would not count.\n _Thank you for signing up and see you on the Competition_",
	        icon_url = "urltoicon",
	        username = "usernamehere"
	        )
