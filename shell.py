import os, disk, core
from termcolor import cprint


def game_end():
    print('\n\n')
    cprint('''              .-=========-.
              \\'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \\|   /|\   |/
               \\__ '`' __/
                 _`) (`_
               _/_______\\_
              /___________\\''', 'green')


def print_welcome():
    cprint('                           _ajjaa  \n'
           '                          _Q???4Qf    ', 'green')
    print('       ', end="")
    cprint('_,...,_', 'yellow', attrs=['blink'], end="")
    cprint('            ) a/]QQb     ', 'green')
    print('     ', end="")
    cprint('.\'@/~~~\@\'.', 'yellow', attrs=['blink'], end="")
    cprint('              jQQba     ', 'green')
    print('   ', end="")
    cprint('//~~\___/~~\\\\', 'yellow', attrs=['blink'], end="")
    cprint('          _, .?QQ#[ _  \'', 'green')
    print('   ', end="")
    cprint('|@\__/@@@\__/@|', 'yellow', attrs=['blink'], end="")
    cprint('         ]m _.7   "asLaas_a/ ', 'green')
    print('   ', end="")
    cprint('|@/  \@@@/  \@|', 'yellow', attrs=['blink'], end="")
    cprint('        , ,\\J#L -!4Wba        ', 'green')
    print('   ', end="")
    cprint('\\\\__/~~~\__//', 'yellow', attrs=['blink'], end="")
    cprint('       [aL[    \\    \\jmm     jP  ', 'green')
    print("     ", end="")
    cprint("'.@\___/@.'", 'yellow', attrs=['blink'], end="")
    cprint("  	 ,b#'\"[     \\jmmmmm    _P.  ", 'green')
    print('       ', end="")
    cprint('`"""""`', 'yellow', attrs=['blink'], end="")
    cprint('        a##\'      "4P#mmm\#   _ya \n'
           '                     _P          !4####m  ?]aa/  \n'
           '                    /\'        aaJ#U###m#   4QP\' \n'
           '                   \'         aa,/4!44! \'     \n'
           '               jf         _\'jQQQQyb7b /     \n'
           '               \'.         \'.QQQQ4QQPb  )?    \n'
           '                            QQQ\'QQP?\'  jg/ f \n'
           '                          _yQP\']QQb aa  \n'
           '     SEAN\'S             a#W?\'..QQQQ?)?   ?\'\n'
           '      AWESOME          "##\'  _jQQP\'    \n'
           '   SOCCER             .j?  [ jQQ\'  \n'
           '      GAME       aJ  jmaaX#L???   \n'
           '                 ? am\'         \n'
           '               _QjQQQ/ \n'
           '               )QQQP?   \n'
           '                4QQQ/ ', 'green')
    cprint('        PRESS ENTER TO JOIN THE FUN!        ',
           'yellow',
           attrs=['blink', 'reverse'])


def main():
    os.system('clear')
    print_welcome()
    input()
    os.system('clear')
    goalie = disk.get_goalie()
    game = core.Game(
        core.Player(
            input('Player 1 Name: ').title(),
            input('Player 1 Team: ').title()), core.Player(
                input('Player 2 Name: ').title(),
                input('Player 2 Name: ').title()), 5, core.Ball())
    while game.keep_playing():
        os.system('clear')
        cprint(
            '{} PRESS ENTER TO SHOOT'.format(game.p1.name.upper()).center(69),
            'yellow',
            attrs=['blink', 'reverse'])
        print(game)
        print(goalie, end="")
        input()
        score = game.p1.score
        game.ball.position = game.p1.shoot()
        cprint(game.ball, attrs=['bold'])
        if score < game.p1.score:
            cprint('{} SCORES!'.format(game.p1.name.upper()).center(69, ' '),
                   'green')
        else:
            cprint('{} misses...'.format(game.p1.name).center(69, ' '), 'red')
        input('press enter to continue')

        os.system('clear')
        cprint(
            '{} PRESS ENTER TO SHOOT'.format(game.p2.name.upper()).center(69),
            'yellow',
            attrs=['blink', 'bold'])
        print(game)
        print(goalie, end="")
        input()
        score = game.p2.score
        game.ball.position = game.p2.shoot()
        cprint(game.ball, attrs=['bold'])
        if score < game.p2.score:
            cprint('{} SCORES!'.format(game.p2.name.upper()).center(69, ' '),
                   'green')
        else:
            cprint('{} misses...'.format(game.p2.name).center(69, ' '), 'red')
        input('press enter to continue')
        game.round += 1

    os.system('clear')
    game_end()
    cprint('{} WINS THE GAME!'.format(game.winner().upper()).center(41, ' '),
           'green',
           attrs=['blink', 'reverse'])


if __name__ == '__main__':
    main()
