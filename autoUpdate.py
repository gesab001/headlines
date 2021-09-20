import time


def updateAuto(interval):
    while True:
        print("Printed immediately.")
        time.sleep(interval)
        print("Printed after " + str(interval) +" seconds.")

