#Forewarning, my comments in the code are sometimes not cronological, also sometimes don't make sense but
#I do not wish to edit them since later I think I will like to go over and see if I can retrace my steps.

print '''So here is a little choose your own adventure tale that I have written. 
This is more just an exercise to practice programming for me so if the story is extraordinarily
cheesy well... it just is. Here are the rules. At various points in the story you will be able to choose various actions. The choices will 
affect your karma which will affect your likelihood of success at any action. You will rarely fail an action completely but there may
be a penalty based off of a mix of randomness and your karma score. Any good or evil action will immediately change your karma score by 1
in the direction of the morality of the choice. If you get too far in any direction choosing a neutral action two times in a row will
move your karma by one point back to the center. Your base rate of success will be 1/2. I do realize that this sounds a little harsh
but once you get your character going the bonuses will hopefully work out.

  The actions will fall into one of three categories good, bad, or neutral.
There will occasionally be more than just three actions in which case one of them is the best action and if you get the best action you will get
a charm. Using the charm will automatically pass the action with no penalty and please do keep in mind that this is coming from my own warped head
so it will behoove you to think what I personally would think is the best answer.
The second use of the charm will be at any point you may consume a charm for a single point of life.
Occasionally there will be times when it is good to be bad
and bad to be good. Once again you will most likely be able to pass the action but there will be an increased chance of penalty and the penalty 
itself may be more severe if your character is aligned to the opposite side.

 The max karma score that you will be able to attain will be plus minus 5 points from your original starting point of 5.
The Karma score will put you into one of five categories. If your karma is 4-6 you will be neutral. Pretty simple in this category there will be
no bonus or penalty to any action. If your Karma is 1-3 you will be considered "Evil". You will gain + 1 chance to succeed at evil actions
but will get a -1 penalty to all good actions. If your karma gets to 0 you will be considered to be "Super Evil" you will get plus 2 to all evil
action success but will get a -3 to chance of choosing a good action. The same applies in reverse to the good side where 7-9 will be a "Good"
character and 10 will be a "Super Good" character which seems like a very good thing but there will be times when the evil action will be the
"correct" response and you will incur the same amount of penalty for success as the "Super Evil" character.

Oh one more thing, if your life gets to 0 you are dead and the story is over. You will be allowed to go back to a checkpoint to see if you can
make some more advantageous choices. '''


stats = { 'life' : 10 , 'karma' : 5 , 'charms' : 0 }

print stats

print " Welcome to Virtue Obscured "

print """     You awaken to a beam of light hitting your face. Last night was one heck of a party your family probaly just let you sleep in. It was
after all the last time that you would be able to spend time with your brother before he headded off to the Elven Wizard Academy so a little self inflicted
illness would be likely to be forgiven by your family. You notice as you rub your eyes that you have a good bit of a headache and are feeling a
little queasy but not so bad that you think you will have to remain in bed any longer. As you stand up you realize that you may even still
be feeling the effects of the let me see, one, two,.... six,.... well at least 6 pints of mead last night that you can account for. Perhaps it
would be a good idea to try to whip up a potion for yourself so that you might be a little more together to wish your brother off to the academy.
You could go with the classic recipie for elven rejuvenation. It certainly has little chance of anything going wrong and despite its modest effects has
been an elf favorite for minor ills of all kinds for centuries. There was also the possibility that you could try one of the recipies that your brother had
recently showed you. He did mention that he had recently been dabbling into the dark arts and had shown you a recipie for a potion that would greatly increase
your stregnth but he also did mention that he had nearly scorched the tips of his ears off twice before he was able to make it without folly. Or you
could simply try one of natures oldest refreshers and simply drink a large glass of water and allow time to do the rest. Do you....
A) Make traditional Elf potion?
B) Make dark Elf potion?
C) Drink a glass of water? """
print stats

choose = raw_input(" I think I will go with: " )

from random import randint

