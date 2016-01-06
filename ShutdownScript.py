#! python3
import time
import os

#ask's user for how many hours they would like the computer to continue to run
hour_Shutdown = input ("In how many hours would you like to shut down the PC?  ")
time.sleep (.5)
print()
print()

#the following takes the input from hour_Shut_Down and converts it to seconds
#for Windows CMD to take as an argument
shutdown_Sec = (float(hour_Shutdown) * 60) * 60

print ("The computer will shut dowin in " + str(hour_Shutdown) + " hours")
print()
print()

#the following 2 variables pass shutdown information to windows CMD
#using the shutdown_Sec var to determine the time of shutdown or to pass
#the cancel shutdown argument in CMD when asked
system_Down = ('shutdown -f -s -t %d' % int(shutdown_Sec))
cancel_Down = ('shutdown -a')

#telling windows to shutdown using the above function or to cancel upon having
#cancel typed by user.
os.system(system_Down)
print("Type \'cancel\' to stop shutdown or enter to continue")

#wating for user input
stop = input()

#if statment to have the computer either shutdown or cancel the shutdown process
if stop == str('cancel'):
    os.system(cancel_Down)
    print()
    input('Press any key to contine...')
else:
    print()
    input('Press any key to exit')
    

               
