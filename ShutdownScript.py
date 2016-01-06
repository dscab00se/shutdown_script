#! python3
import time
import os


shutdownTime = input ("In how many minutes would you like to shut down the PC?  ")
time.sleep (.5)
print()
print()

shutdownSeconds = int(shutdownTime) * 60

print ("The computer will shut dowin in " + str(shutdownTime) + " minutes")
print()
print()

systemDown = ('shutdown -f -s -t %d' % int(shutdownSeconds))
cancelDown = ('shutdown -a')

os.system(systemDown)
print("Type \'cancel\' to stop shutdown or enter to continue")

stop = input()

if stop == str('cancel'):
    os.system(cancelDown)
    print()
    input('Press any key to contine...')
else:
    print()
    input('Press any key to exit')
    

               
