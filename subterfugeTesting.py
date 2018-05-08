import math

drillerP1 = input("How many drillers does your sub have?\n")
# drillersP2 = input("How many drillers does your enemy have at the point?\n")
# shields = input("How many shields do they have\n")

ifSentry = int(math.floor(input("How many sentrys do they have?\n")))

if ifSentry > 0:

    x = input("How many hours will the sub be in the sentry?\n")
    x = int(math.floor(x / 2)) * ifSentry
    #Trigger once because you always get shot the moment you enter the sentrys range
    for i in range(ifSentry):
        drillerP1 = drillerP1 - math.ceil(drillerP1 * 0.05)

    # Trigger loop
    for i in range(x):
        drillerP1 = drillerP1 - math.ceil(drillerP1 * 0.05)
    print(drillerP1)