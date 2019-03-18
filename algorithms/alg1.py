#!/usr/bin/python3
import CourtSide
def calculateOffense(finder,team,opponent):
    #Get necessary statistics
    points = 0
    points = (float(finder.getFirstHalfPPG(team)) + float(finder.getOppFirstHalfPPG(opponent))) / 2
    points += (float(finder.getSecondHalfPPG(team)) + float(finder.getOppFirstHalfPPG(opponent))) / 2
    twoPoints = (float(finder.getPointsFrom2Pointers(team)) + float(finder.getOppPointsFrom2Pointers(opponent))) / 2
    threePoints = (float(finder.getPointsFrom3Pointers(team)) + float(finder.getOppPointsFrom3Pointers(opponent))) / 2
    twoPointPercent = twoPoints / (twoPoints+threePoints)
    threePointPercent = threePoints / (twoPoints+threePoints)

    shotPercent = ((float(finder.getShootingPercent(team)) + float(finder.getOppShootingPercent(opponent))) / 2) / 100

    assists = (float(finder.getAssists(team)) + float(finder.getOppAssists(opponent))) / 2
    turnovers = (float(finder.getTurnovers(team)) + float(finder.getOppTurnovers(opponent))) / 2
    FTpercent = float(finder.getFTPercent(team)) / 100
    FTattempt = float(finder.getFTAttempted(team))
    oppBlocks = float(finder.getBlocks(opponent))
    oppSteals = float(finder.getSteals(opponent))
    oppFouls = float(finder.getOppFouls(opponent))
    #Make calculations to estimate scoring

    #Reduce estimated scoring based on how many blocks the opponent typically has
    points = points - ((oppBlocks * ((2 * twoPointPercent) + (3 * threePointPercent))) * shotPercent)
    #Reduce estimated scoring based on how many steals the opponent typically has
    points = points - ((oppSteals * ((2 * twoPointPercent) + (3 * threePointPercent))) * shotPercent)
    #Reduce estimated scoring based on how many turnovers the team typically has
    points = points - ((turnovers * ((2 * twoPointPercent) + (3 * threePointPercent))) * shotPercent)
    
    #Increase estimated scoring based on how many turnovers the team typically has
    points = points + (assists * ((2 * twoPointPercent) + (3 * threePointPercent)))
    #Increase estimated scoring based on how many FT the team typically has, and how often they are typically fouled.
    points = points + ((FTattempt+oppFouls) * FTpercent)

    return points


