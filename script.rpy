define b = Character("Babcia", color="#2A52BE")
define d = Character("Dziadek", color="#85C1E9")
define p = Character("[player_name]", color="#F39C12")
default hajs = False
default swiezak1 = False
default swiezak2 = False

##################################################################
# never ever put numbers in var names, blease :')
##################################################################

label start:
 
    scene bg 1
    
    "It's a beautiful Sunday morning."
    "You wake up to the sunrays falling on your face from beneath white, lace curtains."
    "It's cozy and warm under the thick quilt decorated with floral patterns. {w}You don't really feel like getting up."
    
    "You're trying to remember anything from before you woke up from this nice sleep."

    $ player_name = renpy.input("What was your name again?...")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Mateuszek"
        
    p "Ah, right. It's [player_name]."
    
##################################################################
    
    "Minutes pass before you hear someone call you."
    
    show babcia start at left
    
    b "Hello there darling!"
    b "I hope you slept well."
    b "You look thirsty!{w}\nWould you like some kompot, [player_name]?"
    
########## kompot menu ###########################################

    menu:

        "Yes please!":
            jump acceptkompot

        "No, thank you.":
            jump refusekompot
        
        "...what is this?":
            jump questionkompot
            
##################################################################

    label acceptkompot:
        b "There you go darling! {w}I made it just for you."
        b "It's got strawberries right from my garden."
        jump getkompot

    label refusekompot:
        b "But sweetie, you should drink healthy drinks. {w}Not just this... {w}How do you call it..."
        "You suggest that the word she's looking for is cola."
        b "...yes, exactly."
        b "But as long as you're here, you'll be all healthy under my wings."
        jump acceptkompot
        jump getkompot
        
    label questionkompot:
        b "My little sweet bear cub, you couldn't have possibly forgotten the taste of your childhood!"
        b "Here you go, enjoy this summer drink."
        jump getkompot
        
##################################################################

    label getkompot:
    
    hide babcia start
    show kompocik 1 at truecenter
    
    "You take the glass and drink the fruity beverage. {w}It's fairly sweet and reminds you of the good old times when you were a kid."
    
    show babcia start at left
    
    b "Now, [player_name], get up while I prepare breakfast for you."
    "She pinches your cheek belovingly before retreating to the kitchen."
    
    hide babcia start
    with dissolve
    hide kompocik 1
    with dissolve

##################################################################

    "You're left alone, sitting on bed, still hazed from a nice sleep."
    "What should you do?"
    
######## get kompot menu #########################################
    
    menu:
        
        "Listen to your babcia and get ready for a meal.":
            jump gokitchen1
            
        "Examine the room.":
            jump theroom

##################################################################

    label gokitchen1:
        "You dress up swiftly, put on fuzzy slippers and walk over to your babcia."
        jump kitchen1
        
    label theroom:
        "You decide to get up and look around the room. {w}It strangely reminds you of communism."
        "What do you want to do?"
        
        menu:
            "Check out the thing behind the couch; there's something green peeking out from behind of it.":
                jump discoverswiezak
                    
            "Walk over to your dziadek who's asleep in the rocking chair.":
                jump discoverdziadek
        
    label discoverswiezak:
        "It's a well-known Polish merchandise from Biedronka. {w}They sold a ton of them. {w}A literal ton. {w}{size=9}Probably.{/size}"
        "Now that you've already found it, you walk around and see..."
        $ swiezak1 = True
    jump discoverdziadek
        
    label discoverdziadek:
        "Your favourite grandpa!"
        "He's snoring loudly. {w}Hopefully he's sleeping well."
        "It would be a shame if {i}someone{/i} was to interrupt him."
    $counter=0
    jump bothermenu
    
################# bother menu ####################################

    menu bothermenu:
        "Bother him a tiny bit. Just a little bit.":
            if counter < 9:
                $counter+=1
                jump bother
            else:

                jump secret
                
        "Leave the old man alone, he's surely tired.":
            jump kitchen1
                
    label bother:
        "Nothing happened."
    jump bothermenu

    label secret:
        "Oh no... He's awoken."
        d "Huh??"
        d "What's going on? I-"
        "He glances all over, visibly scared, before his eyes stop on your face."
        d "Oh. {w}Oh... {w}It's just you."
        d "You gave me a good scare, kiddo! {w}\nDon't do this again..."
        d "Have this and leave me alone."
        "Dziadek reaches over to his pocket to take out 5 złoty. {w}He passes it over to you and sits comfortably in his rocking chair again."
        "You suppose it's high time you went to see your babcia in the kitchen."
        $ hajs = True
    jump kitchen1
    
##################################################################
        
    label kitchen1:
        b "There you are, darling! {w}Sit down please, the food is getting cold!"
        "It's so lovely you have such a babcia."
        "You sit by the table and munch on some scrambled eggs she prepared for you beforehand."
        b "[player_name], do you think you could go to the targ and get me some fresh vegetables for dinner?"
        "It would be shameful to make your babcia run errands herself when you know she's old like that."
        "You nod your head and take a sip of kompot."
        b "I would need you to buy a kilo of potatoes and three onions."
        b "Helenka, my dear friend, should still be out there with her stall. {w}I think you'll find her easily. {w}If not, she will wave at you. I bet she remembers you!"
        "Babcia hands you 10 złoty and pats your hand vigorously. {w}As much as an old lady can, at least."
        "You finish your food quickly and help her wash the dishes, like a good grandchild would."
        b "See you [player_name]! Don't forget about the groceries!"
        if hajs ==True:
            jump walkout
        
##################################################################
        
    label walkout
        "It's a wonderful sunny day."
        "Everyone's obviously at church, besides the ones who are at the targ."
        "These people will probably go to the mass in the evening."
        "You look around the small village your babcia lives in and you notice three places you can go to..."
        "Where do you want to go to first?"
        menu walkout:
            "Go to the targ.":
                jump targ
            "Go next to the church.":
                jump church
            "Go to Biedronka.":
                jump biedronka
                
##################################################################

        label targ:
            # ay lmao come up with something you idiot
        label church:
            




            "yaaay"
        else:
            "naaay"
#        b "[player_name], do you think you could go to targ and get me some fresh vegetables for dinner?"
 #       "It would be shameful to make your babcia run errands herself when you know she's old like that."
  #      "You nod your head and take a sip of kompot."
   #     b "I would need you to buy a kilo of potatoes and three onions."
    #    b "Helenka, my dear friend, should still be out there with her stall. {w}I think you'll find her easily. {w}If not, she will wave at you. I bet she remembers you!"
     #   "Babcia hands you 10 złoty and pats your hand vigorously. {w}As much as an old lady can, at least."
 
