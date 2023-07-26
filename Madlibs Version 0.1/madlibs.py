# MadLibs by Alyssa (Alley) : July 23, 2023 
# ------------------------------------------------------------------------------

# Variables Needed: 
# male_name
# activity (ends in 'ing) 
# location 
# occupation
# celebrity
# emotion
# adjective
# action

# introduction to game 
print("Welcome to MadLibs! A silly story generator. \n")

# ask for the variables
male_name = input("Give me a male name: \n > ")
activity = input("Give me an activity (ends in 'ing) : \n > ")
location = input("Give me a location: \n > ")
occupation = input("Give me an occupation: \n > ")
celebrity = input("Give me the name of a celebrity: \n > ")
emotion = input("Give me an emotion: \n > ")
adjective = input("Give me an adjective: \n > ")
action = input("Give me an action in past tense (ends in 'ed'): \n > ")


# debug test 
print(male_name + activity + location + occupation + celebrity + emotion + adjective + action)


# the story 
print("Once upon a time, there was a man named " + male_name + ". ")
print(male_name + "'s favorite thing to do was" + activity + '. \n')
print("Every single day, " + male_name + " would go out to " + location)
print(" and would go " + activity + ''' for hours at a time. His whole life was about ''' + activity)
print(". Nothing was more important than " + activity +'.')
print('''\n It was the only good thing he had in his life, in between his boring job as a ''' + occupation + '.')
print('''. Then, one day, he met someone who looked just like ''' + celebrity + '.') 
print('''! Being a big fan of them, he decided to approach and say \n''')
print('Excuse me, but has anyone ever told you, you look just like ''' + celebrity + '?')
print("The person just laughed and replied 'I should hope so, I AM ' " + celebrity +  ".")
print(male_name + ''' gasped in excitement, nearly falling over. "I can't believe it! What are YOU doing here, ''' + activity + '?')
print(" I never knew you liked doing that kind of thing!\n")
print("Truth be told, " + celebrity + " looked off to the side, sheepishly, " + '''
 this is my first time ''' + activity + '.' + '''You seem to know what you're doing. I've \n
 been watching you for a bit. Could you give me some pointers?\n''')
print(male_name + " felt " + emotion + ". He had never felt so ") 
print(emotion + " in his entire life! But, how could he say no to " + celebrity + '?' '\n' + '''
 The only problem was, he wasn't a very good teacher and they were not a very good student. \n
 For hours, ''' + male_name + ''' tried to teach ''' + celebrity + ''' the grand art of  ''')
print(" " + activity + ", but it was no use. In the end, when the sun was setting, they both gave up.\n")
print(''' 'I'm sorry,' ''' +  celebrity + ''' expressed in a  ''' + adjective + '''tone of voice,
      which was typical of their usual personality.''' + ''' 'I really tried, but I don't think
        ''' + activity + ''' is for me. it was nice spending time with you, though.' ''')
print(male_name + ' nodded ' + ''' "This was the best day of my life, thank you. ''' )
print('''At that, the two of them ''' + action + ''' and waved goodbye, never to see each other again. ''')
print('THE END.')

# exit
end = input("Press 'enter' to close. > ")