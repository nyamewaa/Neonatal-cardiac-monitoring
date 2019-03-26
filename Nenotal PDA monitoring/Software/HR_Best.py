# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:26:39 2015

@author: Moseph
"""
import HR_LCD as LCD
screen = LCD.Screen(bit_mode = 4, cursor_status= 'on')
screen.clear
import Adafruit_BBIO.GPIO as GPIO
from time import time, sleep
import HR_Monitor as HRM

#screen.on()

# screen.printLine('Hi Cloud9 this s',1) # used to test LCD screen
# screen.printLine('Moss your ruler!',2)

GPIO.setup("P8_11", GPIO.IN) # SW1 OK
GPIO.setup("P8_9", GPIO.IN) # SW2 Down
GPIO.setup("P8_7", GPIO.IN) # SW3 Left
GPIO.setup("P8_15", GPIO.IN) # SW4 Up
GPIO.setup("P8_17", GPIO.IN) # SW5 Right
GPIO.setup("P8_8", GPIO.IN) # SW6 Menu

# Welcome Screen

screen.printLine(' WELCOME TO THE ',1)
screen.printLine('  BEST MONITOR  ',2)
sleep(5)

# Whats your sex Screen

screen.clear
screen.printLine('Whats your sex?',1)
screen.printLine('>MALE     FEMALE',2)
UserSex='Male' # User's input sex (being initialized)
while True:
    Right=GPIO.input("P8_17") # Right button
    Left=GPIO.input("P8_7") # Left button
    OK=GPIO.input("P8_11") # OK button
    if Right==1: # Right button is pressed
        screen.clear
        screen.printLine('Whats your sex?',1)
        screen.printLine(' MALE    >FEMALE',2)
        UserSex='Female'
        sleep(.5)
    elif Left==1: # Left button is pressed
        screen.clear
        screen.printLine('Whats your sex?',1)
        screen.printLine('>MALE     FEMALE',2)
        UserSex='Male'
        sleep(.5)
    elif OK==1: # OK button is pressed to move to next screen/loop
        break
    else: # final condition of while loop is always pass to maintain loop without user input
        pass
    
# Whats your age Screen

sleep(1)
screen.clear
screen.printLine('Whats your age?',1)
screen.printLine('      >20 21 22',2)
agecounter=1 # counnter whose value determines what to display on LCD
UserAge=20 # User's input age (being initialized)
while True:
    Right=GPIO.input("P8_17") # Right button
    Left=GPIO.input("P8_7") # Left button
    OK=GPIO.input("P8_11") # OK button
    if Right==1: # Right button is pressed
        agecounter+=1
        UserAge=agecounter + 19
        if agecounter > 30:
            agecounter = 30
        else:
            agecounter = agecounter
        if UserAge == 20:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine("      >%i %i %i" % (UserAge, UserAge + 1, UserAge + 2),2)
        elif UserAge == 21:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine("    %i>%i %i %i" % (UserAge - 1, UserAge, UserAge + 1, UserAge + 2),2)
        elif UserAge == 48:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i %i   " % (UserAge - 2, UserAge - 1, UserAge, UserAge + 1),2)
        elif UserAge == 49:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i      " % (UserAge - 2, UserAge - 1, UserAge),2)
        else:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i %i %i" % (UserAge - 2, UserAge - 1, UserAge, UserAge + 1, UserAge + 2),2)
        #print agecounter # for debugging purposes
        sleep(.5)
    elif Left==1: # Left button is pressed
        agecounter-=1
        UserAge=agecounter + 19
        if agecounter < 1:
            agecounter = 1
        else:
            agecounter = agecounter
        if UserAge == 20:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine("      >%i %i %i" % (UserAge, UserAge + 1, UserAge + 2),2)
        elif UserAge == 21:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine("    %i>%i %i %i" % (UserAge - 1, UserAge, UserAge + 1, UserAge + 2),2)
        elif UserAge == 48:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i %i   " % (UserAge - 2, UserAge - 1, UserAge, UserAge + 1),2)
        elif UserAge == 49:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i      " % (UserAge - 2, UserAge - 1, UserAge),2)
        else:
            screen.clear
            screen.printLine('Whats your age?',1)
            screen.printLine(" %i %i>%i %i %i" % (UserAge - 2, UserAge - 1, UserAge, UserAge + 1, UserAge + 2),2)
        #print agecounter # for debugging purposes
        sleep(.5)
    elif OK==1: # OK button is pressed to move to next screen/loop
        break
    else:
        pass

# Describe your fitness Screen

sleep(1)
screen.clear
screen.printLine('  Describe Your ',1)
screen.printLine('  Fitness Level ',2)
fitcounter=2
sleep(3)
screen.clear
screen.printLine('  Fitness Level ',1)
screen.printLine(' >Hi Lvl Athlete',2)

UserFitness='High Level Athlete' # User's input fitness level (being initialized)
while True:
    OK=GPIO.input("P8_11") # OK button
    Down=GPIO.input("P8_9") # Down button
    Up=GPIO.input("P8_15") # Up button
    if Down==1: # Down button is pressed
        fitcounter+=1
        #print fitcounter # for debugging purposes
        if fitcounter <= 2:
            fitcounter=2
            screen.clear
            screen.printLine('  Fitness Level ',1)
            screen.printLine(' >Hi Lvl Athlete',2)
            UserFitness='High Level Athlete'
        elif fitcounter == 3:
            screen.clear
            screen.printLine('  Hi Lvl Athlete',1)
            screen.printLine(' >Relatively Fit',2)
            UserFitness='Relatively Fit'
        else:
            fitcounter=4
            screen.clear
            screen.printLine('  Relatively Fit',1)
            screen.printLine(' >Couch Potato  ',2)
            UserFitness='Couch Potato'
        sleep(.5)
    elif Up==1: # Up button is pressed
        fitcounter-=1
        #print fitcounter # for debugging purposes
        if fitcounter <= 2:
            fitcounter=2
            screen.clear
            screen.printLine('  Fitness Level ',1)
            screen.printLine(' >Hi Lvl Athlete',2)
            UserFitness='High Level Athlete'
        elif fitcounter == 3:
            screen.clear
            screen.printLine('  Hi Lvl Athlete',1)
            screen.printLine(' >Relatively Fit',2)
            UserFitness='Relatively Fit'
        else:
            fitcounter=4
            screen.clear
            screen.printLine('  Relatively Fit',1)
            screen.printLine
            UserFitness='Couch Potato'
        sleep(.5)
    elif OK==1: # OK button pressed to move to next screen/loop
        break
    else:
        pass
    
# MAIN MENU Screnn

# print UserSex, UserAge, UserFitness # for debugging purposes

sleep(1)
screen.clear
screen.printLine(' * MAIN MENU *  ',1)
screen.printLine('  >How to Use   ',2)
menucounter=1 # counter whose value is usesd for scrolling through the menu screen
deviceOn=1 # keeps the program running and LCD screen on

while True:
    OK=GPIO.input("P8_11") # OK button
    Down=GPIO.input("P8_9") # Down button
    Up=GPIO.input("P8_15") # Up button
    if Down == 1: # whenever Down is pressed
        menucounter+=1
        #print menucounter # for debugging purposes
        if menucounter <= 1:
            screen.clear
            screen.printLine(' * MAIN MENU *  ',1)
            screen.printLine('  >How to Use   ',2)
        elif menucounter == 2:
            screen.clear
            screen.printLine('   How to Use   ',1)
            screen.printLine(' >Live Monitor  ',2)
        elif menucounter == 3:
            screen.clear
            screen.printLine('  Live Monitor  ',1)
            screen.printLine('>Target HR Zone ',2)
        elif menucounter == 4:
            screen.clear
            screen.printLine(' Target HR Zone ',1)
            screen.printLine('    >FiTrivia   ',2)
        elif menucounter == 5:
            screen.clear
            screen.printLine('     FiTrivia    ',1)
            screen.printLine('     >Credits    ',2)
        else:
            menucounter=6
            screen.clear
            screen.printLine('      Credits    ',1)
            screen.printLine('     >Log Off    ',2)
        sleep(.5)
    elif Up == 1: # whenever Up is pressed
        menucounter-=1
        #print menucounter # for debugging purposes
        if menucounter <= 1:
            screen.clear
            screen.printLine(' * MAIN MENU *  ',1)
            screen.printLine('  >How to Use   ',2)
        elif menucounter == 2:
            screen.clear
            screen.printLine('   How to Use   ',1)
            screen.printLine(' >Live Monitor  ',2)
        elif menucounter == 3:
            screen.clear
            screen.printLine('  Live Monitor  ',1)
            screen.printLine('>Target HR Zone ',2)
        elif menucounter == 4:
            screen.clear
            screen.printLine(' Target HR Zone ',1)
            screen.printLine('    >FiTrivia   ',2)
        elif menucounter == 5:
            screen.clear
            screen.printLine('     FiTrivia    ',1)
            screen.printLine('     >Credits    ',2)
        else:
            menucounter=6
            screen.clear
            screen.printLine('      Credits    ',1)
            screen.printLine('     >Log Off    ',2)
        sleep(.5)
        
    elif OK == 1 and menucounter == 1: # for How to Use option
        screen.clear
        screen.printLine('   * BASICS *   ',1)
        screen.printLine('This is a simple',2)
        usecounter=0 # for scrolling through the text
        while True:
            Menu=GPIO.input("P8_8") # Menu button
            Down=GPIO.input("P8_9") # Down button
            Up=GPIO.input("P8_15") # Up button
            if Menu == 1:
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                menucounter=1
                sleep(.5)
                break
            elif Down == 1: # Down button pressed
                usecounter+=1
                if usecounter <= 0:
                    usecounter = 1
                if usecounter >= 48:
                    usecounter = 48
                UseOnLCD1, UseOnLCD2 = HRM.HowToUse(usecounter)
                screen.clear
                screen.printLine(UseOnLCD1,1)
                screen.printLine(UseOnLCD2,2)
                sleep(.5)
            elif Up == 1: # Up button is pressed
                usecounter-=1
                if usecounter <= 0:
                    usecounter = 1
                if usecounter >= 48:
                    usecounter = 48
                UseOnLCD1, UseOnLCD2 = HRM.HowToUse(usecounter)
                screen.clear
                screen.printLine(UseOnLCD1,1)
                screen.printLine(UseOnLCD2,2)
                sleep(.5)
            else:
                pass
            
    elif OK == 1 and menucounter == 2: # for Live Monitor option
        sleep(.5)
        screen.clear
        screen.printLine(' PLEASE CONNECT ',1)
        screen.printLine('   LEADS NOW!   ',2)
        sleep(3)
        UserRHR = HRM.findsafeRHR(UserSex, UserFitness)
        THRZoneLow, THRZoneHi, UserMaxHR, forLCD=HRM.findTHRZone(UserAge)
        screen.clear
        screen.printLine('Choose duration:',1)
        screen.printLine('>Continuous 10s ',2)
        hrmcounter=1 # counter for scrolling through the time duration options
        break1=0 # variable for breaking out of below loop, thus returning to main menu loop if =1
        while True:
            OK=GPIO.input("P8_11") # OK button
            Right=GPIO.input("P8_17") # Right button
            Left=GPIO.input("P8_7") # Left button
            Menu=GPIO.input("P8_8") # Menu button
            if Right == 1: # Right button pressed
                hrmcounter+=1
                if hrmcounter <= 1:
                    hrmcounter=1
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('>Continuous  10s',2)
                elif hrmcounter == 2:
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('inuous >10s  30s',2)
                elif hrmcounter == 3:
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('s  10s >30s  60s',2)
                else:
                    hrmcounter=4
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('10s  30s >60s   ',2)
                sleep(.5)
            elif Left == 1:
                hrmcounter-=1
                if hrmcounter <= 1:
                    hrmcounter=1
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('>Continuous  10s',2)
                elif hrmcounter == 2:
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('inuous >10s  30s',2)
                elif hrmcounter == 3:
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('s  10s >30s  60s',2)
                else:
                    hrmcounter=4
                    screen.clear
                    screen.printLine('Choose duration:',1)
                    screen.printLine('10s  30s >60s   ',2)
                sleep(.5)
            elif OK == 1 and hrmcounter == 1: # Continuous option chosem
                sleep(.5)
                screen.clear
                screen.printLine('Workout Mode On?',1)
                screen.printLine(' >Yes       No  ',2)
                break1=0
                break2=0 # variable for breaking out of below loop, thus returning to main menu loop if =1
                workcounter=1
                while True:
                    Menu=GPIO.input("P8_8") # Menu button
                    Right=GPIO.input("P8_17") # Right button
                    Left=GPIO.input("P8_7") # Left button
                    OK=GPIO.input("P8_11") # OK button
                    if Right == 1: # Right button pressed
                        screen.clear
                        screen.printLine('Workout Mode On?',1)
                        screen.printLine('  Yes      >No  ',2)
                        workcounter=2
                        sleep(.5)
                    elif Left == 1: # Left button pressed
                        screen.clear
                        screen.printLine('Workout Mode On?',1)
                        screen.printLine(' >Yes       No  ',2)
                        workcounter=1
                        sleep(.5)
                    elif OK == 1 and workcounter == 1: # Yes Workout Mode selected
                        import Adafruit_BBIO.ADC as ADC # ADC pin setup
                        from numpy import zeros, float32, arange
                        ADC.setup()
                        kernel, kernel_size = HRM.definekernel() # define kernel
                        user_time = zeros(4709, dtype = float32) # initialize time array (sec)
                        user_volt = zeros(4709, dtype = float32) # initialize voltage array (mV)
                        screen.clear
                        screen.printLine(' *INITIALIZING* ',1)
                        screen.printLine('                ',2)
                        while True:
                            if Menu == 1: # Menu button pressed
                                break2=1
                                break
                            Menu=GPIO.input("P8_8") # Menu button
                            start1 = time()
                            for s in range(0,4709):
                                user_volt[s] = ADC.read_raw("P9_39") # read off of AIN0 to populate voltage array
                                sleep(.0007139)
                            stop1 = time()
                            elapse1 = (stop1 - start1) / 4709
                            user_time = arange(4709) * elapse1 # populate time array according to time elapsed
                            HR, HRforLCD = HRM.main(user_time, user_volt, kernel, kernel_size)
                            screen.clear
                            screen.printLine(HRforLCD,1)
                            screen.printLine('                ',2)
                            if HR <= UserRHR: # calculated heart rate is below user's calculated safe RHR
                                screen.printLine('WARNING: LOW HR!',2)
                            if HR > .9 * UserMaxHR: # calculated heart rate is greater than 90% of user's calculated max HR
                                screen.printLine('Your Overworking',2)
                            if HR > THRZoneLow and HR < THRZoneHi: # calculated heart rate is within target heart rate zone
                                from random import randrange
                                encourage = randrange(0,5,1)
                                if encourage == 0:
                                    screen.printLine('Keep it up!     ',2)
                                elif encourage == 1:
                                    screen.printLine('In target range!',2)
                                elif encourage == 2:
                                    screen.printLine('Looking good ;) ',2)
                                elif encourage == 3:
                                    screen.printLine('Great work ethic',2)
                                else:
                                    screen.printLine('Hats off,keep on',2)
                            if HR > UserRHR and HR <= 0.6 * UserMaxHR:
                                from random import randrange
                                encourage = randrange(0,3,1)
                                if encourage == 0:
                                    screen.printLine('Pick it Up!     ',2)
                                elif encourage == 1:
                                    screen.printLine('You can improve ',2)
                                elif encourage == 2:
                                    screen.printLine('Keep Pushing    ',2)
                            if Menu == 1:
                                break2=1
                                break
                            
                    elif OK == 1 and workcounter == 2: # No Workout Mode selected
                        import Adafruit_BBIO.ADC as ADC # ADC pin setup
                        from numpy import zeros, float32, arange
                        ADC.setup()
                        kernel, kernel_size = HRM.definekernel() # define kernel
                        user_time = zeros(4709, dtype = float32) # initialize time array (sec)
                        user_volt = zeros(4709, dtype = float32) # initialize voltage array (mV)
                        screen.clear
                        screen.printLine(' *INITIALIZING* ',1)
                        screen.printLine('                ',2)
                        while True:
                            if Menu == 1:
                                break2=1
                                break
                            Menu=GPIO.input("P8_8") # Menu button
                            start1 = time()
                            for s in range(0,4709):
                                user_volt[s] = ADC.read_raw("P9_39") # read off of AIN0 to populate voltage array
                                sleep(.0007139)
                            stop1 = time()
                            elapse1 = (stop1 - start1) / 4709
                            user_time = arange(4709) * elapse1 # populate time array according to time elapsed
                            HR, HRforLCD = HRM.main(user_time, user_volt, kernel, kernel_size)
                            screen.clear
                            screen.printLine(HRforLCD,1)
                            screen.printLine('                ',2)
                            if HR <= UserRHR:
                                screen.printLine('WARNING: LOW HR!',2)
                            if HR >= UserMaxHR:
                                screen.printLine('WARNING: MAX HR!',2)
                            if Menu == 1:
                                break2=1
                                break

                    elif Menu == 1 or break2 == 1: # Menu button pressed
                        break1=1
                        sleep(.5)
                        break
                    else:
                        pass
                    
            elif OK == 1 and hrmcounter == 2: # 10s option
                sleep(.5)
                import Adafruit_BBIO.ADC as ADC # ADC pin setup
                from numpy import zeros, float32, arange
                ADC.setup()
                kernel, kernel_size = HRM.definekernel() # define kernel
                user_time = zeros(4709, dtype = float32) # initialize time array (sec)
                user_volt = zeros(4709, dtype = float32) # initialize voltage array (mV)
                screen.clear
                screen.printLine(' *INITIALIZING* ',1)
                screen.printLine('                ',2)
                Menu=GPIO.input("P8_8") # Menu button
                start1 = time()
                for s in range(0,4709):
                    user_volt[s] = ADC.read_raw("P9_39") # read off of AIN0 to populate voltage array
                    sleep(.0007139)
                stop1 = time()
                elapse1 = (stop1 - start1) / 4709
                user_time = arange(4709) * elapse1 # populate time array according to time elapsed
                HR, HRforLCD = HRM.main(user_time, user_volt, kernel, kernel_size)
                screen.clear
                screen.printLine(HRforLCD,1)
                if HR < UserRHR:
                    screen.printLine('WARNING: LOW HR!',2)
                if HR > UserMaxHR:
                    screen.printLine('WARNING: MAX HR!',2)
                sleep(5)
                break1 = 1
                menucounter = 1
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                break

            elif OK == 1 and hrmcounter == 3: # 30s option
                sleep(.5)
                import Adafruit_BBIO.ADC as ADC # ADC pin setup
                from numpy import zeros, float32, arange
                ADC.setup()
                kernel, kernel_size = HRM.definekernel() # define kernel
                user_time = zeros(14127, dtype = float32) # initialize time array (sec)
                user_volt = zeros(14127, dtype = float32) # initialize voltage array (mV)
                screen.clear
                screen.printLine(' *INITIALIZING* ',1)
                screen.printLine('                ',2)
                Menu=GPIO.input("P8_8") # Menu button
                start1 = time()
                for s in range(0,14127):
                    user_volt[s] = ADC.read_raw("P9_39") # read off of AIN0 to populate voltage array
                    sleep(.0007139)
                stop1 = time()
                elapse1 = (stop1 - start1) / 14127
                user_time = arange(14127) * elapse1 # populate time array according to time elapsed
                HR, HRforLCD = HRM.main(user_time, user_volt, kernel, kernel_size)
                screen.clear
                screen.printLine(HRforLCD,1)
                if HR < UserRHR:
                    screen.printLine('WARNING: LOW HR!',2)
                if HR > UserMaxHR:
                    screen.printLine('WARNING: MAX HR!',2)
                sleep(5)
                break1 = 1
                menucounter = 1
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                break
            
            elif OK == 1 and hrmcounter == 4: # 60s option
                sleep(.5)
                import Adafruit_BBIO.ADC as ADC # ADC pin setup
                from numpy import zeros, float32, arange
                ADC.setup()
                kernel, kernel_size = HRM.definekernel() # define kernel
                user_time = zeros(28254, dtype = float32) # initialize time array (sec)
                user_volt = zeros(28254, dtype = float32) # initialize voltage array (mV)
                screen.clear
                screen.printLine(' *INITIALIZING* ',1)
                screen.printLine('                ',2)
                Menu=GPIO.input("P8_8") # Menu button
                start1 = time()
                for s in range(0,28254):
                    user_volt[s] = ADC.read_raw("P9_39") # read off of AIN0 to populate voltage array
                    sleep(.0007139)
                stop1 = time()
                elapse1 = (stop1 - start1) / 28254
                user_time = arange(28254) * elapse1 # populate time array according to time elapsed
                HR, HRforLCD = HRM.main(user_time, user_volt, kernel, kernel_size)
                screen.clear
                screen.printLine(HRforLCD,1)
                if HR < UserRHR:
                    screen.printLine('WARNING: LOW HR!',2)
                if HR > UserMaxHR:
                    screen.printLine('WARNING: MAX HR!',2)
                sleep(5)
                break1 = 1
                menucounter = 1
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                break
            
            elif Menu ==1 or break1 == 1: # this condition means Menu button was pressed
                sleep(.5)
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                menucounter=1
                break
            else:
                pass
            
    elif OK == 1 and menucounter == 3: # for Target HR Zone option
        THRZoneLow, THRZoneHi, MaxHR, forLCD=HRM.findTHRZone(UserAge)
        screen.clear
        screen.printLine(' Your Target HR ',1)
        screen.printLine(forLCD,2)
        # print forLCD # for debugging purposes
        
        while True:
            Menu=GPIO.input("P8_8")
            if Menu == 1: # Menu button pressed
                sleep(.5)
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                menucounter=1
                break
            else:
                pass
            
    elif OK == 1 and menucounter == 4: # for FiTrivia option
        screen.clear
        screen.printLine('Searching   www.',1)
        screen.printLine('google.com .....',2)
        from random import randrange
        sleep(1)
        FTnumber=randrange(0,3,1) # randomly generated number determining the fact shown
        screen.clear
        screen.printLine('google.com .....',1)
        screen.printLine('................',2)
        sleep(1)
        screen.clear
        screen.printLine('................',1)
        screen.printLine('................',2)
        sleep(3)
        if FTnumber == 0:
            screen.clear
            screen.printLine('Resting heart   ',1)
            screen.printLine('rate is a great ',2)
            sleep(.7)
            screen.clear
            screen.printLine('rate is a great ',1)
            screen.printLine('indicator of an ',2)
            sleep(.7)
            screen.clear
            screen.printLine('indicator of an ',1)
            screen.printLine('individuals fit-',2)
            sleep(.7)
            screen.clear
            screen.printLine('individuals fit-',1)
            screen.printLine('ness.           ',2)
            sleep(.7)
            screen.clear
            screen.printLine('ness.           ',1)
            screen.printLine('                ',2)
            sleep(.7)
            screen.clear
            screen.printLine(' * MAIN MENU *  ',1)
            screen.printLine('  >How to Use   ',2)
            menucounter=1
        if FTnumber == 1:
            screen.clear
            screen.printLine('Max heart rate  ',1)
            screen.printLine('declines with   ',2)
            sleep(.7)
            screen.clear
            screen.printLine('declines with   ',1)
            screen.printLine('age, independent',2)
            sleep(.7)
            screen.clear
            screen.printLine('age, independent',1)
            screen.printLine('of ones physical',2)
            sleep(.7)
            screen.clear
            screen.printLine('of ones physical',1)
            screen.printLine('fitness.        ',2)
            sleep(.7)
            screen.clear
            screen.printLine('fitness.        ',1)
            screen.printLine('                ',2)
            sleep(.7)
            screen.clear
            screen.printLine(' * MAIN MENU *  ',1)
            screen.printLine('  >How to Use   ',2)
            menucounter=1
        if FTnumber == 2:
            screen.clear
            screen.printLine('The fat burning ',1)
            screen.printLine('zone actually   ',2)
            sleep(.7)
            screen.clear
            screen.printLine('zone actually   ',1)
            screen.printLine('occurs at about ',2)
            sleep(.7)
            screen.clear
            screen.printLine('occurs at about ',1)
            screen.printLine('45 - 60% of max-',2)
            sleep(.7)
            screen.clear
            screen.printLine('45 - 60% of max-',1)
            screen.printLine('imum heart rate.',2)
            sleep(.7)
            screen.clear
            screen.printLine('imum heart rate.',1)
            screen.printLine('                ',2)
            sleep(.7)
            screen.clear
            screen.printLine(' * MAIN MENU *  ',1)
            screen.printLine('  >How to Use   ',2)
            menucounter=1
        
    elif OK == 1 and menucounter == 5: # for Credits option
        screen.clear
        screen.printLine('    CREATORS:   ',1)
        screen.printLine('Moss J.         ',2)
        sleep(1)
        screen.clear
        screen.printLine('Moss J.         ',1)
        screen.printLine('-Software Dev   ',2)
        sleep(.7)
        screen.clear
        screen.printLine('-Software Dev   ',1)
        screen.printLine('Mercy A.        ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Mercy A.        ',1)
        screen.printLine('-Hardware Dev   ',2)
        sleep(.7)
        screen.clear
        screen.printLine('-Hardware Dev   ',1)
        screen.printLine('Kate H. &       ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Kate H. &       ',1)
        screen.printLine('Siji O.         ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Siji O.         ',1)
        screen.printLine('-Enclosure Devs ',2)
        sleep(.7)
        screen.clear
        screen.printLine('-Enclosure Devs ',1)
        screen.printLine('SPECIAL THANKS  ',2)
        sleep(.7)
        screen.clear
        screen.printLine('SPECIAL THANKS  ',1)
        screen.printLine('TO FOLLOWING:   ',2)
        sleep(.7)
        screen.clear
        screen.printLine('TO FOLLOWING:   ',1)
        screen.printLine('Mark P.,MD      ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Mark P.,MD      ',1)
        screen.printLine('Nick B.         ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Nick B.         ',1)
        screen.printLine('Matt B.         ',2)
        sleep(.7)
        screen.clear
        screen.printLine('Matt B.         ',1)
        screen.printLine('                ',2)
        sleep(.7)
        screen.clear
        screen.printLine('                ',1)
        screen.printLine('                ',2)
        sleep(.3)
        screen.clear
        screen.printLine(' * MAIN MENU *  ',1)
        screen.printLine('  >How to Use   ',2)
        menucounter=1
        
    elif OK == 1 and menucounter == 6: # for Log Off option
        sleep(.5)
        screen.clear
        screen.printLine(' Are You Sure?  ',1)
        screen.printLine('  Yes       >No ',2)
        while True:
            OK=GPIO.input("P8_11") # OK button
            Right=GPIO.input("P8_17") # Right button
            Left=GPIO.input("P8_7") # Left button
            Menu=GPIO.input("P8_8") # Menu button
            if Right == 1: # Right button is pressed
                screen.clear
                screen.printLine(' Are You Sure?  ',1)
                screen.printLine('  Yes       >No ',2)
                deviceOn=1
                sleep(.5)
            elif Left == 1: # Left button is pressed
                screen.clear
                screen.printLine(' Are You Sure?  ',1)
                screen.printLine(' >Yes        No ',2)
                deviceOn=0
                sleep(.5)
            elif OK == 1 and deviceOn == 1: # OK button pressed while on No
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                menucounter=1
                sleep(.5)
                break
            elif Menu == 1: # Menu button pressed (does same as pressing OK on No)
                screen.clear
                screen.printLine(' * MAIN MENU *  ',1)
                screen.printLine('  >How to Use   ',2)
                menucounter=1
                deviceOn=1
                sleep(.5)
                break
            elif OK == 1 and deviceOn == 0: # OK button pressed while on Yes
                screen.clear
                screen.printLine(' Powering Down  ',1)
                screen.printLine('       3        ',2)
                sleep(.5)
                screen.clear
                screen.printLine('                ',1)
                screen.printLine('                ',2)
                sleep(.5)
                screen.clear
                screen.printLine(' Powering Down  ',1)
                screen.printLine('       2        ',2)
                sleep(.5)
                screen.clear
                screen.printLine('                ',1)
                screen.printLine('                ',2)
                sleep(.5)
                screen.clear
                screen.printLine(' Powering Down  ',1)
                screen.printLine('       1        ',2)
                sleep(.5)
                screen.clear
                screen.printLine('                ',1)
                screen.printLine('                ',2)
                sleep(.3)
                break
            else:
                pass
            
    elif deviceOn == 0:
        # print 'Done with UI!'
        break
    
    else:
        pass

sleep(1)
screen.clear # final screen clear to ensure nothing is being displayed on LCD upon ending program
#screen.off()