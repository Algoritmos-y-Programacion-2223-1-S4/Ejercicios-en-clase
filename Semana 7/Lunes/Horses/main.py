from Horse import Horse
from Race import Race
from Valid import Valid

def main():
    valids = int(input("How many valids do you want:"))
    races = int(input("How many races do you want for each valid:"))
    horse1 =  Horse("El rayo veloz",1)
    horse2 =  Horse("Juan",2)
    horse3=  Horse("Federico",3)
    horse4 =  Horse("Tormenta",4)
    horse5 =  Horse("Leonardo",5)
    horse6 =  Horse("Bernardo",6)
    horse_list = [horse1,horse2,horse3,horse4,horse5,horse6]
    for valid in range(valids):
        race_list = []
        for race in range(races):
            race_object = Race(race,horse_list)
            race_list.append(race_object)
        for race in race_list:
            race.start_race()
            race.choose_winner()
        

main()