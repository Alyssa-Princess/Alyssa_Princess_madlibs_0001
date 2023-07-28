# July 26, 2023 
# MADLIBS Version 0.2 

# NOTE TO SELF: (Try to make this one more polished, PLEASE!!!!) 

# Story Title: The Fruity Princess 

# variables 
fruit =             input("Give me the name of a fruit \n > ") # name for princess and her people
rival_fruit =       input("Give me the name of another fruit \n > ") # name for sister and her people
veggie =            input("Give me the name of a vegetable \n > ") # name for evil rival kingdom
junk =              input("Give me the name of a junk food \n > ") # secret
activity =          input("Give me the name of an activity (ends in 'ing) \n > ") # princess's favorite 
rival_activity =    input("Give me the name of another activity (ends in 'ing) \n > ") # sister's favorite
evil_activity =     input("Give me the name of one more activity (ends in 'ing) \n > ") # evil's fav 
celebrity =         input("Give me the name of a celebrity \n > ") # does not need explaining                   
location =          input("Give me a location \n > ") # princess' favorite hangout spot 
large_object =      input("Give me tha name of a large object \n > ")

# turn into names by  capitalizing the  first letter
fruit =             fruit.title()
rival_fruit =       rival_fruit.title()
veggie =            veggie.title()



# plural variables 
fruit_plural =          str.lower(fruit + "s")
rival_fruit_plural =    str.lower(rival_fruit + "s")
veggie_plural =         str.lower(veggie + 's')
junk_plural =           str.lower(junk + 's')

# fruit plural fix 
if fruit ==             "Strawberry":
    fruit_plural ==     str.lower("strawberries")
elif fruit ==           "Blueberry":
    fruit_plural =      str.lower("blueberries")
elif fruit ==           "Blackberry":
    fruit_plural =      str.lower("Blackberries")
elif (fruit == "raspberry") or (fruit == 'rasberry') or (fruit == 'razberry'):
    fruit_plural =      str.lower("raspberries")



# rival fruit plural fix 
if rival_fruit ==           "Strawberry":
    rival_fruit_plural ==   str.lower("strawberries")
elif rival_fruit ==         "Blueberry":
    rival_fruit_plural =    str.lower("blueberries")
elif rival_fruit ==         "Blackberry":
    rival_fruit_plural =    str.lower("blackberries")
elif (rival_fruit == "Raspberry") or (rival_fruit == 'Rasberry') or (rival_fruit == 'Razberry'):
    rival_fruit_plural =     str.lower("raspberries")



# story 
print("Once upon a time, there was a young princess named " + fruit + 
    ". Princess " + fruit + ''' was a happy girl, always playing in the \n'''
    + location + ''' with the local peasants, all of which  were living, breathing '''
    + fruit_plural + '''. \n She found it silly that she had the same name as the kind of fruit
    they were, but didn't think on it too much. \n
    \n She had a sister, Princess ''' + rival_fruit + 
    ''', who was much older and married to Prince ''' + veggie + 
    '''.\n He was not a nice man and had even tried to kill all of her sister's fruit peasants 
    shortly after the wedding. \nThere were barely any ''' + rival_fruit_plural + 
    ''' left, save for a few that has escaped to the safetly of a nearby ''' 
    + large_object + '''.\n Princess ''' + fruit + ''' HATED Prince ''' + veggie + 
    ''' and decided to write a letter to him. \n It read:''' + 
    '''\n Dear Prince ''' + veggie + ''' \n You are mean and stupid and ugly. I hate you and I hate ''' 
    + veggie_plural + '''!!! \n Give my sister back or else we are going to war!''' + 
    '''\n Love, Princess ''' + fruit+ '''\n After mailing off the letter, she went to her room 
    and did her most favorite thing in the world.\n ''' + activity + 
    '''. \n She spent almost the whole rest of the night ''' + activity + 
    '''until she fell asleep, curled up next to all of her fruity friends.\n The ''' 
    + fruit_plural + '''snuggled on top of her chest and belly
    while the ''' + rival_fruit_plural + ''' cuddled her feet. \n The following morning, 
    she woke up to find her entire castle surrounded by ''' + veggie_plural + '''! \n
    She couldn't believe this! Her declaration of war had been turned against her. \n
    She had never expected Prince ''' + veggie + '''to attack her first! \n
    Even so, she put on a brave face, gathered everyone together, and went outside to the balcony.\n
    She could see the prince mounted atop a massive ''' + veggie + ''' beast, a sword in hand, \n
    ready to send his army to attack at any moment.\n
    'Where is my sister?!' she cried out, hands balled into angry fists. 'I demand to see her right now!'\n
    The prince just grinned, darkly. 'She's back home, doing ' ''' +  evil_activity + '''\n''' +
    '''Princess ''' + fruit + '''gasped in horror, covering her mouth for a moment in disgust. \n
    'You MONSTER!!! You know how much she HATES doing' ''' + activity + '''!!! \n
    Prince ''' + veggie + '''came closer, riding his beast. 'Surrender now, little girl. I've had my eye on \n
    this beautiful piece of land of yours for a while, now. Your letter gave me the perfect excuse to attack.'\n
    If you don't, not only will I end you and all your stupid ''' + fruit_plural + ''', but I will force your \n
    sister to do ''' + rival_activity + '''for the rest of her life! Stuck in the dungeon. What say you, child?\n'''
    + fruit + '''knew that her sister hated ''' + rival_activity + ''' even more than ''' + evil_activity + ''',\n
    but she had a trick up her sleeve. The same night she had sent off the letter to the prince, she had \n
    also sent one out to the ''' + junk + '''empire. Normally a very laid back people, but when put on \n
    the battlefield, they were the fiercest of warriors. \n 
    'NOW!!!!!' she shouted, stretching out her hand towards the sky.\n
    From the rooftops, thousands of ''' + junk + '''soldiers jumped down and began to completely decimate\n
    Prince ''' + veggie + ''''s army. They didn't even stand a chance against the sheer number of ''' + junk_plural + '.\n' + 
    '''Once the prince and his army were fallen, he laid on the ground and watched as Princess ''' + fruit + '\n' +
    ''' approached, pressing her foot onto his chest, trying to pin him down. She leaned forward, resting on her slightly\n
    bent leg, grinning down at the now mostly helpless prince. She reached into a pocket in her dress and pulled out a \n
    handful of photos. It was of the inside of the prince's secret room. Every visible surface of every \n
    wall and even the ceiling were covered in pictures of ''' + celebrity + '''. Even ones that were stitched\n 
     together with pictures of himself and big hearts draw all over. There were also kiss marks on several.\n ''' +
     ''' 'How did you get these???' the prince grabbed up the pictures, quickly hiding them and \n pressing them to his chest. ''' 
     + '''Princess ''' + fruit + '''just giggled, darkly. 'I have my ways. If you don't give my sister back,\n
     then I will make sure everyone in every kingdom on this entire continent knows your dirty little secret!\n
     That you're obsessed with' ''' + celebrity + ''' and love them far more than you could ever love my sister, ''' + rival_fruit + '\n' +
     '''. . . and so, that was the end. With the army defeated and the prince blackmailed,\n
      the only choice to be made was to release Princess ''' + rival_fruit + ''' back to her sister. \n At least for a little while . . . ''')

# end game 
exit = input ("THE END        (Press 'enter' to close window.)   \n  > ")

