"""
Name : Jason
Program : Maze Game
Filename : Maze Game.py
Date : 2018/09/10
Version : 1.5
"""
import random
LOOP = True
Control = True
LVL = int(1)
TEXT = True  # This will never change, it's just there to make editing this code block easier
while Control is True:
    print("System Message: There are four control schemes (+1 Joke mode)")
    print("Please select one from the four listed:")
    print("          UP   |  DOWN |  LEFT | RIGHT ")
    print("1|NSWE: (N)orth|(S)outh|(W)est |(E)ast ")
    print("2|UDLR: (U)p   |(D)own |(L)eft |(R)ight")
    print("3|WSAD: (W)    |(S)    |(A)    |(D)    ")
    print("4|NUMP: (8)    |(2)    |(4)    |(6)    ")
    print("5|WHAT: (?)????|(?)????|(?)????|(?)????")
    CTRL = input("Your choice of input: ")
    if CTRL == "1":
        Up = ["N", "n", "North", "north", "NORTH"]
        Down = ["S", "s", "South", "south", "SOUTH"]
        Left = ["W", "w", "West", "west", "WEST"]
        Right = ["E", "e", "East", "east", "EAST"]
        print("You have selected NSWE\n")
        Control = False
    elif CTRL == "2":
        Up = ["U", "u", "Up", "up", "UP"]
        Down = ["D", "d", "Down", "down", "DOWN"]
        Left = ["L", "l", "Left", "left", "LEFT"]
        Right = ["R", "r", "Right", "right", "RIGHT"]
        print("You have selected UDLR\n")
        Control = False
    elif CTRL == "3":
        Up = ["W", "w"]
        Down = ["S", "s"]
        Left = ["A", "a"]
        Right = ["D", "d"]
        print("You have selected WSAD\n")
        Control = False
    elif CTRL == "4":
        Up = "8"
        Down = "2"
        Left = "4"
        Right = "6"
        print("You have selected NUMP\n")
        Control = False
    elif CTRL == "5":
        Confirm = input("Are you wanna die?(Y/N) ")
        if Confirm in ["Y", "y"]:
            Up = "Once upon a time, a boy flew up into the sky, because he wanted to go up I guess.."
            Down = "There was this man, who felt down, who fell down a well.."
            Left = "Long, long, long ago, a girl punched a bear and left towards the left.."
            Right = "There was this woman, who was right about going right through a tree.."
            print("You've asked for it... Now you cry.")
            print("\nAll you have to remember is..."
                  "\nTo go up, you type:"
                  "\n{0}"
                  "\nTo go down, you type:"
                  "\n{1}"
                  "\nTo go left, you type:"
                  "\n(2)"
                  "\nTo go right, you type:"
                  "\n{3}"
                  "\nOne wrong letter, one bad capital letter, you have to do it again."
                  "\nYou also have to remember all this, because I'm not telling you again..."
                  "\nGood luck"
                  .format(Up, Down, Left, Right))
            Control = False
        else:
            print("I thought so.\n")
    else:
        print("System Message: There are only five control schemes!")
