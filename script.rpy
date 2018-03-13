# to do:
    # find better pics for dresi and kebaby
    # find out how to make buttons
    # try to find out how to fix the jump issue
    # arrange the tracks and loop the necessary ones
    # set up kanikuły
    # animate a shitty pic of Kacper
    # what should all świeżaki do? make a special cg show up?

##################################################################

define p = Character("[player_name]", color="#F39C12")
define b = Character("Babcia Halinka", color="#2A52BE")
define d = Character("Dziadek", color="#85C1E9")
define i = Character("Pani Irenka", color="#ADEC6E")
define ds = Character("Dres Seba", color="#00B732")
define k = Character("Ksiądz Przemek", color="#292929")
define kasa = Character("Kasjerka Andżelika", color="#FF0080")

transform leftish:
    xalign 0.37
    yalign 0.35
transform rightish:
    xalign 0.63
    yalign 0.35

default hajs = False
default targdone = False
default biedra = False
default jesus = False
default jp2 = False
default cola = False
default swiezak1 = False
default swiezak2 = False
default swiezak3 = False
default kebab = False

##################################################################

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
        
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false=[Hide('countdown'), Jump(timer_jump)]) 
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

##################################################################
# never ever put numbers in var names, blease :')
##################################################################

label start:
    play music 'wieś.mp3' 
    scene room1
    with Dissolve(.5)
    
    "It's a beautiful Sunday morning. You're at your {i}babcia{/i}'s house."
    "You wake up to the sunrays falling on your face from beneath white, lace curtains."
    "It's cozy and warm under the thick quilt decorated with floral patterns. {w}You don't really feel like getting up."
    
    "You're trying to remember anything from before you woke up from this nice sleep."

    $ player_name = renpy.input("What was your name again?...")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Mateuszek"
        
    p "Ah, right. It's [player_name]."
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    "Minutes pass before you hear someone call you."
    
    show babcia start at left
    with Dissolve(.5)
    
    b "Hello there darling!"
    b "I hope you slept well."
    b "You look thirsty!{w}\nWould you like some kompot, [player_name]?"
    
########## KOMPOT MENU ###########################################

    menu:

        "Yes please!":
            jump acceptkompot

        "No, thank you.":
            jump refusekompot
        
        "...what is this?":
            jump questionkompot
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    "You're left alone, sitting on bed, still hazed from a nice sleep."
    "What should you do?"
    
######## GET KOMPOT MENU #########################################
    
    menu:
        
        "Listen to your babcia and get ready for a meal.":
            jump gokitchen1
            
        "Examine the room.":
            jump theroom

##################################################################

    label gokitchen1:
        "You dress up swiftly, put on fuzzy slippers and walk over to your babcia."
        jump kitchen1
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
    label theroom:
        "You decide to get up and look around the room. {w}It strangely reminds you of communism."
        scene room2
        with fade
        "What do you want to do?"
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
        menu:
            "Check out the thing behind the couch; there's something green peeking out from behind of it.":
                jump discoverswiezak
                    
            "Walk over to your dziadek who's asleep in the rocking chair.":
                jump discoverdziadek
                
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
    label discoverswiezak:
        scene couchview
        with fade
        "It's a well-known Polish merchandise from Biedronka. {w}They sold a ton of them. {w}A literal ton. {w}{size=-5}Probably.{/size}"
        "Now that you've already found it, you walk around and see..."
        $ swiezak1 = True
    jump discoverdziadek
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
        
    label discoverdziadek:
        scene dziadekbg
        with fade
        "Your favourite {i}dziadek{/i}!"
        "He's snoring loudly. {w}Hopefully he's sleeping well."
        "It would be a shame if {i}someone{/i} was to interrupt him."
    $counter=0
    jump bothermenu
    
