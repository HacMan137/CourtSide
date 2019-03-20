#!/usr/bin/python3
import CourtSide
def calculateOffense(finder,team,opponent):
    points = 0
    possessions = finder.getPossessions(team) #Total # of possessions
    valuedPossessions = 0 #Estimated number of possessions where a score may occur for the team
    threePointersAttempted = finder.get3PointersAttempted(team)
    FGAttempted = finder.getFieldGoalsAttempted(team)
    FGMade = finder.getFieldGoalsMade(team)
    threePointPercent = finder.get3PointPercent(team) / 100
    twoPointPercent = finder.getNonBlocked2PointPercent(team) / 100
    oRebounds = finder.getOffReboundPercent(team) / 100
    oppRebounds = finder.getDefReboundPercent(opponent) / 100
    oppStealsRate = finder.getStealsPerPossession(opponent) / 100
    oppBlockPercent = finder.getBlockPercent(opponent) / 100
    turnoverRate = finder.getTurnoversPerPossession(team) / 100

    #Estimate how many offensive and defensive rebounds will occur
    oReboundCount = possessions * oRebounds
    oppReboundCount = possessions * oppRebounds

    ##Estimate number of possessions based on rebounding
    possessions += oReboundCount

    ##Calculate valuedPossessions based on opponent's defensive stats
    valuedPossessions = possessions - (possessions * oppStealsRate) #Subtract possessions where a steal occurs
    valuedPossessions = valuedPossessions - ((possessions * oppBlockPercent) * oppRebounds) #Subtract possessions where a block occurs and that block is recovered by the defense
    valuedPossessions = valuedPossessions - (possessions * turnoverRate)

    #Estimated statistical value of taking a 2 and 3 point shot
    twoPointVal = (((FGAttempted/(FGAttempted+threePointersAttempted)) * valuedPossessions) * twoPointPercent) * 2
    threePointVal = (((threePointersAttempted/(FGAttempted+threePointersAttempted)) * valuedPossessions) * threePointPercent) * 3
    totalVal = twoPointVal + threePointVal
    ##Calculate average score increase from each valuedPossessions
    points += (totalVal)

    return points


