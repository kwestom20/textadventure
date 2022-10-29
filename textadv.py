# print("You wake up in a dark attic")
# print("Look around?" "Door" "Window" "Floor")
# user_input = input()
#     if user_input== "Door":
#         return print("Its a large wood door, very locked")
#     elif user_input == "Window":
#         return print("There is a large tree outside. The weather is lovely, except that it is raining")
#     elif user_input == "Floor":
#         return print("A thin layer of dust barely hides a key")


def roomattic():
    print("You are in a dusty attic")
    print ("Look around?", "Door", "Window", "Floor")
    while(True):
        user_input = input()
        if user_input == "Door":
            print("It is a very locked door")
        elif user_input == "Window":
            print("There is a large tree outside with branches sticking through a broken windown pane")
            print("Climb down the tree?")
            if input() == "Yes":
                roomgarden()
                return
            else: 
                roomattic()
                return
        elif user_input == "Floor":
            print("You found a key hidden hidden under the rug. Too bad you cant pick it up.")

def roomgarden():
    print("You are in a flowering garden")
    print("Look around?", "Topiary", "Fountain", "Flowerbeds")
    while(True):
        user_input = input()
        if user_input == "Topiary":
            print("Here is a large curling bush shaped like a duck")
        elif user_input == "Fountain":
            print("Your relfection is mirrored perfectly in this pristinely still fountain. The spout doesn't seem to be working. Enscribed on the base is a riddle.")
            print("Let it be said, if one means well, that is well red, enter via bell")
            print("Drop something in the fountain?")
            if input() == "Red Poppy":
                print("Water sputters from the fountain, rippling the surface. You glimpse something under the waves.")
                print("Drop something into the fountain?")
                if input() == "Blue Bell":
                    print("The fountain turns glowing blue and you jump in with a splash")
                    roomlibrary()
                    return
                else: 
                    print("The foutain gurgles unahappily")
                    roomgarden()
                    return
            else:
                print("You relflextion looks at you blankly")
                roomgarden()
                return
        elif user_input == "Flowerbeds":
            print("There is a lovely flowerbed full of flowers", "Tigerlily", "Red Poppy", "Blue Bell", "Violet,")
            print("Pick a flower or two?")
            while(True):
                flower_input = input()
                if flower_input == "Tigerlily":
                    print("You picked a flower")
                elif flower_input == "Red Poppy":
                    print("You picked a flower")
                elif flower_input == "Blue Bell":
                    print("You picked a flower")
                elif flower_input == "Violet":
                    print("You picked a flower")
                elif flower_input == "No":
                    print("You prefer catnip anyways")
                    roomgarden()
                    return
                else:
                    print("If at first you don't succeed, try try again, or is it go fry a hen?")
                    roomgarden()
                    return

            
def roomlibrary():
    print("You are in a lonely library")
    print("There is a great big book in the center")
    print("Read book?")
    while(True):
        user_input = input()
        if user_input == "Yes":
            print("You pronounce the cooky words of the friendship spell.")
            print("Congratulations, you just relased Dinosaurs into the world. Good Luck finding them all before Willow the Witch returns")
            roomdinolib()
            return
        elif user_input == "No":
            print("Its time for a catnap anyways. Where did that spot of sun go?")
            print("Five hours later...")
            roomlibrary()
            return

def roomdinolib():
    print("There is now a pterodactyl in the library. Maybe you should be moving on")
    roomdinogar()
    
