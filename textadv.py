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
                elif flower_input == "Red Poppies":
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
            print("Congratulations, you just relased Dinosaurs onto the world. Good Luck finding them all before Willow returns")
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
    print("You are in a flowering garden. There must be some dinos around here somewhere.")
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
                return
           
        elif user_input == "Fountain":
                print("The portal is still open if you want to go visit the pyterodactyl. Then again do you really want to?")
                return
    
def roomdinoattic():
    print("There is now a stegasaurus in the attic")

roomattic()