#To start off to make things simple I decided to go with a 50/50 chance of succes since any more or less in any direction seemed to unbalance the numbers
#even before testing. The good action below is based off of the karma stat and measures your pure chance of success. So even though the title is good action
#I do think that this function should cover all of the success/fail scenarios(hopefully)...(5 mins later)  Turns out that won't work out but I think if I just reverse the
# less than commands to greater than that should reverse the flow for the "evil" actions. (1 week later) Turns out that is also incorrect but I think that I am
#unfucking this properly now.

#Also I think that the if then another if statement could be replaced with an and statement but its working so I will leave it that way for this project.

def good_action():
    success = randint(1, 10)
    if stats['karma'] < 10:
        stats['karma'] += 1
#had to put this karma modifier before results of action due to return stopping any more code from running. May be a flaw but minor and overlookable for the moment.
    if stats['karma'] < 1:
        if success < 9:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 4:
        if success < 7:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 7:
        if success < 6:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 10:
        if success < 5:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
#Had to review function to catch that I had not included the bonus for supergood. Realized this when reviewing to see if I could put this function into a class.
    elif stats['karma'] == 10:
        if success < 4:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
        
    
#some other minor flaws in karma system found. stats['karma'] was originally > to start for evil action per my just reverse everything idea
#but that would prevent rest of function from operating as once your number is over 1
#it would automatically return a value and stop running.
def evil_action():
    success = randint(1, 10)
    if stats['karma'] > 0:
        stats['karma'] -= 1
    if stats['karma'] < 1:
        if success > 7:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 4:
        if success > 6:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 7:
        if success > 5:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] < 10:
        if success > 4:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
    elif stats['karma'] == 10:
        if success > 2:
            print "FAILURE"
            return False
        else:
            print "SUCCESS"
            return True
            
            

count = 0

def neutral_action():
    global count
    
    success = randint(1, 10)
    
    count += 1
    if count == 2 and stats['karma'] < 5:
        stats['karma'] += 1
    elif count == 2 and stats['karma'] > 5:
        stats['karma'] -= 1

    if count == 2:
        count -= 2
        
    if success < 6:
        print "SUCCESS"
        return True
    else:
        print "FAILURE"
        return False

#testdic = {'life': 3}

            
#good_action()
#evil_action()

#neutral_action()


#if good_action == "FAILURE":
#    testdic['life'] += 1
#else:
    #testdic['life'] -= 1

#print testdic

if choose == 'a' or choose == 'A':
    new_var = good_action()
    if new_var == True:
        print """With just a few simple herbs and an eye of newt you whip up a new vial of remedy and drink it immediately to soothe your
            aching head. You start to feel a bit rejuvenated already. You take a quick bath and dry off then quickly jump into your tunic and
            start to head downstairs. """
        stats['life'] += 1
    elif new_var == False:
        print """Hmm thats strange, this spell has never failed me before. "Maybe I had let the eye of newt spoil." You think to yourself.
Well in any case you are no worse off for it not working. You still look a little rough and your head still hurts but you have survived many
mornings like this before. You decide to skip bathing and quickly throw on the same tunic that you had on last night and start to head downstairs."""

