print('''Welcome to Treasure Island!
Your mission is to find the Scooby Snacks and feed Lucy!''')

print('''
                            __
     ,                    ," e`--o
    ((                   (  | __,'
     \\~----------------' \\_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
''')

left_or_right = input("Which way do you want to go? Left or Right? (left/right): ").lower()

if left_or_right == "left":
    lake = input("Good decision! But now there's a big lake in front of you. Do you want to swim or build a raft? (Swim/Raft): ").lower()

    if lake == "raft":
        chest = input("You did it! In front of you are two chests. Which one do you choose? First or Second? (First/Second): ").lower()

        if chest == "first":
            print("You picked the right one! Inside were the Scooby Snacks!!")
            print('''
    '------._.------'\\
     \\_______________\\
     .'|            .'|
   .'_____________.' .|
   |              |   |
   |  Scooby _.-. | . |
   |  *     (_.-' |   |
   |    Snacks    |  .|
   | *          * |  .'
   |______________|.'

Now Lucy is happy!!!!
''')

        else:
            print("You picked the wrong one. Lucy is sad. Game Over.")

    else:
        print("You made a wrong decision and got eat by a shark. Lucy is sad. Game Over.")
        print('''
                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._)  
''')

else:
    print("You picked the wrong one. Lucy is sad. Game Over.")