def roomdinogar():
    print("You are in a flowering garden. There must be some dinos around here somewhere")
    print("Look around?","Topiary", "Fountain", "Flowerbeds", "Tree")
    while(True):
        user_input = input()
        if user_input == "Topiary":
            print("Here is a large curling bush shaped like a duck. A strange call comes from inside the duck, as if it were talking.")
            print("Challenge the duck to a word battle?")
            duck_input = input()
            if duck_input == "Yes":
                print("Insert incredibly dope rythm here")
                while(True):
                    wordbattle = input()
                    if wordbattle == wordbattle:
                        print("The duck is completely in awe of your poetry skills and a dinosaur crawls out of its hiding spot in the duck's mouth")
                        roomdinogar()
                        return

        elif user_input == "Tree":
            print("This is the large oak tree with branches extending through the window pane of the attic. Something green and spiky is protruding out of the window")
            print("You scale the tree easily and tentatively step onto the other scaly thing.")
            print("Poke the thing?")
            poke_tail = input()
            if poke_tail== "Yes":
                print("The tail pokes back, sending you flying into the fountain")
                roomdinolib()
                return
            elif poke_tail== "No":
                print("Walk delicately across the tail?")
                play_tail = input()
                if play_tail == "Yes":
                    print("The spiny tail shivers, shaking you into the flowerbeds. Luckily, you are not harmed.")
                elif play_tail == "No":
                    print("Pounce on the twitching spike?")
                    pounce_tail = input()
                    if pounce_tail == "Yes":
                        print("The tail swooshes powerfully, pulling you into the attic in a poof of dust bunnies")
                        roomdinoattic()
                        return
                    elif pounce_tail == "No":
                        print ("You stare with much annoyance at the tail, but it is hard to have a staring contest with a dinosaur tail.")
                        roomdinogar()
                        return

        elif user_input == "Flowerbeds":
                print("This was a lovely flowerbed but some larger herbavore seems to have eaten all the flowers.You see something glimmering in the freshly churned dirt")
                print("You have found a pendant. Its a lovely emerald green, which is probably why you did not see it in the flowers, and bears the inscription Willow")
                roomdinogar ()
                return
           
        elif user_input == "Fountain":
                print("The portal is still open if you want to go visit the pyterodactyl. Then again do you really want to?")
                return
    
def roomdinoattic():
    print("There is now a stegosaurus in the attic")

roomattic()

#It is now 2022 and we have decided to restart this project from the beginning. 


#The goal is to unlock the attic door and find some friends

#Room 1: The Attic
# You are in a dusty attic. This is boring, we should look around. Maybe we can find to unlock the door, or maybe dinf some friends. You can look around. There is a Door, Window, and dusty floor with an old rug.
# The Door: It is a very locked door. 
# The Floor: You find a key hidden hidden under the rug. Too bad you can't pick it up.
#The Window: There is a large tree outside with branches sticking through a broken windown pane. You can use this to climb down into the garden


#Room 2: The Garden
# You are in a flowering garden. You can look around. There is a Topiary, a large curling bush shaped like a duck, a Flower Garden, a Foutain, and the Tree
# Climbing the Tree takes you back to Room 1- the Attic
# At this point, the Topiary does nothing.

# The Flower Bed: There is a lovely flowerbed full of flowers. You can pick a Tigerlily, a Blue Bell, a Red Poppy, and a Violet.
#Flower Bed: If you don't pick any flowers maybe return with "You prefer catnip anyways"
# Flower Bed: Also, since it may be vauge what the game is asking you do to, you say If at first you don't succeed, try try again, or is it go fry a hen? in case they don't put Red Poppy in properly or something

# The Fountain: If you answer a ridde correctly by dropping in two items in the correct order you can access the library
#Foutain: Since the spout isn't working, your relfection is mirrored perfectly in this pristinely, glassy fountain. Enscribed on the base is a riddle.
# Fountain's riddle: Let it be said, if one means well, that is well red, enter via bell
# Fountain: Here you can drop things into the fountain from your inventory. Dropping in a Red Poppy followed by a Blue Bell will allow you to jump in and enter the library.
# Fountain: If you drop in the Red Poppy: Water sputters from the fountain spout, rippling the surface. A portal is starting to form under the waves.
# Fountain: If you drop in the Blue Bell after the Red Poppy: The fountain glows blue and you jump in with a splash. You have now entered the library
#Fountain: If you don't put a Red Poppy first: You relflextion looks at you blankly
# Fountain: If you don't put in a Blue Bell after the Poppy:The foutain gurgles unahappily


#Room 3: The Library
# You are in a lonely library with a great big book in the center. 
# Your options are, read book, don't read book, leave room
# You can read the book or not. Not reading the book results in taking a 5 hour nap in a spot of sun. And you return to your two options of read or no. 
#If you take a nap: Its time for a catnap anyways. Where did that spot of sun go? Five hours later...
#If you read the book: You pronounce the cooky words of the friendship spell.Congratulations, you just relased Dinosaurs into the world. Good Luck finding them all before Willow the Witch returns


# Reading the Book is the Flag that turns all three rooms into dinosaur filled rooms.


#Room 4: Pterodactyl in the Library. Your only option is to leave
#There is now a pterodactyl in the library. Maybe you should be moving on


#Room 5: Dinos in the Garden
#You are in a flowering garden. There must be some dinos around here somewhere
# Here you can interact with the Topiary, examine the floorbed, or try to climb the tree. The Foutain no longer allows you into the library. 
# Foutain: The portal is still open if you want to go visit the pyterodactyl. Then again do you really want to?

