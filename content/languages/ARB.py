from content.languages.tutorial import tutorial_ENG as tutorial
diction = {'Choose action' : 'Choose an action',
           'Number of digits' : 'Number of Digits:',
           'Settings' : ' |\n11. Settings',
           'SettingsA' : ['11', 'Settings'],
           'Help' : ['12', 'Help'],
           'InputError' : 'Wrong Number Entered: input not in action list',
           'MathError' : 'Math Error: Unable to solve',
           'ChooseLanguage' : '\nChoose a language:\n |',
           'ListEnd' : ' |____________ empty = EXIT\n',
           'ExitList' : ['', 'EMPTY', 'EXIT'],
           'Analisys' : ['Parity:', 'Sum of digits of a number:',
                         'Number divisors:','Is the square of a number:',
                         'Is the cube of a number:', ' Properties:'],
           'LangSet' : '\nLanguage set:',
           'Restart' : 'Restart the program',
           'DivisorLimitBreak' : 'Breaking: Reached Divisor Limit',
           'DivisorWarning' : ['Type "?div" to see all the divisors (', ' found)'],
           'CtrlC Break' : 'Press Ctrl+C to break',
           'HelpList' : [['1', 'Tutorial']]
           }

actions = {'Summation' : ['Summation', '+', '1'],
           'Subtraction' : ['Subtraction', '-', '2'],
           'Multiplication' : ['Multiplication', '*', '3'],
           'Division' : ['Division', '/', '4'],
           'Integer Division' : ['Integer Division', '//', '5'],
           'Remainder' : ['Remainder', '%', '6'],
           'Exponentiation' : ['Exponentiation', '**', '7'],
           'Root' : ['Root', '^/', '8', '**/'],
           'Conversion to decimal number system' : ['Conversion to decimal number system', '>>|', '9'],
           'Detailed Analysis' : ['Detailed Analysis', '?', '10']}

sactions = {'Language' : ['Language', '1', [['ENG', '1'], ['RUS', '2'], ['ARB', '3']]],
            'Divisor Limit' : ['Divisor Limit', '2', ['Enter new Divisor Limit:']],
            'Reset Installation' : ['Reset Installation', '3']}
