import math

drillerP1 = input("How many drillers does your sub have?\n")
# drillersP2 = input("How many drillers does your enemy have at the point?\n")
# shields = input("How many shields do they have\n")

ifSentry = input("How many sentrys do they have?\n")

if ifSentry > 0:

    x = input("How many hours will the sub be in the sentry?\n")

    for i in range(x):
        drillerP1 = drillerP1 - math.ceil(drillerP1 * 0.05)
    print(drillerP1)