print("Welcome to the maze! Your objective is to navigate to the end!\n")
while LOOP is not False:
    Switch = False
    GAME = True
    while GAME is not False:  # Map loader
        if LVL == 1:
            # 0 = Wall, 1 = space, 2 = start, 3 = end
            #        0  1  2  3  4  5  6  7
            grid = [[0, 0, 0, 0, 0, 0, 0, 0],  # 0
                    [0, 2, 1, 0, 1, 0, 3, 0],  # 1
                    [0, 0, 1, 0, 1, 0, 1, 0],  # 2
                    [0, 1, 1, 0, 1, 1, 1, 0],  # 3
                    [0, 1, 0, 0, 1, 0, 1, 0],  # 4
                    [0, 1, 1, 0, 1, 0, 1, 0],  # 5
                    [0, 1, 0, 0, 1, 1, 1, 0],  # 6
                    [0, 1, 1, 1, 1, 0, 1, 0],  # 7
                    [0, 0, 0, 0, 0, 0, 0, 0]]  # 8
            print("  ^^^^^^^^^  ")
            print("< Level One >")
            print("  vvvvvvvvv  ")
            GAME = False
        elif LVL == 2:
            # 0 = Wall, 1 = space, 2 = start, 3 = end
            #        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0 done
                    [0, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1 done
                    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 2 done
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],  # 3 done
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 4 done
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],  # 5 done
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 6 done
                    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],  # 7 done
                    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 8 done
                    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],  # 9 done
                    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10 done
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # 11 done
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 12 done
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],  # 13 done
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],  # 14 done
                    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],  # 15 done
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 16 done
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],  # 17 done
                    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 18 done
                    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 3, 0],  # 19 done
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 20 done
            """Visual interpretation
            000000000011111111112
            012345678901234567890
            XXXXXXXXXXXXXXXXXXXXX done
            XS  X   X   X XXXXXXX done
            X X XXX X XXX XXXXXXX done
            X   XXX     X   XXX X done
            XXX XXX X XXXXX XXX X done
            XXX     X   X       X done
            XXXXX XXX X XXX XXXXX done
            X     XXX X XXX     X done
            X X XXXXXXX XXX XXX X done
            X X   X         XXX X done
            X X XXXXX XXXXXXXXXXX done
            X   XXX         XXXXX done
            XXX XXXXXXXXXXX XXXXX done
            XXX   XXXXXXX       X done
            XXXXX XXXXXXX XXX X X done
            XXX X         X X   X done
            XXX XXX XXX XXX XXX X done
            X   XXX     XXX     X done
            X X XXXXX XXXXX XXXXX done
            X X         XXX    EX done
            XXXXXXXXXXXXXXXXXXXXX done
            # S = Start
            # E = End"""
            print("  ^^^^^^^^^  ")
            print("< Level Two >")
            print("  vvvvvvvvv  ")
            GAME = False
        elif LVL == 3:
            # 0 = Wall, 1 = space, 2 = start, 3 = end, 4 = BOSS
            #        0  1  2  3  4  5  6
            grid = [[0, 0, 0, 0, 0, 0, 0],  # 0
                    [0, 2, 0, 3, 4, 1, 0],  # 1
                    [0, 1, 1, 0, 0, 1, 0],  # 2
                    [0, 0, 1, 0, 1, 1, 0],  # 3
                    [0, 0, 1, 1, 0, 1, 0],  # 4
                    [0, 5, 0, 1, 0, 1, 0],  # 5
                    [0, 1, 1, 1, 0, 1, 0],  # 6
                    [0, 0, 1, 0, 1, 1, 0],  # 7
                    [0, 0, 1, 1, 0, 1, 0],  # 8
                    [0, 1, 1, 1, 0, 1, 0],  # 9
                    [0, 1, 0, 0, 1, 1, 0],  # 10
                    [0, 1, 1, 0, 0, 1, 0],  # 11
                    [0, 0, 1, 0, 1, 1, 0],  # 12
                    [0, 0, 1, 0, 1, 0, 0],  # 13
                    [0, 0, 1, 0, 1, 1, 0],  # 14
                    [0, 1, 1, 1, 0, 1, 0],  # 15
                    [0, 1, 0, 1, 0, 1, 0],  # 16
                    [0, 1, 0, 1, 0, 1, 0],  # 17
                    [0, 1, 0, 0, 1, 1, 0],  # 18
                    [0, 1, 1, 0, 1, 0, 0],  # 19
                    [0, 0, 1, 0, 1, 1, 0],  # 20
                    [0, 0, 1, 0, 1, 1, 0],  # 21
                    [0, 1, 1, 1, 0, 1, 0],  # 22
                    [0, 1, 0, 0, 0, 1, 0],  # 23
                    [0, 1, 1, 1, 1, 1, 0],  # 24
                    [0, 0, 0, 0, 0, 0, 0]]  # 25
            print("  ^^^^^^^^^^^  ")
            print("< Level Three >")
            print("  vvvvvvvvvvv  ")
            GAME = False
        elif LVL == 4:
            # 0 = Wall, 1 = space, 2 = start, 3 = end, 6 = | gates, 7 = _ gates, 8 = switch
            #        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0 done
                    [0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],  # 1 done
                    [0, 1, 1, 1, 6, 1, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 1, 0],  # 2 done
                    [0, 8, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],  # 3 done
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 8, 0, 0, 0, 0, 0, 1, 0],  # 4 done
                    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],  # 5 done
                    [0, 1, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 6 done
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # 7 done
                    [0, 0, 0, 0, 0, 0, 0, 8, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # 8 done
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 9 done
                    [0, 1, 1, 1, 1, 1, 1, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 0],  # 10 done
                    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 11 done
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 12 done
                    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 3, 0, 0],  # 13 done
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 0, 0],  # 14 done
                    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],  # 15 done
                    [0, 1, 1, 1, 1, 1, 0, 0, 8, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # 16 done
                    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],  # 17 done
                    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],  # 18 done
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 19 done
            """Visual Aid
            000000000011111111
            012345678901234567
            XXXXXXXXXXXXXXXXXX Done
            XS  X      X     X Done
            X   | XXXX | XXX X Done
            X&  X      XXXXX X Done
            XXXXXXX XX&XXXXX X Done
            X       XXXX     X Done
            X & XXXXXXXX XXXXX Done
            XXXXXX         XXX Done
            XXXXXXX&        XX Done
            XXXXXXXX         X 6 switches
            X      X_XXXXX&XXX 4 doors
            X XXXX   X XXXXXXX
            X   XXXXXX XXXXXXX
            X X        XXXXEXX
            X XXX XXXX XXXX_XX
            XX XX XXXX       X
            X     XX&XXXXX   X
            X XXX XX XX XXX  X
            X XXX       XXXX X
            XXXXXXXXXXXXXXXXXX
            # S = Start
            # E = End
            # |, _ = doors
            # & = Switch"""
            print("  ^^^^^^^^^^  ")
            print("< Level Four >")
            print("  vvvvvvvvvv ")
            Switch1a = False
            Switch2a = False
            Switch2b = False
            Switch3a = False
            Switch3b = False
            Switch4a = False
            '''Switch1a = grid[3][1]
            Switch2a = grid[4][10]
            Switch2b = grid[6][2]
            Switch3a = grid[8][7]
            Switch3b = grid[10][14]
            Switch4a = grid[16][8]
            Gate1 = grid[2][4]
            Gate2 = grid[2][11]
            Gate3 = grid[10][8]
            Gate4 = grid[14][15]
            '''
            Switch = True
            GAME = False
        else:
            GAME = False
            LOOP = False
            break
    R = int(1)
    C = int(1)
    if TEXT is True:
        SwitchText = "You've found a switch! You hear a click!"
        DoorText = "You've found a gate... you'll need to find a way to open it though..."
        UserText = "Your answer: "
        UserMove = "Which way do you like to go? "
        BossSign = "\n~~~~BOSS~~~~~"
        CountText = ("\nHello user, I am The Count"
                     "\nI'm made so that you cannot pass without defeating me"
                     "\n..."
                     "\nLet's begin...")
        CountWarning = "You're only allowed positive integers."
        CountDisappoint = "That is incorrect"
        CountApproved1 = "Correct, onto the next question"
        CountApproved2 = "Correct, onto the last question"
        CountApproved3 = "Correct... we're done...\n"
        CountNoMiss = "Congrats! You got all of them right! You may pass!\n"
        Count1Miss = "One wrong! Great job, now off with ya.\n"
        Count2Miss = "Just passed! You can go.\n"
        CountHates = "You failed. Come back when you are truly ready.\n"
        LevelCompletion = "\nYou finished the level!"
        WallText1 = "\nThat's a wall! No matter how hard you try, you just can't phase through!"
        WallText2 = "\nThat's still wall... you can't go through it."
        WallText3 = "\nNope! It's a wall."
        WallText4 = "\nIt's obviously a wall, and you aren't a ghost."
        NorthText = "\nYou moved north, which is up!"
        SouthText = "\nYou moved south, which is down!"
        WestText = "\nYou moved west, which is left!"
        EastText = "\nYou moved east, which is right!"
        SecretText1 = ("\nYou encountered a big plush dragon!"
                       "\nIt did nothing because it does nothing."
                       "\nYou can't do anything about it either."
                       "\nThe plush dragon is just sorta there as decoration or something..."
                       "\nAt least you get to say you've found a secret?")
        SecretText2 = ("\nYou encountered a big plush T-Rex!"
                       "\nIt did nothing because it does nothing."
                       "\nYou can't do anything about it either."
                       "\nThe plush T-Rex is just sorta there as decoration or something..."
                       "\nAt least you get to say you've found a secret?")
        SecretText3 = ("\nYou encountered a big plush doggo!"
                       "\nIt is a good boy."
                       "\nYou can't do anything about it."
                       "\nThe plush doggo is just sorta there as a proof of concept..."
                       "\nAt least you get to say you've found a secret?")
        SecretText4 = ("\nYou encountered a big plush dolphin!"
                       "\nIt did nothing because it does nothing."
                       "\nYou can't do anything about it either."
                       "\nThe plush dolphin is just sorta there as decoration or something..."
                       "\nAt least you get to say you've found a secret?")
        LevelText = "\nGreat job! Onto the next level!"
        Congratulations = "You've completed all the levels! Good job!!! You've finished the maze game! Congrats!"
    while grid[R][C] != 3:  # Main game
            MAP = False
            North = R - 1
            South = R + 1
            West = C - 1
            East = C + 1
            while MAP is not True:  # This creates a visual 9X9 map representing how
                    View = [[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]
                    A = int(0)
                    D = int(1)
                    E = int(1)
                    F = int(1)
                    View1 = [grid[North][West], grid[North][C], grid[North][East]]
                    View2 = [grid[R][West], grid[R][C], grid[R][East]]
                    View3 = [grid[South][West], grid[South][C], grid[South][East]]
                    while D != 4:
                            if View1[A] == 0:
                                    View[0][A] = "█"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 2:
                                    View[0][A] = "▓"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 3:
                                    View[0][A] = "▒"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 4:
                                    View[0][A] = "#"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 5:
                                    View[0][A] = "+"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 6:
                                    View[0][A] = "|"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 7:
                                    View[0][A] = "_"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            elif View1[A] == 8:
                                    View[0][A] = "!"
                                    A = int(A + 1)
                                    D = int(D + 1)
                            else:
                                    View[0][A] = "░"
                                    A = int(A + 1)
                                    D = int(D + 1)
                    A = int(0)
                    while E != 4:
                            if View2[A] == 0:
                                    View[1][A] = "█"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 2:
                                    View[1][A] = "▓"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 3:
                                    View[1][A] = "▒"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 4:
                                    View[1][A] = "#"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 5:
                                    View[1][A] = "+"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 6:
                                    View[1][A] = "|"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 7:
                                    View[1][A] = "_"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 8:
                                    View[1][A] = "!"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            else:
                                    View[1][A] = "░"
                                    A = int(A + 1)
                                    E = int(E + 1)
                    A = int(0)
                    while F != 4:
                            if View3[A] == 0:
                                    View[2][A] = "█"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 2:
                                    View[2][A] = "▓"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 3:
                                    View[2][A] = "▒"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 4:
                                    View[2][A] = "#"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 5:
                                    View[2][A] = "+"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 6:
                                    View[2][A] = "|"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 7:
                                    View[2][A] = "_"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 8:
                                    View[2][A] = "!"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            else:
                                    View[2][A] = "░"
                                    A = int(A + 1)
                                    F = int(F + 1)

                    MAP = True
            while grid[R][C] == 4:
                MISS = int(0)
                BOSS = True  # boss code
                Q1 = True
                Q2 = True
                Q3 = True
                Q4 = True
                Judgement = True
                print(BossSign)
                if LVL == 3:
                    print(CountText)
                    NUMBER = random.randint(1, 20)
                    print("And we begin... with the number {0}".format(NUMBER))
                    while BOSS is True:
                        print("Answer two of four questions right, and you shall pass")
                        b1q1 = (int(NUMBER) + 13 - 44 - 200 + 1759)
                        b1q2 = (4 * int(NUMBER) / 4 * 17)
                        b1q3 = (int(NUMBER) + b1q2 * (43 - 14) * 10)
                        b1q4 = (4 * 19 / 2 + int(NUMBER) * 29 + 7849)
                        while Q1 is True:
                            print("\nFirst question, what is {0} plus 13 minus forty-four".format(NUMBER))
                            print("minus 2 hundred plus 17 hundred 59?\n")
                            Checker = False
                            while Checker is False:
                                b1a1 = input(UserText)
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a1)
                                        valid = True
                                        Checker = True
                                    except ValueError:
                                        print(CountWarning)
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q1)
                            if USER == ANSB:
                                print(CountApproved1)
                                Q1 = False
                            else:
                                print(CountDisappoint)
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q1 = False
                        while Q2 is True:
                            print("\nWhat is 4 times {0} divided by the first number times 17?\n".format(NUMBER))
                            Checker = False
                            while Checker is False:
                                b1a2 = input(UserText)
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a2)
                                        valid = True
                                        Checker = True
                                    except ValueError:
                                        print(CountWarning)
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q2)
                            if USER == ANSB:
                                print(CountApproved1)
                                Q2 = False
                            else:
                                print(CountDisappoint)
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q2 = False
                        while Q3 is True:
                            print("\nNow, what is {0} plus {1} times (43 - 14) times ten?\n".format(NUMBER, int(b1q2)))
                            Checker = False
                            while Checker is False:
                                b1a3 = input(UserText)
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a3)
                                        valid = True
                                        Checker = True
                                    except ValueError:
                                        print(CountWarning)
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q3)
                            if ANSB == USER:
                                print(CountApproved2)
                                Q3 = False
                            else:
                                print(CountDisappoint)
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q3 = False
                        while Q4 is True:
                            print("\nLast one...")
                            print("What is 4 times 19 divided by two plus the number we began with times 29")
                            print("plus 78 hundred 49?\n")
                            Checker = False
                            while Checker is False:
                                b1a4 = input(UserText)
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a4)
                                        valid = True
                                        Checker = True
                                    except ValueError:
                                        print(CountWarning)
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q4)
                            if USER == ANSB:
                                print(CountApproved3)
                                Q4 = False
                            else:
                                print(CountDisappoint)
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q4 = False
                        while Judgement is True:
                            if MISS == 0:
                                print(CountNoMiss)
                                grid[1][4] = int(1)
                                BOSS = False
                                Judgement = False
                            elif MISS == 1:
                                print(Count1Miss)
                                grid[1][4] = int(1)
                                BOSS = False
                                Judgement = False
                            elif MISS == 2:
                                print(Count2Miss)
                                grid[1][4] = int(1)
                                BOSS = False
                                Judgement = False
                            else:
                                print(CountHates)
                                R = int(22)
                                C = int(3)
                                BOSS = False
                                Judgement = False
            print("\n <<[MAP]>>")
            print("     ^      ")
            print("  ---N----  ")
            print(" | {0}{0}{1}{1}{2}{2} | ".format(View[0][0], View[0][1], View[0][2]))
            print(" | {0}{0}{1}{1}{2}{2} | ".format(View[0][0], View[0][1], View[0][2]))
            print("<  {0}{0}/\{2}{2} E>".format(View[1][0], View[1][1], View[1][2]))
            print("<W {0}{0}\/{2}{2}  >".format(View[1][0], View[1][1], View[1][2]))
            print(" | {0}{0}{1}{1}{2}{2} | ".format(View[2][0], View[2][1], View[2][2]))
            print(" | {0}{0}{1}{1}{2}{2} | ".format(View[2][0], View[2][1], View[2][2]))
            print("  ^^^^S^^^  ")
            print("      v     ")
            Fin = False
            Move = input(UserMove)
            if Move in Up:
                    while Fin is not True:
                            if grid[North][C] == 0:
                                    print(WallText1)
                                    Fin = True
                            elif grid[North][C] == 2:
                                    R = (R - 1)
                                    print(NorthText)
                                    Fin = True
                            elif grid[North][C] == 3:
                                    R = (R - 1)
                                    print(LevelCompletion)
                                    Fin = True
                            elif grid[North][C] == 5:
                                    print(SecretText1)
                                    Fin = True
                            elif grid[North][C] in [6, 7]:
                                    print(DoorText)
                                    Fin = True
                            elif grid[North][C] == 8:
                                    R = (R - 1)
                                    print(SwitchText)
                                    Fin = True
                            else:
                                    R = (R - 1)
                                    print(NorthText)
                                    Fin = True
            elif Move in Down:
                    while Fin is not True:
                            if grid[South][C] == 0:
                                    print(WallText2)
                                    Fin = True
                            elif grid[South][C] == 2:
                                    R = (R + 1)
                                    print(SouthText)
                                    Fin = True
                            elif grid[South][C] == 3:
                                    R = (R + 1)
                                    print(LevelCompletion)
                                    Fin = True
                            elif grid[South][C] == 5:
                                    print(SecretText2)
                                    Fin = True
                            elif grid[South][C] in [6, 7]:
                                    print(DoorText)
                                    Fin = True
                            elif grid[South][C] == 8:
                                    R = (R + 1)
                                    print(SwitchText)
                                    Fin = True
                            else:
                                    R = (R + 1)
                                    print(SouthText)
                                    Fin = True
            elif Move in Left:
                    while Fin is not True:
                            if grid[R][West] == 0:
                                    print(WallText3)
                                    Fin = True
                            elif grid[R][West] == 2:
                                    C = (C - 1)
                                    print(WestText)
                                    Fin = True
                            elif grid[R][West] == 3:
                                    C = (C - 1)
                                    print(LevelCompletion)
                                    Fin = True
                            elif grid[R][West] == 5:
                                    print(SecretText3)
                                    Fin = True
                            elif grid[R][West] in [6, 7]:
                                    print(DoorText)
                                    Fin = True
                            elif grid[R][West] == 8:
                                    C = (C - 1)
                                    print(SwitchText)
                                    Fin = True
                            else:
                                    C = (C - 1)
                                    print(WestText)
                                    Fin = True
            elif Move in Right:
                    while Fin is not True:
                            if grid[R][East] == 0:
                                    print(WallText4)
                                    Fin = True
                            elif grid[R][East] == 2:
                                    C = (C + 1)
                                    print(EastText)
                                    Fin = True
                            elif grid[R][East] == 3:
                                    C = (C + 1)
                                    print(LevelCompletion)
                                    Fin = True
                            elif grid[R][East] == 5:
                                    print(SecretText4)
                                    Fin = True
                            elif grid[R][East] in [6, 7]:
                                    print(DoorText)
                                    Fin = True
                            elif grid[R][East] == 8:
                                    C = (C + 1)
                                    print(SwitchText)
                                    Fin = True
                            else:
                                    C = (C + 1)
                                    print(EastText)
                                    Fin = True
            else:
                if CTRL == "5":
                    print("No hints for you!")
                else:
                    print("Only up, down, left, right please!")
                    print("Up:   ", Up)
                    print("Down: ", Down)
                    print("Left: ", Left)
                    print("Right:", Right)
            if Switch is True:
                if LVL == 4:
                    if R == 3 and C == 1:
                        Switch1a = True
                        grid[3][1] = int(1)
                    elif R == 4 and C == 10:
                        Switch2a = True
                        grid[4][10] = int(1)
                    elif R == 6 and C == 2:
                        Switch2b = True
                        grid[6][2] = int(1)
                    elif R == 8 and C == 7:
                        Switch3a = True
                        grid[8][7] = int(1)
                    elif R == 10 and C == 14:
                        Switch3b = True
                        grid[10][14] = int(1)
                    elif R == 16 and C == 8:
                        Switch4a = True
                        grid[16][8] = int(1)
                    if Switch1a is True:
                        grid[2][4] = int(1)
                    elif Switch2a is True and Switch2b is True:
                        grid[2][11] = int(1)
                    elif Switch3a is True and Switch3b is True:
                        grid[10][8] = int(1)
                    elif Switch4a is True:
                        grid[14][15] = int(1)
    LVL = (LVL + 1)  # When the user goes onto "3" on the map, the game stops the loop and adds 1 to the LVL count
    if LVL <= 4:
        print(LevelText)
    else:
        LOOP = False
        break