################# BOTHER MENU ####################################

    menu bothermenu:
        "Bother him a tiny bit. Just a little bit.":
            if counter < 9:
                $counter+=1
                jump bother
            else:
                jump secret
                
        "Leave the old man alone, he's surely tired.":
            jump kitchen1
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                
    label bother:
        "Nothing happened."
    jump bothermenu

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
        scene kitchen1
        with fade
        b "There you are, darling! {w}Sit down please, the food is getting cold!"
        "It's so lovely you have such a babcia."
        "You sit by the table and munch on some scrambled eggs she prepared for you beforehand."
        b "[player_name], do you think you could go to the targ and get me some fresh vegetables for dinner?"
        "It would be shameful to make your babcia run errands herself when you know she's old like that."
        "You nod your head and take a sip of kompot."
        b "I would need you to buy a kilo of potatoes and three onions."
        b "Irenka, my dear friend, should still be out there with her stall. {w}I think you'll find her easily. {w}If not, she will wave at you. I bet she remembers you!"
        "Babcia hands you 10 złoty and pats your hand vigorously. {w}As much as an old lady can, at least."
        "You finish your food quickly and help her wash the dishes, like a good grandchild would."
        b "See you [player_name]! Don't forget about the groceries!"
        jump walkout
        
##################################################################
        
    label walkout:
        show dom1
        with fade
        "It's a wonderful sunny day."
        "Everyone's obviously at church, besides the ones who are at the targ."
        "These people will probably go to the mass in the evening."
        "You look around the small village your babcia lives in and you notice three places you can go to..."
        "Where do you want to go to first?"
        
        menu walkoutmenu:
            "Go to the targ.":
                window hide Dissolve (.5)
                jump targ
            "Go next to the church.":
                window hide Dissolve (.5)
                jump church
            "Go to Biedronka.":
                window hide Dissolve (.5)
                jump biedronka
                
