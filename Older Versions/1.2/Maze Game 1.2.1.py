"""
Name : Jason
Program : Maze Game
Filename : Maze Game.py
Date : 2018/09/10
Version : 1.2.1
"""
# planning map
"""
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
# E = End
https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
"""
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
                    [0, 1, 1, 1, 1, 0, 1, 0],  # 7
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
            print("  ^^^^^^^^^  ")
            print("< Level Two >")
            print("  vvvvvvvvv  ")
            GAME = "False"
        else:
            GAME = "False"
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
                            elif View1[A] == 1:
                                    View[0][A] = "░"
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
                    A = int(0)
                    while E != 4:
                            if View2[A] == 0:
                                    View[1][A] = "█"
                                    A = int(A + 1)
                                    E = int(E + 1)
                            elif View2[A] == 1:
                                    View[1][A] = "░"
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
                    A = int(0)
                    while F != 4:
                            if View3[A] == 0:
                                    View[2][A] = "█"
                                    A = int(A + 1)
                                    F = int(F + 1)
                            elif View3[A] == 1:
                                    View[2][A] = "░"
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

                    MAP = "Y"
            print("\n <<[MAP]>> ")
            print("     ^     ")
            print("  ---N---  ")
            print(" | {0}{1}{2} | ".format(View[0][0], View[0][1], View[0][2]))
            print("<W {0}{1}{2} E>".format(View[1][0], View[1][1], View[1][2]))
            print(" | {0}{1}{2} | ".format(View[2][0], View[2][1], View[2][2]))
            print("  ^^^S^^^  ")
            print("     v     ")
            Fin = "N"
            Move = input("Which way do you like to go? ")
            if Move in ["N", "n"]:
                    while Fin != "Y":
                            if grid[North][C] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[North][C] == 1:
                                    R = (R - 1)
                                    print("You moved north, which is up!")
                                    Fin = "Y"
                            elif grid[North][C] == 2:
                                    R = (R - 1)
                                    print("You moved north, which is up!")
                                    Fin = "Y"
                            else:  # grid[North][C] == 3
                                    R = (R - 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
            elif Move in ["S", "s"]:
                    while Fin != "Y":
                            if grid[South][C] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[South][C] == 1:
                                    R = (R + 1)
                                    print("You moved south, which is down!")
                                    Fin = "Y"
                            elif grid[South][C] == 2:
                                    R = (R + 1)
                                    print("You moved south, which is down!")
                                    Fin = "Y"
                            else:  # grid[South][C] == 3
                                    R = (R + 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
            elif Move in ["W", "w"]:
                    while Fin != "Y":
                            if grid[R][West] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[R][West] == 1:
                                    C = (C - 1)
                                    print("You moved west, which is left!")
                                    Fin = "Y"
                            elif grid[R][West] == 2:
                                    C = (C - 1)
                                    print("You moved west, which is left!")
                                    Fin = "Y"
                            else:  # grid[R][West] == 3
                                    C = (C - 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
            elif Move in ["E", "e"]:
                    while Fin != "Y":
                            if grid[R][East] == 0:
                                    print("That's a wall! No matter how hard you try, you just can't phase through it!")
                                    Fin = "Y"
                            elif grid[R][East] == 1:
                                    C = (C + 1)
                                    print("You moved east, which is right!")
                                    Fin = "Y"
                            elif grid[R][East] == 2:
                                    C = (C + 1)
                                    print("You moved east, which is right!")
                                    Fin = "Y"
                            else:  # grid[R][East] == 3
                                    C = (C + 1)
                                    print("You finished the maze!")
                                    Fin = "Y"
            else:
                    print("Only N, S, E, or W!")
    print("Great job! Onto the next level!")
    LVL = (LVL + 1)
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
1.2.1: Added Final thoughts and Version details"""