print(Congratulations)
done = input("See you in the word guessing game")
# Final thoughts:
"""
I created this code in such a way that I can keep adding onto it without messing up the main code.
This allows me to have different size maps and multiple levels, and maybe even make a new feature.
The hardest part was either starting the code, or the graphic map generator.
Also I learned something very useful: you can indent a block of code by selecting the block and pressing Tab...
it saved more than 20 minutes of work."""
# Version Details:
"""
0.1: Started project
0.2: Remade the map
1.0: Completed game code, with playable map
1.1: Added the graphic map generator
1.2: Added levels
1.2.1: Added Final thoughts and Version details
1.2.2: Rearranged the tiles of the map generator, and removed map planner
1.3: Created new map with new feature, along with some changes for the program to allow new features
1.3.1: Fixed visual map
1.3.2: Added centerpiece to avoid confusion
1.3.3: Made map Biiiigggg
1.4: 1st boss created
1.4.1: Fixed boss
1.4.2: Added something... a secret?
1.4.3: made the game completable
1.4.4: Fixed some text things
1.5: Added map and visual aid
1.5.1: Changed some values to boolean
1.5.2: Removed secret from "normal" levels. and fixed map
1.5.3: mapped doors and switches
1.5.4: Coded em!
1.5.5: Coded graphics and bug fixes
1.5.6: Took most text outside function
1.5.7: applied text to those switches and gates, and took one more line out
1.5.8: Added options to use WSAD, UDLR, NSWE, or 8246(Numberpad)
1.5.9: Inserted JOKE mode, and changed a text to match these control schemes"""
