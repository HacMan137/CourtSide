#!/usr/bin/python3
import CourtSide
def calculateOffense(finder,team,opponent):
    #Get necessary statistics
    twoPoints = (float(finder.getPointsFrom2Pointers(team)) + float(finder.getOppPointsFrom2Pointers(opponent))) / 2
    threePoints = (float(finder.getPointsFrom3Pointers(team)) + float(finder.getOppPointsFrom3Pointers(opponent))) / 2
    twoPointPercent = twoPoints / (twoPoints+threePoints)
    threePointPercent = threePoints / (twoPoints+threePoints)

    points = (twoPoints * 2) + (threePoints * 3)
    shotValue = (2 * twoPointPercent) + (3 * threePointPercent)


    shotPercent = ((float(finder.getShootingPercent(team)) + float(finder.getOppShootingPercent(opponent))) / 2) / 100
    shotValue = shotValue * shotPercent

    #assistMargin: -1 * (avg assists - (avg assists + avg assists allowed) / 2)
    #Will be negative if team should expect fewer assists than normal, positive if more
    assistMargin = -1 * (finder.getAssists(team) - ((finder.getAssists(team) + finder.getOppAssists(opponent)) / 2))
    turnoverMargin = -1 * (finder.getTurnovers(team) - ((finder.getTurnovers(team) + finder.getOppTurnovers(opponent)) / 2))
    FTpercent = (finder.getFTPercent(team)) / 100
    FTattemptMargin = -1 * (finder.getFTAttempted(team) - (finder.getFTAttempted(team) + finder.getOppFTAttempted(opponent)) / 2)
    oppBlocksMargin = -1 * (finder.getBlocks(opponent) - ((finder.getBlocks(opponent) + finder.getOppBlocks(team)) / 2))
    oppStealsMargin = -1 * (finder.getSteals(opponent) - ((finder.getSteals(opponent) + finder.getOppSteals(team)) / 2))
    oppFoulsMargin = -1 * (finder.getFoulsPerGame(opponent) + ((finder.getFoulsPerGame(opponent) + finder.getOppFouls(team)) / 2))
    #Make calculations to estimate scoring
    points += (assistMargin * shotValue) #Increase or decrease score based on how many more/less assists predicted
    points += (FTattemptMargin * FTpercent)
    points += (turnoverMargin * shotValue)
    points += (oppBlocksMargin * shotValue)
    points += (oppStealsMargin * shotValue)
    points += (oppFoulsMargin * shotValue)


    return points


