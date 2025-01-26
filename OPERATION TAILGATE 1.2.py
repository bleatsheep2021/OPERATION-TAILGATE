import random
import time


class Submarine:
    def __init__(self, distance: int, noise: int, hull: int, data: int):
        self.distance = distance
        self.noise = noise
        self.hull = hull
        self.data = data


# loading screen is too long
# 1.2




    # Define a failure method for consistent quit messages
    def fail(self, reason: str):
        print(reason)
        quit("FAIL")

    def close_in(self) -> None:
        self.distance = max(0, self.distance - 50)
        if self.distance < 1:
            self.fail("Hold on! We're about to collide!\n")

    def back_off(self) -> None:
        self.distance += 50
        if self.distance > 1500:
            self.fail("Captain, We've lost the sub.")

    def repair(self) -> None:
        self.noise = max(1, self.noise + random.randint(1, 3))
        self.hull = min(100, self.hull + random.randint(5, 30))
        if self.noise > 9:
            self.fail("We've been spotted! The enemy has detected us!")

    def ignore(self) -> None:
        self.hull = max(0, self.hull - random.randint(1, 20))
        if self.hull <= 1:
            self.fail("Catastrophic failure. Hull integrity is compromised!")

    def shut_down(self) -> None:
        self.noise = max(1, self.noise - random.randint(1, 3))
        self.distance += random.randint(300, 700)
        if self.distance > 1500:
            self.fail("Captain, We've lost the sub.")

    def record_information(self) -> None:
        if self.distance <= 150:
            print("We're collecting info now...")
            time.sleep(1)
            print("Recording...")
            time.sleep(1)
            print("Recording... We need more data...")
            time.sleep(1)
            print("Got It! Data collected.\n")
            self.data += random.randint(1, 3)
            if self.data > 9:  # Win condition
                print(
                    "Well done, we have collected enough information on the audio signature for SOSUS to identify the sub!")
                print("WIN")
                quit()
        else:
            print("We're too far away to gather any data on the sub.")

    def continue_as_normal(self):
        print("We're continuing as normal... but stay alert. This is a dangerous mission.\n")

    def crazy_ivan(self) -> None:
        self.distance -= random.randint(100, 200)
        print("Crazy Ivan maneuver! The enemy has made a sudden, sharp turn!\n")
        if self.noise > 5:
            self.fail("They've spotted us! They know we're here!")
        if self.distance < 1:
            quit("FAIL")

    def stop(self) -> None:
        self.distance -= 100
        print("Stop! They've shut down all engines... they're trying to lose us!\n")
        if self.distance < 1:
            self.fail("Hold on! We're about to collide with the enemy sub!")

    # Define placeholders for enemy actions
    def placeholder1(self):
        print("They haven't noticed us yet... Let's keep it that way.")

    def placeholder2(self):
        print("They're continuing on course. This is our chance to get closer.")

    def placeholder3(self):
        print("Watch out, they might pull a Crazy Ivan at any moment!")

    def placeholder4(self):
        print("They're still going straight... we must stay hidden.")

    def placeholder5(self) -> None:
        print("Be careful, they're slowing down... this might be a trap!")
        self.distance -= random.randint(20, 75)
        if self.distance < 1:
            self.fail("Hold on! We're about to collide!")

    def speedup(self) -> None:
        print("They're speeding up! They're trying to get away!\n")
        self.distance += random.randint(20, 75)
        if self.distance > 1500:
            self.fail("Captain, We've lost the sub.")

    # Define problem events
    def fire(self) -> None:
        action = input("Captain, the engine just caught fire! We need to act fast. Do we attempt to repair the damage (3), or ignore it and hope it doesn't spread (5)?\n")
        if action == '3':
            print("Damage control teams are rushing to the engine room...\n")
            time.sleep(1)
            print("The fire is fierce! We need to cool down the system fast...\n")
            self.hull -= random.randint(5, 25)  # Hull damage from fire
            self.noise += random.randint(1, 5)  # Increased noise
            print("Fire under control, but the hull is damaged. Noise levels are up. We’re in a precarious position.\n")
        elif action == '5':
            print("Ignoring the fire... it's a risky move.\n")
            time.sleep(1)
            print("The fire spreads... It's out of control!\n")
            if random.choice([True, False]):
                self.fail("The fire is raging! The sub's integrity is compromised! Evacuate now!")
            else:
                print("The fire is contained... but the hull is severely damaged. We're losing pressure.\n")
                self.hull -= random.randint(10, 50)
        else:
            print("Invalid input! Choose 3 to repair or 5 to ignore.\n")

    def diveplane(self) -> None:
        action = input("Captain, a dive plane is stuck! We must make a choice. Do we repair it (3), or ignore it and risk going down (5)?\n")
        if action == '3':
            print("Sending divers to fix the plane... pressure is building...\n")
            self.noise += random.randint(1, 5)
            self.distance += random.randint(200, 500)
            print("The dive plane seems functional again... but we're at risk!\n")
        elif action == '5':
            print("Ignoring the issue... we might lose control at any moment.\n")
            if random.choice([True, False]):
                self.fail("The dive plane has failed! We're descending uncontrollably!")
            else:
                print("The plane seems to have held... but it could fail again at any time.\n")
        else:
            print("Invalid input! Choose 3 to repair or 5 to ignore.\n")

    def radleak(self) -> None:
        action = input("Radiation detected! What should we do? Seal the doors (3) or ignore it and hope it doesn't spread (5)?\n")
        self.hull -= random.randint(12,27)
        if action == '3':
            print("Sealing the doors... the radiation is contained for now.\n")
            self.noise += random.randint (1,3)
        elif action == '5':
            print("Ignoring the radiation leak... it's spreading...\n")
            if random.choice([True, False, False, False]):
                self.fail("Radiation levels critical! Evacuate now before it's too late!")
            else:
                print("Radiation has spread... we're not out of danger yet.\n")
        else:
            print("Invalid input! Choose 3 to seal the doors or 5 to ignore.\n")

    def missiledoors(self) -> None:
        action = input("Enemy missile doors are open! Should we fire a torpedo (3), or hope it’s just a test (5)?\n")
        if action == '3':
            print("Launching torpedoes... this could be the end for us!\n")
            self.fail("Missile launch detected! We’re under attack!")
        elif action == '5':
            print("Hoping it’s just a test... but we must stay alert!\n")
            if random.choice([False] * 9 + [True]):
                self.fail("Missile launch detected! Brace for impact!")
            else:
                print("False alarm! The missile doors are closing.\n")
        else:
            print("Invalid input! Choose 3 to fire or 5 to ignore.\n")

    def depthdown(self) -> None:
        action = input("Enemy sub is descending quickly! Should we descend (3), or hold our depth (5)?\n")
        if action == '3':
            print("Descending quickly to avoid detection...\n")
            self.fail("Hull breaches detected during rapid descent! We're going down!")
        elif action == '5':
            print("Holding our depth... but they could crush us if we’re not careful.\n")
            if random.choice([True, False]):
                self.fail("Hull leaks detected! We’re losing control!")
            else:
                print("We’ve managed to hold our depth for now.\n")
        else:
            print("Invalid input! Choose 3 to descend or 5 to hold depth.\n")

    def display_hud(self):
        time.sleep(3)
        print("\n---------------------------------------------------------------------------------------------------------------------")
        print(f"Distance to Target: {self.distance} | Noise Level: {self.noise} | Hull Integrity: {self.hull}% | Audio Signature data: {self.data}")

    def canyonrun(self) -> None:
        action = input("Captain, navigation reports a trench below us. Should we risk it for better data (3) or continue on our path (5)?\n")
        if action == '3':
            print("Descending into the trench...\n")
            crash = random.randint(1, 3)
            if crash == 1:
                print("Descending to 876m...\n")
                time.sleep(1)
                print("100m below max depth...\n")
                time.sleep(1)
                print("Leak in the torpedo room...\n")
                time.sleep(1)
                print("Torpedo room is flooding! Hull breach imminent!\n")
                time.sleep(1)
                self.fail("EMERGENCY SURFACE! Hull breach detected!")
            else:
                print("We’re deep beneath the Soviet sub now!\n")
                time.sleep(1)
                print("Collecting audio... there are leaks in several rooms!\n")
                time.sleep(1)
                self.data += random.randint(2, 5)
                self.hull -= random.randint(1, 3)  # Hull degrades due to pressure
                self.noise += 1  # Increased noise due to depth
                self.display_hud()
        elif action == '5':
            print("Continuing as usual...\n")
        else:
            print("Invalid input! Enter 3 to risk it or 5 to continue.\n")