elif choose == 'b' or choose == 'B':
    evil = evil_action()
    if evil == True:
        print """You go to the little drawer under your chest where you hide some of the dark herbs that your brother had showed you how to find.
You are almost an adult and soon will be capable of making your own decisions and even live on your own but your are not there just yet and
your parents would not be pleased with you keeping such things in the house. You collect and grind the herbs in a small bowl then mix in the water
but nothing happens. "What am I forgetting?" You think as you see your family cat jump up onto the bed. It jogs your memory that the potion requires
a drop of blood from a... well something living. "Here Max this will only sting for a second." But perhaps your cat is capable of senseing your dark
purpose in mind, he hisses and then scratches you on the hand then boldts down the stairs. Well at least now your dilema for how to get a drop of blood
has been solved. You squeeze a drop onto the mixture which then starts to emanate just a little bit of a red glow. You drink it down and you
feel a surge of stregnth come over you. You can feel some new life running through you but it does seem a bit tainted by some unseemly power.
You can see why your parents might disapprove of such things. In any case no time to worry now. You get ready with extra speed at everything including
taking a shower and pressing one of your better tunics to see your brother off. You then start to head downstairs."""
        stats['life'] += 2
    elif evil == False:
        print """You go to the little drawer under your chest where you hide some of the dark herbs that your brother had showed you how to find.
You are almost an adult and soon will be capable of making your own decisions and even live on your own but your are not there just yet and
your parents would not be pleased with you keeping such things in the house. You collect and grind the herbs in a small bowl then mix in the water
but nothing happens. "What am I forgetting?" You think as you see your family cat jump up onto the bed. It jogs your memory that the potion requires
a drop of blood from a... well something living. "Here Max this will only sting for a second." But perhaps your cat is capable of senseing your dark
purpose in mind, he hisses and then scratches you on the hand then boldts down the stairs. Well at least now your dilema for how to get a drop of blood
has been solved. You squeeze a drop into the mix and it quickly begins to boil. Then it begins to boil over. You reach for it to try to get it to the window
when it erupts with a loud "BANG". Your head is engulfed in a mixture of whatever herbs you used, a little blood, and just a little bit of fire. You grab
a towel and try to wipe the mixture off of your face. You can't quite get it all off and are a little confused as to why somebody had not come up
to see what all this racket is. You throw on your tunic and start to head downstairs and hope that by some miracle the noise was not as loud as you thought."""
        stats['life'] -= 1

elif choose == 'c' or choose == 'C':
    print ''' It is far too early to be fooling around with sorcery. Best to just let nature run its course. You do feel a little better after a large glass
        of water but know that it will be some time before you are really feeling back to your normal self. You do however feel refreshed enough to take
        a rather fast bath and to put on a fresh tunic so that you at least look somewhat decent to see your brother off on this both sad and exciting day. You
        You start to head down the stairs to see who is all up and how much time you have left before he actually has to leave.'''

else:
    print "That is definitely not an option."

print """ As you are headding down the stairs you notice that something is very strange. There is not a sound in the whole house. "Perhaps they are just
quietly discussing over breakfast what the Academy will be like for Azriel." You think to yourself. But when you open the door to downstairs you don't see
anybody at all. To the left you see the quaint little kitchen that you, your mom and dad, and your brother shared countless meals in. But there was nobody
sitting at the little round table with its little stools. The small black stove in the back of the room looked like it had not been used at all that day. There
were dishes on the table but there wasn't a single hint that anybody had used them or that there was soon to be food to use them.
    You quickly take a few stepsinto the living room to see if anybody is there. There are just a few embers left in the fireplace but other than that the
    room looked perfectly in order as
though nobody had used it in days. "Oh no! I hope I didn't miss seeing my brother off!"  Even though your family would try to understand you know that they
as well as your brother would be terribly disappointed. This was a very big day for him and if you missed your last chance to see him it would be till spring
that you would be able to see him again. You try not to think of the looks on everybody's faces as you stroll up having missed his departure. You run to the door
and swing it open only to feel the sharpest chill as you ran out into a fog that was cold as ice.

You stumble a bit as you take a couple steps out the door and
realize that you can only see for a few feet in front of you. It seems as though it is the dead of winter by the chill but it is just the beginning of fall.
"Well if they aren't here where could everybody possibly have gone too in this dreadful weather." You think to yourself. As you are peering into the fog in an
attemt to see anybody or anything that might be around you notice something dark and shadowy moving not too far in the distance. After a second it seems to fade
back into the mist but then seems to reappear a little closer but off to the left a bit. It then fades away but then reappears even closer but off to the right
a little bit. It is clear at this point that whatever it is, is coming towards you. It seems quite threatening but perhaps your eyes are just playing tricks on
you and it is a family member trying to figure out what is going on. You do feel it is rather ominous but attacking immediately seems a bit hasty. You could try
to cast a light spell to see if you could get a better look but it is approaching fast. You could just hold still and hope that whatever it is hasn't actually
seen you yet and might just go away. Or you could simply head back inside before whatever it is approaches, despite the jokes your brother would crack at you for
fleeing at the first sight of a shadow if it is him.
Do You
A) Attack!!! Best defense is a good offense...
B) Use your light magic.
C) Stand Very Still.
D) Go back insidel. (Run Away!!!)"""

