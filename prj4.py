from pygame import mixer
import time
# a healthy programmer

"""we have to make functions for eye , exercise , and drink water"""

import time

from datetime import datetime


def eye():

    from pygame import mixer

    mixer.init()

    mixer.music.load("/home/moin/Downloads/Physical.mp3")

    mixer.music.play()

def exercise():

    from pygame import mixer

    mixer.init()

    mixer.music.load("/home/moin/Downloads/Physical.mp3")

    mixer.music.play()

def water():

    from pygame import mixer

    mixer.init()

    mixer.music.load("/home/moin/Downloads/drink water.mp3")

    mixer.music.play()

def getdate():

    import datetime

    return datetime.datetime.now()


if __name__ == "__main__":

    log = 20

    inp = input("enter your name : ")

    inp1 = input(f"ok {inp} , let's create some files , enter the name for exercise file : ")

    f = open(f"{inp1}","x")

    f.write("this is a file for exercise only.")

    f.close()
   # print(__name__)


    inp2 = input("enter the name for eye exercise file : ")

    f = open(f"{inp2}","x")

    f.write("this is a file for eye exercise only.")

    f.close()



    inp3 = input("enter the name for the water drinking : ")

    f = open(f"{inp3}","x")

    f.write("this is a file for drinking water.")



    while (log > 1):

        eye()    # time.sleep(5)
        inp4 = input("enter eye done to stop alaram")

        if inp4 == "ey done":

            from pygame import mixer

            mixer.init()

            mixer.music.load("/home/moin/Downloads/Physical.mp3")

            mixer.music.stop()

            f = open(f"{inp2}","w")

            f.write(f"{inp} has done the eye exercise at {getdate()}")

            f.close()

            log = log-1

        else:

            print(" enter a valid input! after 5 seconds. ")

        time.sleep(5)





        exercise()

        inp5 = input("time to do physical exercise , enter 'ex done' to stop the alarm : ")

        if inp5=="ex done":

            from pygame import mixer

            mixer.init()

            mixer.music.load("/home/moin/Downloads/Physical.mp3")

            mixer.music.stop()

            f = open(f"{inp1}","w")

            f.write(f"{inp} has done physical exercise at {getdate()}")

            f.close()

            log = log-1

        else:

            print(" enter a valid input! after 5 seconds. ")

        time.sleep(5)




                                       #water exercise
        water()

        inp6 = input("time to drink water , enter 'dw done' to stop the alarm : ")

        if inp6=="dw done":

            from pygame import mixer

            mixer.init()

            mixer.music.load("/home/moin/Downloads/drink water.mp3")

            mixer.music.stop()

            f = open(f"{inp3}","w")

            f.write(f"{inp} has dranked water at {getdate()}")

            f.close()

            log = log-1

        else:

            print(" enter a valid input! after 5 seconds. ")



