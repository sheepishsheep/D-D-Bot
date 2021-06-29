#D&D Discord Bot
#Author: Z. Wool
#End goals: 
#Roll dice for:
#           XAny input diceX
#           specfic skill checks
#           specifc spells
#Upload D&DBeyond character sheet and pull skill checks and spell values. 
#repond to dice roles with gifs for Nat ones or Nat 20s
#use mongodb to store PC data (seperate code file)
#update data (spell slots, HP, etc)
#remove encouragment items





import discord #discord lib
import giphy_client #gif lib
import os #token lib
import random #random lib
import requests #request lib
import json #json lib
import re
from replit import db #replit database lib


from giphy_client.rest import ApiException #api for giphy
from discord.ext import commands #discord bot commands

#initiate client call to discord
client =discord.Client()

#sad "trigger" words
sad_words=["sad","depressed","unhappy","miserable","depressing","gloomy"]

#starter encouraging words
starter_ecrg =[
  "Cheer up!",
  "Hang in there",
  "Hold on there kitten",
  "You are adequate"
]

#value to turn responding on/off
if "responding" not in db.keys():
  db["responding"]=True


#update encouragments database
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements=db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"]=encouragements
  else:
    db["encouragements"]=[encouraging_message]

#delete phrase from encouragement database
def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements)>index:
    del encouragements[index]
    db["encouragements"]=encouragements

#show we have logged into discord server
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

#event reactions
@client.event
async def on_message(msg):
  #Say nothing if bot sends
  if msg.author==client.user:
    return
  
  #respond to hello
  if msg.content.startswith('$hello'):
    await msg.channel.send('Hello')

  #turn responding on/off
  if msg.content.startswith("$responding"):
    value = msg.content.split("$responding ",1)[1]
    if value.lower()=="true":
      db["responding"]=True
      await msg.channel.send("Responding is on")
    else:
      db["responding"]=False
      await msg.channel.send("Responding is off")


   #rolls dice based on input
  if msg.content.startswith("$roll"):
    
    dice=msg.content.split("$roll ",1)[1]
    try:
      numdice,dietype,mod=re.split("d|\+",dice)
      diceroll=int(mod);
      for x in range(int(numdice)):
        diceroll+=random.randint(1,int(dietype))
      await msg.channel.send("you rolled "+str(diceroll))
    except:
      try:
        numdice,dietype=re.split("d",dice) 
        mod="0";
        diceroll=int(mod);
        for x in range(int(numdice)):
          diceroll+=random.randint(1,int(dietype))
        await msg.channel.send("you rolled "+str(diceroll))
      except Exception:
        await msg.channel.send("Please enter dice roll in the format of '$roll XdY+Z'")
          
  
    
    







  

  #respond with giphy gif
  if msg.content.startswith("I'm needy"):
    #await msg.channel.send('But that ass is fine')
    api_key=os.getenv('GIFTOKEN')
    api_instance=giphy_client.DefaultApi()

    try:
      api_response = api_instance.gifs_search_get(api_key,"I love you",limit=10)
      lst = list(api_response.data)
      giff=random.choice(lst)

      await msg.channel.send(giff.embed_url)
    
    except ApiException as e:
      print("Exception when calling Api")
      await msg.channel.send("No gif found :(")

  #reply to sad words with encouragements 
  if db["responding"]:
    options=starter_ecrg
    if "encouragements" in db.keys():
      options=options+list(db["encouragements"])

    if any(word in msg.content for word in sad_words):
      await msg.channel.send(random.choice(options))

  #add encouragment to database
  if msg.content.startswith("$new"):
    encouraging_message=msg.content.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await msg.channel.send("New encouraging message added")
    
  #remove encouragment from database
  if msg.content.startswith("$del"):
    encouragements=[]
    if "encouragements" in db.keys():
      index=int(msg.content.split("$del",1)[1])
      delete_encouragment(index)
      encouragements=db["encouragements"]
    await msg.channel.send(encouragements)
  
  #display list of encouragments in database
  if msg.content.startswith("$list"):
    encouragements=[]
    if "encouragements" in db.keys():
      encouragements=list(db["encouragements"])
    await msg.channel.send(encouragements)

  




#retried token ford discord
client.run(os.getenv('TOKEN'))