#started writing a function for the multiple selections. Decided to try to work this into a class..... Trying to
#figure out if this is even necessary or if this will just make it needlessly more complex
##def choices():
##    print choose
##    if choose == 'a' or choose == 'A':
##        evil = evil_action()
##        if evil == True:
##            print evil_success
##        else:
##            print evil_failure
##            
##    elif choose == 'b' or choose == 'B':
##        good = good_action()
##        if good == True:
##            print good_success
##        else:
##            print good_failure

#Well so far I have at least been able to make the story function. However I do think that I need to
#make a class  so that I do not need to even recall the choose variable and copy paste the outcome
#functions every time.

#the variables below are just place holders for text than I plan to write later... (sometime later) the text is now filled in, just figured I can reassign these variables to any other diffferent text later in the
#program so I can fill out all the choices in full now. Now I am just trying to figure out how to recall the choices class so that i can have the reader choose another course of action after the text.
evil_success ='''Well this fog is just downright unsettling and you do not want some evil creature to get the drop on you. You charge at the shadowy thing that is coming at you while reaching for your sword.
You realize only after you have started charging that you had not gotten any of your weapons in your haste to see who all was up and if your brother was still here. As you close in on the creature you see a
mass of tentacles and other unseemly goo where a humans body might be. You pummel the goo right at the middle as attacking the tentacles would be an impossible task. You get in a few good blows and
the creature is stunned for a moment but then it seems to recover and the  tentacles start to mount some sort of counter attack and they manage to get a few good swipes in as they swing about wildly.
You shove the monster to the ground with a forceful heave. The thing starts to get up quickly however and does not appear to have taken any permanent damage. Perhaps it would have been a good idea
to figure out what is going on before rushing into battle.'''



evil_failure = '''You are not going to be intimidated by some sort of squiqqly whatever even if there is an strange and evil fog all around you. Unfortunately you are still hungover at best from last nights
celebration. You lunge at the monster only to realize that your sword is still inside since you were in such a rush to make sure that you hadn't missed your brother. You swing about clumsily as you close in
on what appears to be mostly a mass of tentacles. Your shots are ill timed and poorly aimed. You just barely manage to hit the thing once and knock it back a bit as you are getting pummeled with
slippery black tentacles. You have just a moment before this thing will obviously begin its assault again.'''