##################################################################

        label targ:
            $ targdone = True
            scene targ1
            with fade
            "There isn't a lot of people on the targ today."
            "Especially at this hour."
            scene targ5
            "You walk around looking for your babcia's friend. {w}You have no idea how are you supposed to find her, but... Yeah."
            scene targ7
            "Where might she be?"
            "You decide to walk around a little bit more and compare the prices of apples."
            scene targ2
            "Nope, it's not her."
            "{size=-5}Presumably.{/size}"
            "And the apples are pretty expensive, too."
            "Not like you need apples really."
            scene targ3
            "You've been walking around the endless targ for an hour now."
            "Still no sight of {i}Pani Irenka{/i} or cheap apples."
            "Your stomach starts grumbling silently at you."
            scene targ4
            "Finally, after another thirty minutes, you spot someone waving at you."
            "It must be Pani Irenka!"
            show irenka at leftish
            i "There you are!"
            i "Long time no see, kid!"
            "She flashes a smile at you and carries out a bag of potatoes and a couple onions."
            i "Your babcia told me you would come over and mentioned veggies so I assumed that's what she needed."
            "Wow, these babcias really do have some special sense."
            "You pick up the plastic bag and pay just the right amount."
            i "Say hi to Halinka from me!"
            scene targ1
            "This little nasty monster in your belly really growls at you now."
            "Which means you're pretty hungry."
            "Oh. {w}Oh!..."
            scene kebab1
            "There's a kebab, always when it's needed!"
            "Everyone loves kebaby."
            "If you don't love them... You're not a true Pole. {w}Sorry. {w}I don't make the rules."
            scene kebab2
            show janusz1 at leftish
            "The fellow Pole stares at you thoughtfully."
            "He speaks no words but you know what is on his mind."
            "You just know."
            "..."
            "He wants you to buy a kebab."
            "And you really are hungry, so maybe it's a good idea..."
            if hajs:
                menu:
                    "You deserve a good meal, right?":
                        jump kebabyes
                    "A tasty dinner probably awaits you at home. Don't get a kebab.":
                        jump kebabno
                    
                        label kebabyes:
                            $ kebab = True
                            show kebab at truecenter
                            "Janusz the kebab man hands you a kebab."
                            "His face doesn't change but you can feel he's content."
                            hide kebab
                            "Soon enough you feel full and satisfied."
                            jump dresi
                        
                        label kebabno:
                            "You deny the kebab."
                            "Janusz the kebab man starts to get angry."
                            hide janusz1
                            show janusz2 at leftish
                            "He shows you teeth and you can feel his fury growing."
                            "You decide to retreat the fastest you can before you experience the kebab wrath."
                            jump dresi
                            
            else:
                "Sadly, you find your pockets empty. {w}Just like your stomach."
                "That's too bad."
                show janusz2 at leftish
                "Janusz the kebab man grunts angrily. You quickly walk away. Better not have him jump to your eyes."
                jump dresi
                        
    label dresi:
        scene gangsta babcia
        show dres
        "Walking down the street you notice a couple dresi standing by."
        "You speed up significantly but they catch you anyway..."
        "They never give up."
        ds "What do you stand for?"
        ds "Legia Warszawa or Wisła Kraków?"
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'niewiem'
        show screen countdown
        menu:
            "Legia Warszawa!":
                hide screen countdown
                jump legia
            "Wisła Kraków!":
                hide screen countdown
                jump wisła
                
                label legia:
                    $ swiezak3 = True
                    ds "You're one of us!"
                    ds "Lucky you I'm in a good mood today."
                    ds "Have this before I change my mind."
                    show swiezak3 at truecenter
                    "He... {w}He hands you a świeżak."
                    "That did come unexpected."
                    hide swiezak3
                    with Dissolve (.5)
                    "You stutter out a thank you and go away quickly."
                jump walkout2
                
                label wisła:
                    ds "{i}Really?{/i}"
                    ds "You're dead, man."
                    ds "You'd better run."
                    "Maybe it does seem like a good idea to {i}run like hell before they beat you up all black and blue.{/i}"
                    scene dom1
                    "By the skin of your teeth you've escaped."
                    "Next time it would be useful to at least learn some sports teams..."
                jump walkout2
                
                label niewiem:
                    ds "Oh, you can't choose?"
                    ds "I'll choose for you."
                    "You decide to run away before he beats you up."
                jump walkout2
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
        label church:
            scene church1
            with fade
            "It's an old church that you vaguely remember from your childhood. {w}You probably used to go there every Sunday with your babcia and dziadek."
            "As you walk by, a man, clearly some kind of {i}ksiądz{/i}, approaches you with a smile."
            show ksiądz at leftish
            with Dissolve (.5)
            k "Hello! Hm... I think I remember your face, may you remind me who are you?..."
            "He truly looks like he's buried deep in thoughts."
            "You explain you're Babcia Halinka's grandchild. {w}The village's so small that he easily remembers who are you talking about."
            k "Ah, wonderful! The last time I saw you was years, years ago... You were still in diapers!"
            k "Children... They grow up so quick..."
            "You smile politely and explain you need to go on your small quest of getting veggies for dinner."
            "Ksiądz Przemek, however, suggests that you check out the church first."
            "As he says, it's been refreshed and looks much different on the inside."
            "Seems like he really wants to show it off to you. Maybe he was the one to design the interior?"
            hide ksiądz
            with Dissolve (.5)
            "You walk in and you're immediately stunned by what you see."
            scene church2
            with Dissolve (.5)
            "Beautiful columns..."
            scene church3
            with Dissolve (.5)
            "Wide naves..."
            scene church4
            with Dissolve (.5)
            "Colorful light shining through stained glass..."
            scene church1
            with Dissolve (.5)
            "The church you remember looked way different and way more modest."
            k "Feel free to walk around, the next mass won't start until thirty minutes from now."
            "After saying this, he seems to be thinking hard again."
            "He pulls out two paper cards out of his pocket."
            k "Right, I would like you to take this. Choose one!"
            
            ### button pics right here right here
            
            show jesus at leftish
            with Dissolve (.5)
            show jp2 at rightish
            with Dissolve (.5)
            "It's pictures of Jesus Christ and Pope John Paul II."
            "Which one will you choose?"
            
            menu picture:
                "Jesus Christ.":
                    jump jesus
                "Pope John Paul II.":
                    jump jp2
                    
           ### button pics ending rrright here
                                                            
                    label jesus:
                        hide jp2
                        with Dissolve (.5)
                        show jesus at truecenter
                        "You've obtained a picture!"
                        "Your babcia will surely love it."
                        $ jesus = True
                        jump walkout2
                            
                    label jp2:
                        hide jesus
                        with Dissolve (.5)
                        show jp2 at truecenter
                        "You've obtained a picture!"
                        "Your babcia will surely love it."
                        $ jp2 = True
                        jump walkout2
                        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                        
        label biedronka:
            $ biedra = True
            scene biedra1
            p "Here we are, the {i}best{/i} Polish store... Hah..."
            "You snicker to yourself."
            "No offense, you go to this store a lot. It's a fine one."
            "The essence of Poland, basically."
            "You approach it and gaze in awe. {w}Or... {w}No, not really."
            scene biedra2
            with Dissolve (.5)
            "The slide doors open in front of you, like gates to heaven. Sorta."
            scene biedra3
            with Dissolve (.5)
            "You think to yourself that maybe it's time to stop this attitude. Wow. How rude, right?"
            scene biedra4
            with Dissolve (.5)
            "The store isn't too big but it's got a lot of things all around."
            "You swiftly move among the aisles and wander around looking for veggies."
            "Out of sudden, a guy starts dancing wild moves right in front of the sweets aisle. {w}Weird music plays along from his tiny speaker, too."
            scene biedra5
            with Dissolve (.5)
            play music 'kanikuly.mp3'
            "What the {i}hell{/i}?"
            "You decide to quickly retreat from this wild man."
            scene biedra7
            with Dissolve (.5)
            "Walking down the aisles you finally spot the veggie stall."
            "Sure they're a bit more expensive than on the targ, but who cares?"
            "Veggies are veggies."
            "You grab just how much you need and walk past the beverages aisle."
            scene biedra6
            with Dissolve (.5)
            "Oh, here's some nice drink..."
            show cola1 at truecenter
            "You wonder if you should get some off brand cola or not."
            "A typical Polish kid thing."
            
            menu cola:
                "Take it.":
                    $ cola = True
                    jump colatrue
                "You have kompot at home, you don't need cola.":
                    hide cola1
                    with Dissolve (.5)
                    jump colafalse
                    
                    label colatrue:
                        "A nice cold drink won't hurt anyone, will it?"
                        "You take a bottle and head over to the {i}kasjerka{/i}."
                        hide cola1
                        with Dissolve (.5)
                        jump kasa
                         
                    label colafalse:
                        "Fizzy drinks? With phosphoric acid? You listened well at chemistry classes. {w}You won't fall for this sweet, carbonated trap."
                        "Not today, cola! Not today!"
                        "...moving on. {w}You head to the {i}kasjerka{/i} now."
                        jump kasa
            
            label kasa:
            scene biedra8
            "She looks pretty tired with life."
            "Moving your veggies slowly, she eventually gets it all done and prints out the receipt."
            if cola ==True:
                kasa "Oh, right."
                kasa "You paid enough to get a świeżak. Here you go."
                "She takes a świeżak out from behind the counter and puts it on the till."
                show swiezak2 at truecenter
                "Another one for you! {w}That's pretty cool, right?"
                hide swiezak2
                with Dissolve (.5)
                "Now that you've got all you need (and a new friend!...) you walk out of this {i}heavenly{/i} store."
                $ swiezak2 = True
            else:
                kasa "Thank you for shopping in Biedronka, or something."
                "You shrug and walk out with your groceries. {w}And a bottle of unhealthy fizzy drink."
            jump walkout2
                
