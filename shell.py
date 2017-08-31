import os
from termcolor import cprint


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
    print_welcome()
    input()
    os.system('clear')


if __name__ == '__main__':
    main()
