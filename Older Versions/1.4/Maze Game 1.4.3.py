"""
Name : Jason
Program : Maze Game
Filename : Maze Game.py
Date : 2018/09/10
Version : 1.4.3
"""
import random
LOOP = "True"
LVL = int(1)
print("Welcome to the maze! Your objective is to navigate to the end!")
print("Put in N for north, S for south, W for west, E for east!")
while LOOP != "False":
    GAME = "True"
    while GAME != "False":  # Map loader
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
                    [0, 1, 1, 1, 1, 0, 5, 0],  # 7
                    [0, 0, 0, 0, 0, 0, 0, 0]]  # 8
            print("  ^^^^^^^^^  ")
            print("< Level One >")
            print("  vvvvvvvvv  ")
            GAME = "False"
        elif LVL == 2:
            # 0 = Wall, 1 = space, 2 = start, 3 = end
            #        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0 done
                    [0, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1 done
                    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 2 done
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 5, 0],  # 3 done
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
            print("  ^^^^^^^^^  ")
            print("< Level Two >")
            print("  vvvvvvvvv  ")
            GAME = "False"
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
            GAME = "False"
        else:
            GAME = "False"
            LOOP = "False"
            break
    R = int(1)
    C = int(1)
    while grid[R][C] != 3:  # Main game
            MAP = "N"
            North = R - 1
            South = R + 1
            West = C - 1
            East = C + 1
            while MAP != "Y":  # This creates a visual 9X9 map representing how
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
                            else:
                                    View[2][A] = "░"
                                    A = int(A + 1)
                                    F = int(F + 1)

                    MAP = "Y"
            while grid[R][C] == 4:
                MISS = int(0)
                BOSS = "True"  # boss code
                Q1 = "True"
                Q2 = "True"
                Q3 = "True"
                Q4 = "True"
                Judgement = "True"
                print("\n~~~~BOSS~~~~~")
                if LVL == 3:
                    print("Hello user, I am The Count")
                    print("I'm made so that you cannot pass without defeating me")
                    print("...")
                    print("Let's begin")
                    NUMBER = random.randint(1, 20)
                    print("And we begin, with the number {0}".format(NUMBER))
                    while BOSS == "True":
                        print("Answer two of four questions right, and you shall pass")
                        b1q1 = (int(NUMBER) + 13 - 44 - 200 + 1759)
                        b1q2 = (4 * int(NUMBER) / 4 * 17)
                        b1q3 = (int(NUMBER) + b1q2 * (43 - 14) * 10)
                        b1q4 = (4 * 19 / 2 + int(NUMBER) * 29 + 7849)
                        while Q1 == "True":
                            print("\nFirst question, what is {0} plus 13 minus forty-four".format(NUMBER))
                            print("minus 2 hundred plus 17 hundred 59?\n")
                            Checker = "N"
                            while Checker == "N":
                                b1a1 = input("Your answer: ")
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a1)
                                        valid = True
                                        Checker = "Y"
                                    except ValueError:
                                        print("You're only allowed positive integers.")
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q1)
                            if USER == ANSB:
                                print("Correct, onto the next question")
                                Q1 = "False"
                            else:
                                print("That's incorrect")
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q1 = "False"
                        while Q2 == "True":
                            print("\nWhat is 4 times {0} divided by the first number times 17?\n".format(NUMBER))
                            Checker = "N"
                            while Checker == "N":
                                b1a2 = input("Your answer: ")
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a2)
                                        valid = True
                                        Checker = "Y"
                                    except ValueError:
                                        print("You're only allowed positive integers.")
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q2)
                            if USER == ANSB:
                                print("Correct, onto the next question")
                                Q2 = "False"
                            else:
                                print("That's incorrect")
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q2 = "False"
                        while Q3 == "True":
                            print("\nNow, what is {0} plus {1} times (43 - 14) times ten?\n".format(NUMBER, int(b1q2)))
                            Checker = "N"
                            while Checker == "N":
                                b1a3 = input("Your answer: ")
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a3)
                                        valid = True
                                        Checker = "Y"
                                    except ValueError:
                                        print("You're only allowed positive integers.")
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q3)
                            if ANSB == USER:
                                print("Correct, onto the last question")
                                Q3 = "False"
                            else:
                                print("That's incorrect")
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q3 = "False"
                        while Q4 == "True":
                            print("\nLast one...")
                            print("What is 4 times 19 divided by two plus the number we began with times 29")
                            print("plus 78 hundred 49?\n")
                            Checker = "N"
                            while Checker == "N":
                                b1a4 = input("Your answer: ")
                                valid = False
                                while valid is not True:
                                    try:
                                        test = int(b1a4)
                                        valid = True
                                        Checker = "Y"
                                    except ValueError:
                                        print("You're only allowed positive integers.")
                                        valid = True
                            USER = int(test)
                            ANSB = int(b1q4)
                            if USER == ANSB:
                                print("Correct... we're done.")
                                Q4 = "False"
                            else:
                                print("That's incorrect")
                                print("it was {}".format(ANSB))
                                MISS = (MISS + 1)
                                Q4 = "False"
                        while Judgement == "True":
                            if MISS == 0:
                                print("Congrats! You got all of them right! You may pass!")
                                grid[1][4] = int(1)
                                BOSS = "False"
                                Judgement = "False"
                            elif MISS == 1:
                                print("One wrong! Great job, now off with ya.")
                                grid[1][4] = int(1)
                                BOSS = "False"
                                Judgement = "False"
                            elif MISS == 2:
                                print("Just passed! You can go.")
                                grid[1][4] = int(1)
                                BOSS = "False"
                                Judgement = "False"
                            else:
                                print("You failed. Come back when you are truly ready.")
                                R = int(22)
                                C = int(3)
                                BOSS = "False"
                                Judgement = "False"
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
            Fin = "N"
            Move = input("Which way do you like to go? ")
            if Move in ["N", "n"]:
                    while Fin != "Y":
                            if grid[North][C] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[North][C] == 2:
                                    R = (R - 1)
                                    print("You moved north, which is up!")
                                    Fin = "Y"
                            elif grid[North][C] == 3:
                                    R = (R - 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
                            elif grid[North][C] == 5:
                                    print("You encountered a big plush dragon!")
                                    print("It did nothing because it does nothing.")
                                    print("You can't do anything about it either.")
                                    print("The plush dragon is just sorta there as decoration or something...")
                                    print("At least you get to say you've found a secret?")
                                    Fin = "Y"
                            else:
                                    R = (R - 1)
                                    print("You moved north, which is up!")
                                    Fin = "Y"
            elif Move in ["S", "s"]:
                    while Fin != "Y":
                            if grid[South][C] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[South][C] == 2:
                                    R = (R + 1)
                                    print("You moved south, which is down!")
                                    Fin = "Y"
                            elif grid[South][C] == 3:
                                    R = (R + 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
                            elif grid[South][C] == 5:
                                    print("You encountered a big plush dragon!")
                                    print("It did nothing because it does nothing.")
                                    print("You can't do anything about it either.")
                                    print("The plush dragon is just sorta there as decoration or something...")
                                    print("At least you get to say you've found a secret?")
                                    Fin = "Y"
                            else:
                                    R = (R + 1)
                                    print("You moved south, which is down!")
                                    Fin = "Y"
            elif Move in ["W", "w"]:
                    while Fin != "Y":
                            if grid[R][West] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[R][West] == 2:
                                    C = (C - 1)
                                    print("You moved west, which is left!")
                                    Fin = "Y"
                            elif grid[R][West] == 3:
                                    C = (C - 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
                            elif grid[R][West] == 5:
                                    print("You encountered a big plush dragon!")
                                    print("It did nothing because it does nothing.")
                                    print("You can't do anything about it either.")
                                    print("The plush dragon is just sorta there as decoration or something...")
                                    print("At least you get to say you've found a secret?")
                                    Fin = "Y"
                            else:
                                    C = (C - 1)
                                    print("You moved west, which is left!")
                                    Fin = "Y"
            elif Move in ["E", "e"]:
                    while Fin != "Y":
                            if grid[R][East] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[R][East] == 2:
                                    C = (C + 1)
                                    print("You moved east, which is right!")
                                    Fin = "Y"
                            elif grid[R][East] == 3:
                                    C = (C + 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
                            elif grid[R][East] == 5:
                                    print("You encountered a big plush dragon!")
                                    print("It did nothing because it does nothing.")
                                    print("You can't do anything about it either.")
                                    print("The plush dragon is just sorta there as decoration or something...")
                                    print("At least you get to say you've found a secret?")
                                    Fin = "Y"
                            else:
                                    C = (C + 1)
                                    print("You moved east, which is right!")
                                    Fin = "Y"
            else:
                    print("Only N, S, E, or W!")
    LVL = (LVL + 1)
    if LVL <= 3:
        print("Great job! Onto the next level!")
    else:
        LOOP = "False"
        break
print("Wait, that's all the levels! Good job!!! You've completed the maze game!")
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
1.4.3: made the game completable"""