#from SUB import Submarine

Sub = Submarine(200, 0, 100, 0)




enemy_turn = 0
problem = 0
turn = 50



time.sleep(2)
print("O")




time.sleep(0.3)
print("P")
time.sleep(0.3)
print("E")
time.sleep(0.3)
print("R")
time.sleep(0.3)
print("A")
time.sleep(0.3)
print("T")
time.sleep(0.3)
print("I")
time.sleep(0.3)
print("O")
time.sleep(0.3)
print("N ")
time.sleep(0.6)
print("\nT")
time.sleep(0.3)
print("A")
time.sleep(0.3)
print("I")
time.sleep(0.3)
print("L")
time.sleep(0.3)
print("G")
time.sleep(0.3)
print("A")
time.sleep(0.3)
print("T")
time.sleep(0.3)
print("E")
time.sleep(1)
print("\n\nOperation Tailgate\nBy Oscar Craw\nVersion 1.2")
time.sleep(5)


print("Welcome aboard SSN 661 Lapon, Captain. We’ve spotted a Yankee class submarine.")
time.sleep(2)
print("Your mission: Stalk and gather 10 data points on its audio signature.\n")
time.sleep(2)
rules = input("Would you like to view the rules (this menu will not show again)\n1(yes)\nAny other key(no)\n")

