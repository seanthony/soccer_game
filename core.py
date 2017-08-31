from random import randint


class Game:
    ''' game class for the soccer shoot out '''

    def __init__(self, player_one, player_two, turns, ball):
        '''(Player, Player, int) -> '''
        self.p1 = player_one
        self.p2 = player_two
        self.turns = turns
        self.round = 1
        self.ball = ball

    def keep_playing(self):
        ''' return true if the game should continue '''
        return not (abs(self.p1.score - self.p2.score) >
                    (self.turns - self.round))

    def __str__(self):
        r = 'ROUND: {}'.format(str(self.round))
        if self.round > self.turns:
            r = 'OVERTIME'
        return '{} {}\n{} {}\n{} {}\n{}'.format(
            self.p1.team.center(34, ' '), self.p2.team.center(34, ' '),
            str(self.p1.score).center(34, ' '),
            str(self.p2.score).center(34, ' '), self.p1.name.center(34, ' '),
            self.p2.name.center(34, ' '), r.center(69, '-'))

    def winner(self):
        if self.p1.score > self.p2.score:
            return self.p1.name
        else:
            return self.p2.name


class Player:
    ''' player class '''

    def __init__(self, name, team):
        ''' str, str -> '''
        self.name = name
        self.team = team
        self.score = 0

    def shoot(self):
        shot = randint(0, 63)
        if (shot >= 8 and shot <= 15) or (shot == 29) or (shot >= 45 and
                                                          shot <= 58):
            self.score += 1
        return shot


class Ball:
    ''' ball class'''

    def __init__(self):
        self.position = 0

    def __str__(self):
        s = self.position * ' '
        return '{} /\_/\\\n{}(-<_>-)\n{} \\/_\\/'.format(s, s, s)
