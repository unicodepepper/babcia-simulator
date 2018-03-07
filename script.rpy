define p = Character("[player_name]", color="#F39C12")
define b = Character("Babcia", color="#2A52BE")
define d = Character("Dziadek", color="#85C1E9")
define k = Character("Ksiądz Przemek", color="#292929")
define kasa = Character("Kasjerka Andżelika", color="#FF0080")
default hajs = False
default jesus = False
default jp2 = False
default swiezak1 = False
default swiezak2 = False

##################################################################
# never ever put numbers in var names, blease :')
##################################################################

label start:
 
    scene bg 1
    
    "It's a beautiful Sunday morning. You're at your {i}babcia{/i}'s house."
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
        "It's a well-known Polish merchandise from Biedronka. {w}They sold a ton of them. {w}A literal ton. {w}{size=12}Probably.{/size}"
        "Now that you've already found it, you walk around and see..."
        $ swiezak1 = True
    jump discoverdziadek
        
    label discoverdziadek:
        "Your favourite {i}dziadek{/i}!"
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
        jump walkout
        
##################################################################
        
    label walkout:
        "It's a wonderful sunny day."
        "Everyone's obviously at church, besides the ones who are at the targ."
        "These people will probably go to the mass in the evening."
        "You look around the small village your babcia lives in and you notice three places you can go to..."
        "Where do you want to go to first?"
        
        menu walkoutmenu:
            "Go to the targ.":
                jump targ
            "Go next to the church.":
                jump church
            "Go to Biedronka.":
                jump biedronka
                
##################################################################

        label targ:
        # ay lmao come up with something you idiot
        
        jump walkout2
        
        
        label church:
                # church from afar pic
            "It's an old church that you vaguely remember from your childhood. {w}You probably used to go there every Sunday with your babcia and dziadek."
            "As you walk by, a man, clearly some kind of {i}ksiądz{/i}, approaches you with a smile."
                # show ksiądz as well, to the left
            k "Hello! Hm... I think I remember your face, may you remind me who are you?..."
            "He truly looks like he's buried deep in thoughts."
            "You explain you're Babcia Halinka's grandchild. {w}The village's so small that he easily remembers who are you talking about."
            k "Ah, wonderful! The last time I saw you was years, years ago... You were still in diapers!"
            k "Children... They grow up so quick..."
            "You smile politely and explain you need to go on your small quest of getting veggies for dinner."
            "Ksiądz Przemek, however, suggests that you check out the church first."
            "As he says, it's been refreshed and looks much different on the inside."
            "Seems like he really wants to show it off to you. Maybe he was the one to design the interior?"
                # church on the inside
            "You walk in and you're immediately stunned by what you see."
                # column pic
            "Beautiful columns..."
                # some kinda center pic
            "Wide naves..."
                # a close up on witraże?
            "Colorful light shining through stained glass..."
                # back to the first inside pic
            "The church you remember looked way different and way more modest."
            k "Feel free to walk around, the next mass won't start until thirty minutes from now."
            "After saying this, he seems to be thinking hard again."
            "He pulls out two paper cards out of his pocket."
            k "Right, I would like you to take this. Choose one!"
            "It's pictures of Jesus Christ and Pope John Paul II."
            "Which one will you choose?"
            menu picture:
                "Jesus Christ.":
                    jump jesus
                "Pope John Paul II.":
                    jump jp2
                                                            
                    label jesus:
                            # a pic of jesus
                        "You've obtained a picture!"
                        "Your babcia will surely love it."
                        $ jesus = True
                        jump walkout2
                            
                    label jp2:
                            # a pic of jp2
                        "You've obtained a picture!"
                        "Your babcia will surely love it."
                        $ jp2 = True
                        jump walkout2
                        
                        
                        
        label biedronka:
                # a pic of biedra from the outside
            p "Here we are, the {i}best{/i} Polish store... Hah..."
            "You snicker to yourself."
            "No offense, you go to this store a lot. It's a fine one."
            "The essence of Poland, basically."
            "You approach it and gaze in awe.{w}Or... {w}No, not really."
            "The slide doors open in front of you, like gates to heaven. Sorta."
            "You think to yourself that maybe it's time to stop this attitude. Wow. How rude, right?"
                # here should go a pic of biedra aisles
            "The store isn't too big but it's got a lot of things all around."
            "You swiftly move among the aisles and wander around looking for veggies."
            "Out of sudden, a guy starts dancing wild moves right in front of the sweets aisle. {w}Weird music plays along from his tiny speaker, too."
                # here kanikuły start playing and kacper shows up
            "What the {i}hell{/i}?"
            "You decide to quickly retreat from this wild man."
                # music and kacper are g o n e
                # aisles turn to veggies
            "Walking down the aisles you finally spot the veggie stall."
            "Sure they're a bit more expensive than on the targ, but who cares?"
            "Veggies are veggies."
            
            
            "You grab just how much you need and walk to the {i}kasjerka{/i}."
            "She looks pretty tired with life."
            "Moving your veggies slowly, she eventually gets it all done and prints out the receipt."
            kasa "Oh, right."
            kasa "You paid enough to get a świeżak. Here you go."
            "She takes a świeżak out from behind the counter and puts it on the till."
            "Another one for you! {w}That's pretty cool, right?"
                
##################################################################

        label walkout2:
            "Where do you want to go now?"
            menu walkoutmenu2:
                "Go to the targ.":
                    jump targ
                "Go next to the church." if not jp2 and jesus:
                    jump church
                "Go to Biedronka.":
                    jump biedronka