if rules == "1":
    print("\nYour options each turn:")
    print("1: Close in (Decrease distance by 50m)")
    print("2: Back off (Increase distance by 50m)")
    print("3: Repair (Increase hull but increase noise)")
    print("4: Record audio signature (Within 150m)")
    print("5: Shut down engines (Reduce noise but drift away)")

    time.sleep(6)

    print("\nEnemy actions may include:")
    print("1: Speed up (Increase distance)")
    print("2: Slow down (Decrease distance)")
    print("3: Crazy Ivan (Decreases distance)")

    time.sleep(6)

    print("\nGame rules:")
    print("- Avoid detection (Noise over 9 = fail).")
    print("- Don’t collide with the enemy (Distance under 1 = fail).")
    print("- Don’t lose track of the enemy (Distance over 1500 = fail).")
    print("- You have 50 turns to gather enough data or you lose.")

    time.sleep(6)





    print("Sometime they will also speed up. This will increases distance by a random number inbetween 20-75.\n")

    print("Also they sometimes execute a 'Crazy Ivan', this is when they make a hard turn to check if any subs (you) are following them. This will reduce distance by around 100-200m. Also if your noise is greater than 5 you will be detected.\n")

    print("You will be detected (Lose) if you noise is over 9 at any time. Also if your distance is lower than 1 you will crash in to the enemy, and if your distance is higher than 1500 you lose the enemy sub and the game ends.\n")

    print("And finally, if you run out of turns (you start with 50) you lose.\n"
          "")

    time.sleep(6)

print("PRESS ENTER TO START")
input()
print("-----------------------------------------------------------------------------------------------------------------")
while True:



    enemy_turn = random.randint(1,16)
    problem = random.randint(1,32)
    bonus = random.randint(1,30)

    Sub.display_hud()
    print(turn,"turns left\n")
    action = input("What would you like to do?\nClose in (1)\nBack off(2)\nRepair(3)\nContinue as normal (enter any letter)\nRecord the audio signature (4)\nOr Shut down?(5)\n").lower()

    if (action == "1"):
        print("Ok, were closing in!\n")
        Sub.close_in()
        turn = turn - 1

    elif (action == "2"):
        print("Ok, were backing off a bit.\n")
        Sub.back_off()
        turn = turn - 1

    elif (action == "3"):
        print("Ok, I'll tell the chief engineer.\n")
        Sub.repair()
        turn = turn - 1

    elif (action == "4"):
        Sub.record_information()
        turn = turn - 1

    elif (action == "5"):
        print("Shutting down all engines now!\n")
        Sub.shut_down()
        turn = turn - 1

    else:
        Sub.continue_as_normal()
        turn = turn - 1

    time.sleep(1)

    if enemy_turn == 1:
        Sub.crazy_ivan()

    elif enemy_turn == 2:
        Sub.speedup()

    elif enemy_turn == 3:
        Sub.placeholder1()

    elif enemy_turn == 4:
        Sub.placeholder2()

    elif enemy_turn == 5:
        Sub.placeholder3()

    elif enemy_turn == 6:
        Sub.placeholder4()

    elif enemy_turn == 7:
        Sub.placeholder5()

    elif enemy_turn == 8:
        Sub.speedup()

    elif enemy_turn == 9:
        Sub.placeholder1()

    elif enemy_turn == 10:
        Sub.placeholder2()

    elif enemy_turn == 11:
        Sub.placeholder3()

    elif enemy_turn == 12:
        Sub.placeholder4()

    elif enemy_turn == 13:
        Sub.placeholder5()

    elif enemy_turn == 14:
        Sub.stop()

    elif enemy_turn == 15:
        Sub.placeholder5()

    elif enemy_turn == 16:
        Sub.speedup()

    if problem == 1:
        Sub.diveplane()

    elif problem == 3:
        Sub.fire()

    elif problem == 4:
        Sub.fire()

    elif problem == 5:
        Sub.radleak()

    elif problem == 7:
        Sub.missiledoors()

    elif problem == 10:
        Sub.depthdown()

    if bonus == 1:
        Sub.canyonrun()

    if Sub.hull < 20:  # adjust threshold as needed
        quit("Warning: Hull Integrity at Critical Level!")