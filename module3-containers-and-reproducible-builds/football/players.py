'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name=None):
        self.name = name
        self.stats = {'td':0,}
        self.valid_stats = []
    
    def stat_update(self, **kwargs):
        for key, val in kwargs.items():
            if self.stat_valid(key):
                self.stats[key] = self.stats[key] + val

    def stat_valid(self, key):
        if key in self.valid_stats:
            return True
        return False

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None):
        super().__init__(name=name)

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
