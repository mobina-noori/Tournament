import math
def devideNplay(teams):
    length = len(teams)
    printPlaying(teams, length)
    if length/2 > 1:
        subGroupA = teams[0:int(math.floor(length/2))]
        subGroupB = teams[int(math.floor(length/2)):length]
        devideNplay(subGroupA)
        devideNplay(subGroupB)
def printPlaying(teams , length):
    teamA = teams[0:int(math.floor(length/2))]
    teamB = teams[int(math.floor(length/2)):length]
    for offset in range(int(math.floor(length/2))):
        for i in range(int(math.floor(length/2))):
            print(f'Team {teamA[i]} - Team {teamB[((i + offset) % (math.floor(length/2)))]}')

def main():
    number = int(input("please enter the number of teams in shape of 2^n: "))
    teams = [0 for i in range(number)]
    for i in range(number):
        teams[i] = i+1
    devideNplay(teams)
main()
