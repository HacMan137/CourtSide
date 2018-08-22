import urllib.request
import re

class NCAAMBB():
    def __init__(self):
        self.baseurl = "https://www.teamrankings.com/ncaa-basketball/stat/"

    def searchTeam(self,team):
        pass

    def makeRequest(self,url,team,year=""):
        try:
            url = self.baseurl + url
            if(len(year)>3):
                url+="?date="+year+"-04-04"
            response = urllib.request.urlopen(url)
            data = response.read()
            datalines = data.split(b"\n")
            for i in range(len(datalines)-1):
                if(b"\"" + team.encode() + b"\"" in datalines[i]):
                    stat = datalines[i+1].decode()
                    stat.replace("\t","")
                    final = re.search(">\-*\+*[0-9]*\.*[0-9]*\%*",stat)
                    return (final.group(0)[1:])
        except:
            return -1

    def getPPG(self,team,year=""):
        try:
            return self.makeRequest("points-per-game",team,year)
        except:
            return -1

    def getScoringMargin(self,team,year=""):
        try:
            return self.makeRequest("average-scoring-margin",team,year)
        except:
            return -1

    def getOffEfficiency(self,team,year=""):
        try:
            return self.makeRequest("offensive-efficiency",team,year)
        except:
            return -1

    def getFloorPercentage(self,team,year=""):
        try:
            return self.makeRequest("floor-percentage",team,year)
        except:
            return -1

    def getFirstHalfPPG(self,team,year=""):
        try:
            return self.makeRequest("1st-half-points-per-game",team,year)
        except:
            return -1

    def getSecondHalfPPG(self,team,year=""):
        try:
            return self.makeRequest("2nd-half-points-per-game",team,year)
        except:
            return -1

    def getOTPPG(self,team,year=""):
        try:
            return self.makeRequest("overtime-points-per-game",team,year)
        except:
            return -1

    def getAverageFirstHalfMargin(self,team,year=""):
        try:
            return self.makeRequest("average-1st-half-margin",team,year)
        except:
            return -1

    def getAverageSecondHalfMargin(self,team,year=""):
        try:
            return self.makeRequest("average-2nd-half-margin",team,year)
        except:
            return -1

    def getAverageOTMargin(self,team,year=""):
        try:
            return self.makeRequest("average-overtime-margin",team,year)
        except:
            return -1

    def getPointsFrom2Pointers(self,team,year=""):
        try:
            return self.makeRequest("points-from-2-pointers",team,year)
        except:
            return -1

    def getPointsFrom3Pointers(self,team,year=""):
        try:
            return self.makeRequest("points-from-3-pointers",team,year)
        except:
            return -1

    def getPercentOfPointsFrom2Pointers(self,team,year=""):
        try:
            return self.makeRequest("percent-of-points-from-2-pointers",team,year)
        except:
            return -1

    def getPercentOfPointsFrom3Pointers(self,team,year=""):
        try:
            return self.makeRequest("percent-of-points-from-3-pointers",team,year)
        except:
            return -1

    def getPercentOfPointsFromFT(self,team,year=""):
        try:
            return self.makeRequest("percent-of-points-from-free-throws",team,year)
        except:
            return -1

    def getShootingPercent(self,team,year=""):
        try:
            return self.makeRequest("shooting-pct",team,year)
        except:
            return -1

    def getEffectiveFieldGoalPercent(self,team,year=""):
        try:
            return self.makeRequest("effective-field-goal-pct",team,year)
        except:
            return -1

    def get3PointPercent(self,team,year=""):
        try:
            return self.makeRequest("three-point-pct",team,year)
        except:
            return -1

    def get2PointPercent(self,team,year=""):
        try:
            return self.makeRequest("two-point-pct",team,year)
        except:
            return -1

    def getFTPercent(self,team,year=""):
        try:
            return self.makeRequest("free-throw-pct",team,year)
        except:
            return -1

    def getTrueShootingPercent(self,team,year=""):
        try:
            return self.makeRequest("true-shooting-percentage",team,year)
        except:
            return -1

    def getFieldGoalsMade(self,team,year=""):
        try:
            return self.makeRequest("field-goals-made-per-game",team,year)
        except:
            return -1

    def getFieldGoalsAttempted(self,team,year=""):
        try:
            return self.makeRequest("field-goals-attempted-per-game",team,year)
        except:
            return -1

    def get3PointersMade(self,team,year=""):
        try:
            return self.makeRequest("three-pointers-made-per-game",team,year)
        except:
            return -1

    def get3PointersAttempted(self,team,year=""):
        try:
            return self.makeRequest("three-pointers-attempted-per-game",team,year)
        except:
            return -1

    def getFTMade(self,team,year=""):
        try:
            return self.makeRequest("free-throws-made-per-game",team,year)
        except:
            return -1

    def getFTAttempted(self,team,year=""):
        try:
            return self.makeRequest("free-throws-attempted-per-game",team,year)
        except:
            return -1

    def get3PointRate(self,team,year=""):
        try:
            return self.makeRequest("three-point-rate",team,year)
        except:
            return -1

    def get2PointRate(self,team,year=""):
        try:
            return self.makeRequest("two-point-rate",team,year)
        except:
            return -1

    def getFTAttemptedPerFGAttempted(self,team,year=""):
        try:
            return self.makeRequest("fta-per-fga",team,year)
        except:
            return -1

    def getFTPer100(self,team,year=""):
        try:
            return self.makeRequest("ftm-per-100-possessions",team,year)
        except:
            return -1

    def getFTAttemptedPerOffPlay(self,team,year=""):
        try:
            return self.makeRequest("free-throw-rate",team,year)
        except:
            return -1

    def getNonBlocked2PointPercent(self,team,year=""):
        try:
            return self.makeRequest("non-blocked-2-pt-pct",team,year)
        except:
            return -1

    def getOffRebounds(self,team,year=""):
        try:
            return self.makeRequest("offensive-rebounds-per-game",team,year)
        except:
            return -1

    def getDefRebounds(self,team,year=""):
        try:
            return self.makeRequest("defensive-rebounds-per-game",team,year)
        except:
            return -1

    def getTeamRebounds(self,team,year=""):
        try:
            return self.makeRequest("team-rebounds-per-game",team,year)
        except:
            return -1

    def getTotalRebounds(self,team,year=""):
        try:
            return self.makeRequest("total-rebounds-per-game",team,year)
        except:
            return -1

    def getOffReboundPercent(self,team,year=""):
        try:
            return self.makeRequest("offensive-rebounding-pct",team,year)
        except:
            return -1

    def getDefReboundPercent(self,team,year=""):
        try:
            return self.makeRequest("defensive-rebounding-pct",team,year)
        except:
            return -1

    def getTotalReboundPercent(self,team,year=""):
        try:
            return self.makeRequest("total-rebounding-percentage",team,year)
        except:
            return -1

    def getBlocks(self,team,year=""):
        try:
            return self.makeRequest("blocks-per-game",team,year)
        except:
            return -1

    def getSteals(self,team,year=""):
        try:
            return self.makeRequest("steals-per-game",team,year)
        except:
            return -1

    def getBlockPercent(self,team,year=""):
        try:
            return self.makeRequest("block-pct",team,year)
        except:
            return -1

    def getStealsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("steals-perpossession",team,year)
        except:
            return -1

    def getStealsPerDefPlay(self,team,year=""):
        try:
            return self.makeRequest("steal-pct",team,year)
        except:
            return -1

    def getAssists(self,team,year=""):
        try:
            return self.makeRequest("assists-per-game",team,year)
        except:
            return -1

    def getTurnovers(self,team,year=""):
        try:
            return self.makeRequest("turnovers-per-game",team,year)
        except:
            return -1

    def getTurnoversPerPossession(self,team,year=""):
        try:
            return self.makeRequest("turnovers-per-possession",team,year)
        except:
            return -1

    def getAssistTurnoverRatio(self,team,year=""):
        try:
            return self.makeRequest("assist--per--turnover-ratio",team,year)
        except:
            return -1

    def getAssistsPerFGM(self,team,year=""):
        #Assists per Field Goals Made
        try:
            return self.makeRequest("assists-per-fgm",team,year)
        except:
            return -1

    def getAssistsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("assists-per-possession",team,year)
        except:
            return -1

    def getTurnoversPerOffPlay(self,team,year=""):
        try:
            return self.makeRequest("turnover-pct",team,year)
        except:
            return -1

    def getFoulsPerGame(self,team,year=""):
        try:
            return self.makeRequest("personal-fouls-per-game",team,year)
        except:
            return -1

    def getFoulsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("personal-fouls-per-possession",team,year)
        except:
            return -1

    def getFoulsPerDefPlay(self,team,year=""):
        try:
            return self.makeRequest("personal-foul-pct",team,year)
        except:
            return -1

    def getOppPPG(self,team,year=""):
        try:
            return self.makeRequest("opponent-points-per-game",team,year)
        except:
            return -1

    def getOppScoringMargin(self,team,year=""):
        try:
            return self.makeRequest("opponent-average-scoring-margin",team,year)
        except:
            return -1

    def getDefensiveEfficiency(self,team,year=""):
        try:
            return self.makeRequest("defensive-efficiency",team,year)
        except:
            return -1

    def getOppFloorPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-floor-percentage",team,year)
        except:
            return -1

    def getOppFirstHalfPPG(self,team,year=""):
        try:
            return self.makeRequest("opponent-1st-half-points-per-game",team,year)
        except:
            return -1

    def getOppSecondHalfPPG(self,team,year=""):
        try:
            return self.makeRequest("opponent-2nd-half-points-per-game",team,year)
        except:
            return -1

    def getOppOTPPG(self,team,year=""):
        try:
            return self.makeRequest("opponent-overtime-points-per-game",team,year)
        except:
            return -1

    def getOppPointsFrom2Pointers(self,team,year=""):
        try:
            return self.makeRequest("opponent-points-from-2-pointers",team,year)
        except:
            return -1

    def getOppPointsFrom3Pointers(self,team,year=""):
        try:
            return self.makeRequest("opponent-points-from-3-pointers",team,year)
        except:
            return -1

    def getOpp2PointPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-percent-of-points-from-2-pointers",team,year)
        except:
            return -1

    def getOpp3PointPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-percent-of-points-from-3-pointers",team,year)
        except:
            return -1

    def getOppFTPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-percent-of-points-from-free-throws",team,year)
        except:
            return -1

    def getOppShootingPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-shooting-pct",team,year)
        except:
            return -1

    def getOppEffectiveFGPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-effective-field-goal-pct",team,year)
        except:
            return -1

    def getOpp3PointPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-three-point-pct",team,year)
        except:
            return -1

    def getOpp2PointPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-two-point-pct",team,year)
        except:
            return -1

    def getOppFTPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-free-throw-pct",team,year)
        except:
            return -1

    def getOppTrueShootingPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-true-shooting-percentage",team,year)
        except:
            return -1

    def getOppFieldGoalsMade(self,team,year=""):
        try:
            return self.makeRequest("opponent-field-goals-made-per-game",team,year)
        except:
            return -1

    def getOppFieldGoalsAttempted(self,team,year=""):
        try:
            return self.makeRequest("opponent-field-goals-attempted-per-game",team,year)
        except:
            return -1

    def getOpp3PointersMade(self,team,year=""):
        try:
            return self.makeRequest("opponent-three-pointers-made-per-game",team,year)
        except:
            return -1

    def getOpp3PointersAttempted(self,team,year=""):
        try:
            return self.makeRequest("opponent-three-pointers-attempted-per-game",team,year)
        except:
            return -1

    def getOppFTMade(self,team,year=""):
        try:
            return self.makeRequest("opponent-free-throws-made-per-game",team,year)
        except:
            return -1

    def getOppFTAttempted(self,team,year=""):
        try:
            return self.makeRequest("opponent-free-throws-attempted-per-game",team,year)
        except:
            return -1

    def getOpp3PointRate(self,team,year=""):
        try:
            return self.makeRequest("opponent-three-point-rate",team,year)
        except:
            return -1

    def getOpp2PointRate(self,team,year=""):
        try:
            return self.makeRequest("opponent-two-point-rate",team,year)
        except:
            return -1

    def getOppFTAttemptedPerFGAttempted(self,team,year=""):
        try:
            return self.makeRequest("opponent-fta-per-fga",team,year)
        except:
            return -1

    def getOppFTPer100(self,team,year=""):
        try:
            return self.makeRequest("opponent-ftm-per-100-possessions",team,year)
        except:
            return -1

    def getOppFTAttemptedPerOffPlay(self,team,year=""):
        try:
            return self.makeRequest("opponent-free-throw-rate",team,year)
        except:
            return -1

    def getOppNonBlocked2PointPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-non-blocked-2-pt-pct",team,year)
        except:
            return -1

    def getOppOffRebounds(self,team,year=""):
        try:
            return self.makeRequest("opponent-offensive-rebounds-per-game",team,year)
        except:
            return -1

    def getOppDefRebounds(self,team,year=""):
        try:
            return self.makeRequest("opponent-defensive-rebounds-per-game",team,year)
        except:
            return -1

    def getOppTeamRebounds(self,team,year=""):
        try:
            return self.makeRequest("opponent-team-rebounds-per-game",team,year)
        except:
            return -1

    def getOppTotalRebounds(self,team,year=""):
        try:
            return self.makeRequest("opponent-total-rebounds-per-game",team,year)
        except:
            return -1

    def getOppOffReboundPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-offensive-rebounding-pct",team,year)
        except:
            return -1

    def getOppDefReboundPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-defensive-rebounding-pct",team,year)
        except:
            return -1

    def getOppBlocks(self,team,year=""):
        try:
            return self.makeRequest("opponent-blocks-per-game",team,year)
        except:
            return -1

    def getOppSteals(self,team,year=""):
        try:
            return self.makeRequest("opponent-steals-per-game",team,year)
        except:
            return -1

    def getOppBlockPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-block-pct",team,year)
        except:
            return -1

    def getOppStealsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("opponent-steals-perpossession",team,year)
        except:
            return -1

    def getOppStealsPerDefPlay(self,team,year=""):
        try:
            return self.makeRequest("opponent-steal-pct",team,year)
        except:
            return -1

    def getOppAssists(self,team,year=""):
        try:
            return self.makeRequest("opponent-assists-per-game",team,year)
        except:
            return -1

    def getOppTurnovers(self,team,year=""):
        try:
            return self.makeRequest("opponent-turnovers-per-game",team,year)
        except:
            return -1

    def getOppAssistTurnoverRatio(self,team,year=""):
        try:
            return self.makeRequest("opponent-assist--per--turnover-ratio",team,year)
        except:
            return -1

    def getOppAssistsPerFGM(self,team,year=""):
        try:
            return self.makeRequest("opponent-assists-per-fgm",team,year)
        except:
            return -1

    def getOppAssistsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("opponent-assists-per-possession",team,year)
        except:
            return -1

    def getOppTurnoversPerPossession(self,team,year=""):
        try:
            return self.makeRequest("opponent-turnovers-per-possession",team,year)
        except:
            return -1

    def getOppTurnoversPerOffPlay(self,team,year=""):
        try:
            return self.makeRequest("opponent-turnover-pct",team,year)
        except:
            return -1

    def getOppFouls(self,team,year=""):
        try:
            return self.makeRequest("opponent-personal-fouls-per-game",team,year)
        except:
            return -1

    def getOppFoulsPerPossession(self,team,year=""):
        try:
            return self.makeRequest("opponent-personal-fouls-per-possession",team,year)
        except:
            return -1

    def getOppFoulsPerDefPlay(self,team,year=""):
        try:
            return self.makeRequest("opponent-personal-foul-pct",team,year)
        except:
            return -1

    def getGamesPlayed(self,team,year=""):
        try:
            return self.makeRequest("games-played",team,year)
        except:
            return -1

    def getPossessions(self,team,year=""):
        try:
            return self.makeRequest("possessions-per-game",team,year)
        except:
            return -1

    def getExtraChances(self,team,year=""):
        try:
            return self.makeRequest("extra-chances-per-game",team,year)
        except:
            return -1

    def getEffectivePossessionRatio(self,team,year=""):
        try:
            return self.makeRequest("effective-possession-ratio",team,year)
        except:
            return -1

    def getOppEffectivePossessionRatio(self,team,year=""):
        try:
            return self.makeRequest("opponent-effective-possession-ratio",team,year)
        except:
            return -1

    def getWinPercent(self,team,year=""):
        try:
            return self.makeRequest("win-pct-all-games",team,year)
        except:
            return -1

    def getCloseWinPercent(self,team,year=""):
        try:
            return self.makeRequest("win-pct-close-games",team,year)
        except:
            return -1

    def getOppWinPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-win-pct-all-games",team,year)
        except:
            return -1

    def getOppCloseWinPercent(self,team,year=""):
        try:
            return self.makeRequest("opponent-win-pct-close-games",team,year)
        except:
            return -1

        
        
##myFinder = NCAAMBB()
##print(myFinder.getOppCloseWinPercent("Michigan St","2018"))