good_success = '''You reach into your pocket and luckily still have the crystal that  your brother gave to you last night. You skillfully recite the spell to make the crystal blaze forth with a firey bright light.
As it illuminates the area the creature reels back being bathed in the brightness. Perhaps there is a reason this thing is skulking about in an unnatural fog. You are able to discern about 5 black tentacles
on either side of the thing, two of which are larger and seem to have taken the place of legs, a few on either side of it and one slightly larger one on the top in the middle which may be its head. Even bathed
in light the thing is still a slimy jet black and while the tentacles are distinguishable as the appendages, it is difficult to discern where the tentacles end and the body begins. Perhaps the thing is almost
entirely tentacle. In any case the thing appears to have been stunned for the moment but the tentacles are now starting to wave back and forth faster and faster. It looks like it may be powering up for
some sort of attack.'''
good_failure = '''You decide to try to cast some light on the situation but you are not feeling your best and you fumble about in your pockets looking for the crystal to cast the light spell. All the while the
thing is closing in. You try a few times to remember the words to the light spell but finnaly are able to complete it. However as you begin to thrust the crystal into the air the mysterious blob has closed to
combat range and is able to get in a good swipe with one of its sickly black tentacles. You do however get the light spell in full swing but not before you take some damage. Once the spell is fully powered
up the creature does reel back in apparent disgust. You can make out that this thing is comprised of sickly black tentacles and almost nothing else if indeed anything else at all. The thing is momentarily
pacified but it then begins to wriggle around again waving its slippery limbs faster and faster.'''
neutral_success = '''You decide to freeze  in the hopes that the thing will not notice you. You are able to freeze to perfection but the thing is still advancing although not as fast as before. It seems to
be trying to find you. It begins to swing a something here and there in the mist although it is hard to tell even what it is swinging. Perhaps it is swinging some sort of weapon but who knows. In this state
it is hard to tell anything for sure. You are contemplating your next move when one of the swings hits you squarely in the shoulder knocking you to the ground. It then begins to swing wildly where you were
once standing. You very slowly stand back up as the creature is still attemping to find you with one of its wild attacks.'''
neutral_failure = '''You try to stand still to avoid detection by the creature but you slip on a stone below you. You do not fall over but you do make enough noise to attract the attention of the shadowy whatever
and it is closing on you fast. You try to take a few steps back but the creature swings wildly at you and manages to hit you a couple times pretty squarely. After it hits you, you are able to take a step to the
side to get out of range of the creature and it continues to swing wildly where you once were. This may be a temporary solution but you clearly must come up with some sort of other plan or it will find
you again.'''
charm_answer = '''Something is obviously terribly wrong at this point. Your whole family is gone and now there is some ominous mystery lurking in what is clearly some sort of unnatural mist. This is no time
for heroics you need to gather yourself and see if you can find some more information as to just what the heck is going on. You go right back inside without delay. As you close the door begind you, you hear a
loud "THUD!!!" as whatever that thing was throws itself against the door. Some sort of evil magic is at work here it is time to get to the bottom of this!'''

class action(object):
    def __init__(self, parameters):
        self.parameters = parameters
    def choices(self):
        choose = raw_input(" I think I will go with: " )
        choose
        if choose == 'a' or choose == 'A':
            evil = evil_action()
            if evil == True:
                print evil_success
                return 'evil success'
            else:
                print evil_failure
                return 'evil failure'
                
        elif choose == 'b' or choose == 'B':
            good = good_action()
            if good == True:
                print good_success
                return 'good success'
            else:
                print  good_failure
                return 'good failure'
        elif choose == 'c' or choose == 'C':
            neutral = neutral_action()
            if neutral == True:
                print neutral_success
                return 'neutral success'
            else:
                print neutral_failure
                return 'neutral failure'
        elif choose == 'd' or choose == 'D':
            print charm_answer
            return 'charm answer'
            
first_class_ever = action(1)
print stats
for x in range(10):
    store = first_class_ever.choices()
    print stats
    if store == 'evil success':
        stats['life'] -= 2
    elif store == 'evil failure':
        stats['life'] -= 3
    elif store == 'good success':
        stats['life'] += 1
    elif store == 'good failure':
        stats['life'] -= 1
    elif store == 'neutral success':
        stats['life'] -= 1
    elif store == 'neutral failure':
        stats['life'] -= 2
    elif store == 'charm answer':
        stats['charms'] += 1
        break
    print stats
    print 'After your truly wise (or possibly truly stupid) choices your new attributes are as follows...' 


print stats


#Just a little testing here but I do want to leave all of the little tid bits even of things I do not use so that if I ever
#do want to come back and see how I got to the final product that my testing and mental processes in general
#are intact.
#class test(object):
    #def __init__(self, at1, at2, at3):
