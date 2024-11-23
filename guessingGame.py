
import random

num = random.randint(0,100)
print("Guess the random number between 0 to 100:\nPress Q to quit.")
count=1

#scoring system based on attempts
#       0-1 = 5*
#       2-5 = 4*
#       5-10= 3* 
#       10-15= 2*
#       15+  = 1*


def score(count):
    if count in [0,1]:
        print("Score: *****/5")
    elif 2 <= count < 5:
        print("Score: ****/5")
    elif 5 <= count < 10:
        print("Score: ***/5")
    elif 10 <= count < 15:
        print("Score: **/5")
    else:
        print("Score: */5")



while True:
    
    userInp = input("Input: ")
    count= count+1

    if userInp.lower() == 'q':
        print("Quitten")
        break

    userInp = int(userInp)

    if userInp > num:

        if userInp-num<10:
            print("Go lower, but you are close.")

        else:
            print("Go lower.")


    elif userInp < num:

        if num-userInp<10:
            print("Go higher, but you are close.")

        else:
            print("Go higher.")

    else:
        print(f"Correct! You guessed the number in {count} attempts.")
        score(count)
        break
        




   

