#!/usr/bin/python3
import CourtSide
import sys
import algorithms.alg8 as alg

if(len(sys.argv)<2):
    print("Usage: %s <match up file>" % (sys.argv[0]))
    sys.exit(0)

def main():
    print("-----BRACKETOLOGY ANSWER KEY-----\n\n")
    finder = CourtSide.NCAAMBB()
    fName = sys.argv[1]
    print("Parsing Matchup file....")
    #Parse through matchups file
    try:
        matchFile = open(fName,"r")
        matchUps = []
        for line in matchFile.readlines():
            line = line.replace("\n","")
            if(len(matchUps)<1):
                matchUps.append([line])
            else:
                if(len(matchUps[-1])<2):
                    matchUps[-1].append(line)
                else:
                    matchUps.append([line])
    except:
        return -1
    print("Matchup file parse successful.")
    if(len(matchUps[-1])<2):
        print("Last matchup is not full!")
        return -2

    #Check to see if we can't find a certain team
    print("Checking teams...")
    for matchUp in matchUps:
        for team in matchUp:
            result = (finder.getPPG(team))
            failed = False
            if(result==None):
                print("Couldn't Find Team %s" % (team))
                failed = True
        if(failed==True):
            return -3
    print("All teams are valid.")
    print("Calculating Winners...\n\n")
    winFile = open("winners.txt","w")
    for matchUp in matchUps:
        print("Matchup: %s VS %s" % (matchUp[0],matchUp[1]))
        score1 = alg.calculateOffense(finder,matchUp[0],matchUp[1])
        score2 = alg.calculateOffense(finder,matchUp[1],matchUp[0])
        print("Score: %s: %s\t%s: %s" % (matchUp[0],score1,matchUp[1],score2))
        if(score1>score2):
            print("----%s wins" % (matchUp[0]))
            winFile.write("%s\n" % (matchUp[0]))
        else:
            print("----%s wins" % (matchUp[1]))
            winFile.write("%s\n" % (matchUp[1]))
    winFile.close()

    return 0
      
main()