#Flowerbed: Searching the floorbed adds Willow's pendant to your inventory
#Flowerbed text: This was a lovely flowerbed but some larger herbavore seems to have eaten all the flowers.You see something glimmering in the freshly churned dirt
#Flowerbed text cont: You have found a lovely emerald green pendant, with the inscription Willow. It's a little heavy to carry around your neck but nothing your grace can't handle

#The Topiary: Here you can engage in a word battle with the now talking duck. Any kind of text will impress the duck and bring the dino out of hiding.
#Topiary text: Here is a large curling bush shaped like a duck. A strange call comes from inside the duck, as if it were talking.
# Topiary text cont: Challenge the duck to a word battle? Insert incredibly dope rythm here 
# Topiary text cont: The duck is completely in awe of your poetry skills and a small parasaurolophus crawls out of its hiding spot in the duck's mouth

#The Tree: When you try to climb the tree, you are blocked by a large spiky tail. Your options are Poke, Pounce, Walk Gently, or Stare in Annoyance
# The Tree: This is the large oak tree with branches extending through the window pane of the attic. Something green and spiky is protruding out of the window
# The Tree: You scale the tree easily and tentatively approach the scaly thing that blocks your way into the attic.
# Tree Poke: the tail sends you flying into back into the fountain, spawning you in the Pterodactyl library
# Tree Poke: The tail pokes back, sending you flying into the fountain"
# Tree Pounce: Pouncing on the tail allows you to enter the Stegosaurus Attic
# Tree Pounce: The tail swooshes powerfully, pulling you into the attic in a poof of dust bunnies
# Tree Walk: Walking on the tail sends you back into the Dino garden. 
# Tree Walk: The spiny tail shivers, shaking you into the flowerbeds. Luckily, you are not harmed
# Tree Stare: This does nothing. You stare with much annoyance at the tail, but it is hard to have a staring contest with a dinosaur tail.


#Room 6: Stegosaurus in the Attic
# A rather large Stagosaurus takes up most of this space. He is currently eating the rug
#(You can now exit and enter the window to the garden as you please. If you go back to the garden you don't have to play with the tail? You can just walk in?)
# In this room, you can try to open the locked door, go through the window, examine the floor, or play with the stegosaurus tail. 

#Tail: Same options as before, Poke, Pounce, Walk, or Stare. None of these do anything unless the dinosaur is turned around. In which case, Poke let's you out. 
# Tail Poke: The tail pokes back, putting another hole in the window
#Tail poke: If you have turned the dino around, poking puts a hole in the door. You are free!
# Tail Pounce: The tail swooshes powerfully, pulling you around the attic in a poof of dust bunnies
#Tail Stare: You stare with much annoyance at the tail, but it is hard to have a staring contest with a dinosaur tail
#Tail Walk: he spiny tail shivers, throwing you up into the air. Luckily, you are not harmed.

#Door: The door is still very locked.
#Door: After the dino punches a hole in the door: The door has a large horn shaped hole in it. It's a perfect exit for you!
#Door: Jump through the door. You are free! This leads you to the Kitchen

#Window: jumping through the window takes you to the garden
# Floor: The key is gone. The stegosaurs may have already eaten it. He seems to be enjoying the rug. 
# Floor: You have the option to drag the rug. Doing so turns the dinosaur around. His tail is now facing the locked door. 


#Room 7: The Kitchen
# This is Willow's tidy, warm kitchen, with a breakfast table and flower vase. There is also another book in here. 
# You have all these new friends, you should throw a tea party!
# You look at the table of contents in the book. 

# Your options are read the T, E, or A spell. Type in different words with these letters to cast the spell. 
#Tea- Spawn a buttercup yellow teapot with matching teacups. The pot is nice and warm and fills the room with a black, cinnamony smell
#Tae - Nothing happens
#Ate- Scrumpious little crustless sandwhichs appear. Of course, there are cucumber options for the dinos and tuna for you
#Aet-  Nothing happens
#Eat- Lovely bunt cakes appear at each table spot. Do dinos eat cake? They do at your parties!
#Eta- An hourglass appears. It looks like Willow is coming home soon, but you don't care. You have a tea party to plan

# Your last option is "Close the book and start the party!"
# When you have closed, the dinosaurs come to the table and you all have a wonderful tea party. 
# you have one spell left to read the Z..z..z spell. 
#Reading the Z spell sends the Dinos home and you have a long nap and only wake up when Willow comes home. 
# While you definitely smashed up the house a bit, your efforts allowed Willow to find her pendant. She forgives you. 
#Of course, she does. You are a very cute cat after all. 