##################################################################

        label walkout2:
            scene dom1
            with Dissolve (.5)
            "Where do you want to go now?"
            menu walkoutmenu2:
                "Go to the targ." if not (biedra or targdone):
                    pass
                    jump targ
                "Go next to the church." if not (jp2 or jesus):
                    pass
                    jump church
                "Go to Biedronka." if not (biedra or targdone):
                    pass
                    jump biedronka
                "Go home.":
                    jump kitchen2
                    
##################################################################
        
    label kitchen2:
        scene kitchen1
        with Dissolve (.5)
        b "Welcome back, darling! Is it hot outside?"
        b "I'm glad I didn't leave the house..."
        "You put the groceries on the table and sit down."
        "Babcia reaches for potatoes and onions, happy that you did what she asked for."

        if cola:
            "The veggies are now on the counter, ready to be peeled."
            "Babcia Halinka turns around to say something but her eyes stop on the bottle of cola you hold."
            "Her expression changes to something between disgust and disappointment."
            b "Do you really not like my kompot?"
            b "I thought you liked it, [player_name]."
            "You're a bit confused. Why would you buying cola mean you don't like her kompot?"
            "Maybe it's just that it's an unhealthy drink and she really wanted to take care of you."
            "You feel kinda ashamed and bummed."
            "Her expression is still sort of disappointed when she peels the potatoes."
            return
            
        elif biedra:
            "Her smile slowly degrades into a disgusted emotion."
            b "Did you go to the targ for sure like I asked you to?"
            menu:
                
                "Yes, I did!":
                    jump lie
                "Well...":
                    jump truth
            
                    label lie:
                        "You vigorously nod your head and say that you, in fact, went to the targ."
                        "Your babcia, however, picks an onion and smells it. It seems weird to you."
                        "Not until seconds later do you remember babcias have brilliant sense for spotting supermarket products."
                        "She can feel the difference."
                        "She knows you lied."
                        "You nasty, little {i}liar{/i}."
                    return
            
                    label truth:
                        "You feel a bit ashamed that you were too lazy to go to the targ."
                        "There's no point in trying to wiggle out of this lie, so you roll with speaking the truth."
                        "Babcia strangely knows you feel bad for having done that."
                        b "I'm disappointed that you didn't go for the fresh veggies, but for the ones sprayed with pesticides."
                        b "Listen, [player_name]. I love you either way, I really do, and I'm glad you told me the truth."
                        b "But please, next time listen to me, alright?"
                        "She smiles a little bit but you can tell she's still hurt."
                        "What's done is done. You can't fix the past."
                    return
    
        else:
            "The veggies are exactly what needed. She happily grates the potatoes and dices the onion."
            "What might she be cooking?..."
            "You watch her beat some pork into nice {i}kotlety schabowe{/i}."
            $ renpy.music.set_volume(volume=0.5, delay=0, channel='music')
            play music 'kormorany.mp3' fadein 10.0
            "The radio station she turned on now plays old Polish songs."
            "It's really enjoyable."
            "Feels like a good day."
            "Feels like a real summer day."
            "Babcia hums along to the songs and does a little dance sometimes."
            "Potatoes are in the pot now, kotlety are on the pan, frying."
            "There's one more pot - a big one. You know well what's there."
            "It's {i}rosół{/i}. You love it. It's truly a nostalgic dish. It's what you used to eat every Sunday at your grandparents'."
            "Now you don't visit them just as often, only occassionally. {w}You miss those times."
            "Seeing babcia smiling and happy fills your heart with warmth."
            $ renpy.music.set_volume(volume=0.25, delay=0, channel='music')
            "Time passes. Babcia snaps you out of your memories"
            b "Darling, can you lay out the cutlery? I'm almost done with cooking."
            "Soon enough, forks, knives and spoons shine on the table."
            "Long awaited, dinner is in front of you."
            if kebab:
                "However... You aren't much hungry anymore. Afterall, you've eaten a kebab..."
                "You stare at your plate instead of even sipping rosół."
                b "What's wrong, [player_name]?"
                b "You like rosół, I know you do."
                "You sigh and admit that you've eaten something before."
                "You just couldn't fight the temptation of getting a kebab."
                "Babcia looks a bit sad, maybe angry. You can't tell."
                "She's certainly not satisfied that you picked fastfood over a Polish meal."
                return
                
            else:
                "The aroma is wonderful. Carrots? Crunchy. Kotlet? Tender and delicious."
                "By the time you're done eating, you're sated. That's a good feeling, definitely."
                "You also get a cup of kompot again."
                "What a wonderful babcia you have."
                return
                    