##        self.at1 = at1
##        self.at2 = at2
##        self.at3 = at3
##
##        self.at1 = []
##        self.at2 = {dictionary:1}
##        self.at3 = 3

print ''' You take a step back from the door and start calling the names of your family... "Mother!!! Father!!!..... Azriel?!?!...." but nobody answers. There is
only total silence and the sound of your heart beating in your chest for while your physical exertion is over, all you know ath this moment is panic. You run
upstairs and start searching from room to room, knocking over tables, looking under the beds, even checking all of the closets, but all you see is their clothes
and other items with nothing to indicate that anything is even remotely wrong other than their abscence. You go from room to room ransacking all of the
beds and all of the closets hoping that they are hiding hoping that you have been the victim of some horrible prank but wind up with nothing other than
an incredibly messy house. In exasperation you sit on the couch and decide what to do next. You lay down and try to close your eyes to think for a minute but
your eyes fall directly into a ray of sun coming through the window making it impossible to even think. "SUN?!?!" Was it over? Did the fog lift? You look out the
window to see if you can catch any glimpse of receeding fog but all you see is the most beautiful sunny day outside. You think to yourself "Oh thank goodness
now I can search the village to find my family. Maybe last nights celebration was a little wilder than I thought and I am imagining things... everything looks fine.
But then off in the distance behind one of the cottages you spot what you think is a hint of that slimy blackness. You open the window to see if you can spot it clearly but as soon
as you do thick dense fog begins rolling in the window. You hear something moving around in the mist and quickly close the window only to see the same sunny
day through the glass. Just as a test you decide to open the window just a bit to see what happens. Surely enough the sunny day is clear enough to see
through the window but the fog is still pouring in throug the open crack in the window. Then you see the slimy black creature come out from behind your
neighboors house and quickly start moving your way. You can make it out fairly clearly without the fog all around it but there is not much to clearly see, just
a mass of black tentacles, two of which appear to be serving as legs, one in the middle which may be some sort of head and various arms. It is purely dark
and in the sun you can see that it is leaving a little trail of sllime behind it. You think of giving it a closer look but it seems to be aware of your existence at this
moment and is closing fast. You close the window quickly with a little thud but then you look out the window again and the thing is nowhere to be found.
You wonder what sort of evil sorcery this is and if the fog is some sort of evil spell or is the bright sunny day the magical trick and the fog is real. After much
racking your brain, pacing,  and attempting to come up with some sort of plan you throw a plate across the room which shatters as it hits the wall. The
force of the plate causes the cellar door to open just a crack. "Oh god I hope they are not down there." Nonetheless you know that you have to go down there
to check. But first you stop at your room and grab your sword. Best be prepared just in case something else bad happens on this increasingly strange day.
With your sword attached firmly to your belt you do feel a little more at ease. At least some monster won't catch you hungover and unprepared.

Your sense of self confidence is quickly emaciated when you open the door to the cellar. There is no monster there but then again neither is anything that
you expected to be there either. As a matter of fact there is just a narrow set of stone stairs that only appears to go down for a while but then drops off into
pitch blackness. ".....gulp.....". While you do not relish the thought of investigating this any farther your only other options are to go outside and fight some
unknown monster, or wait around and hope that both whatever is out there doesn't get in and that there is nothing else in the basement that might just be
resting a bit after murdering your family and will soon be back to finish the job once it figures out that you are up there.

Smashing a stool for a handle and
wrapping that in some scraps of cloth that you cut off one of your older tunics makes a decent enough torch for now. You begin to step slowly down the stairs
and you realize that the stairs do not drop off but take a right turn at where you previously thought was the end. They then go down about the same amount
then turn right again. It seems as if there is no floor and no ceiling either. Just this old narrow set of stairs going down to...wherever. After about three or
four more turns you see something larger at the end of one of the flights of stairs.'''
        
    
            
            






