#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:34:13 2019

author: theavenger@intergalactic a.k.a Sony Wicaksono
"""
## Define a function that responds to a user's message: respond
## It is a traditional dialogue modelling and yet implement natural language understanding (NLU)

import re
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

rules = {'I want (.*)': ['What would it mean if you got {0}',
  'Why do you want {0}',
  "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
  'Do you wish that {0}',
  'What do you think about {0}',
  'Really--if {0}']}

def send_message(message):
    # print user_template including the user_message
    print(user_template.format(message))
    # get the bot response
    response = respond(message)
    print(bot_template.format(response))
    
def match_rule(rules, messages):
    response, phrase = "default", None
    
    for pattern, responses in rules.items():
        match = re.search(pattern, messages)
        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    return response.format(phrase), phrase

#Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)

# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("Do you remember your last birthday")
send_message("Do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")