import discord #discord lib
import giphy_client #gif lib
import os #token lib
import random #random lib
import requests #request lib
import json #json lib
import re
from replit import db #replit database lib
import pandas as pd

stats={
  "Race":"",
  "Class":"",
  "Background":"",
  "Initiative":0,
  "Strength":0,
  "Dexterity":0,
  "Constitution":0,
  "Intelligence":0,
  "Wisdom":0,
  "Charisma":0,
  "Defenses":"",
  "Senses":"",
  "Armor Class":0,
  "Speed":0,
  "Languagues":"",
  "Hit Points":{
     "Total":0,
     "Current":0,
     "Temp HP":0,
  },
  "Hit Dice":{
    "Total":0,
    "Successes":0,
    "Failures":0,
    }, 
  "Inspiration":0,
  "Passive Perception":0,
  "Passive Insight":0,
  "Passive Investigation":0,
  "Saving Throws":{
    "Strength":0,
    "Dexterity":0,
    "Constitution":0,
    "Intelligence":0,
    "Wisdom":0,
    "Charisma":0,
  },
  "Skills":{
    "Acrobatics ":0,   
    "Animal Handling ":0,
    "Arcana ":0,
    "Athletics ":0, 
    "Deception ":0,
    "History ":0, 
    "Insight ":0,
    "Intimidation ":0,
    "Investigation ":0,
    "Medicine ":0,
    "Nature ":0,
    "Perception ":0,
    "Performance ":0, 
    "Persuasion ":0,
    "Religion ":0, 
    "Sleight of Hand ":0,
    "Stealth ":0, 
    "Survival ":0
  }, 
  "Actions":"",
  "Specials":{
    "Action":"",
    "Total":"",
    "Remaining":""
  },  
  "Traits":"",
  "Weapons":{
    #Weapon dictonary set up, make new one per spell 
    "Weapon":{ 
      "Name":"",
      "Hit":"",
      "Damage/Type":"",
      "Notes":""
    }
  },
  "Spells":{
    #Spell dictonary set up, make new one per spell 
    "Spell":{
      "Name":"",
      "Level":0,
      "SOURCE":"",
      "SAVE/ATK":0,
      "TIME":"",
      "RANGE":"",
      "COMP":"",
      "DURATION":"",
      "PAGE REF":"",
      "NOTES":""
    }
  },
  "Spell Slots":{
    "First":{
      "Total":0,
      "Used":0
    },
    "Second":{
      "Total":0,
      "Used":0
    },
    "Third":{
      "Total":0,
      "Used":0
    },
    "Fourth":{
      "Total":0,
      "Used":0
    },
    "Fifth":{
      "Total":0,
      "Used":0
    },
    "Sixth":{
      "Total":0,
      "Used":0
    },
    "Seventh":{
      "Total":0,
      "Used":0
    },
    "Eigth":{
      "Total":0,
      "Used":0
    },
    "Ninth":{
      "Total":0,
      "Used":0
    },
  }


}

def char_sheet():


  char_df = pd.read_csv('HaggisHalfbrew.txt',header=None, sep='\t')
  pd.set_option("display.max_rows", None, "display.max_columns", None)
  char_df.columns=["data"]
  charlist=char_df.values.tolist()
  #print ((charlist[23]))

  statcat=[]
  char_stat=stats.copy()
  for skill in char_stat["Skills"]:
    #print(skill)
    for item in charlist:
      if skill in item:
        statcat.append(charlist.index(item))
        char_stat["Skills"][skill]="".join(charlist[charlist.index(item)+58])
    

  return char_stat
  print(statcat)

  #char_stat["Acrobatics"]=char_df.iloc[statcat+58]
  #print(char_stat["Skills"])#["Acrobatics"])