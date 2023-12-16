'''
Rozhok Calc (console) v1.6
        by DaregonPL
'''
def main(): # just main. im not gonna describe that
    global br, diction, actions, debug, divise, \
           keyWordDict, tutorial, firststart, hideMenu
#                                   PRINTING POSSIBLE ACTIONS
    if (hideMenu == '1' and firststart) or (hideMenu == '0'):
        print('\n' + diction['Choose action'] + ':\n |')
        for x in actions:
            x = actions[x]
            print(x[2] + '. ' + x[0])
        print(diction['Settings'])
        print(diction['Help'][0] + '. ' + diction['Help'][1])
        print(diction['ListEnd'])
    firststart = False
#                                   WORK WITH INPUT(s)
    ans = input('|] ')
    print('')
    act = ''

    for now in actions:
        now = actions[now]
        for element in now:
            if ans.upper() == element.upper():
                act = now[1]
                if int(debug):
                    print(ans.upper()+' = '+element.upper()+'  <<<<')
            elif ans.upper() != element.upper() and int(debug):
                print(ans.upper()+' ?= '+element.upper())
        
    if ans in diction['SettingsA']:
        settings()

    elif ans in diction['Help']:
        print('\n' + diction['Choose action'] + ':\n |')
        for z in diction['HelpList']:
            print(z[0] + '. ' + z[1])
        print(diction['ListEnd'])
        ans = input('|?] ')
        print('')
        if ans in diction['HelpList'][0]:
            for x in tutorial:
                print(x['Text'])
                if x['Input']:
                    for y in x['Input']:
                        if x['Answers']:
                            while 1:
                                if input(y) in x['Answers']:
                                    break
                        else:
                            if x['Title'] == 'Math action':
                                if y == '|a-> ':
                                    while 1:
                                        a = input(y)
                                        if a.isdigit():
                                            break
                                elif y == 'a + ':
                                    while 1:
                                        b = input(y)
                                        if b.isdigit():
                                            print(a, '+', b, '=', int(a) + int(b))
                                            break
                            elif x['Title'] == 'FastCalc':
                                while 1:
                                    a = input(y)
                                    chech = 0
                                    for b in a:
                                        if b in ['+', '-', '*', '/', '%', '(', ')', ' ', '.'] or b.isdigit():
                                            chech += 1
                                    if chech == len(a):
                                        break
                                execdict = {'a' : a, 'res' : 0}
                                try:
                                    exec('res = ' + a, execdict)
                                    print(a + ' = ' + str(execdict['res']))
                                except:
                                    print(diction['MathError'])
        elif ans in diction['HelpList'][1]:
            print(diction['Functions'])
        elif ans in diction['HelpList'][2]:
            print(diction['About'])

    elif ans == '?div':
        if divise:
            for x in divise:
                print(x, end=' ')

    elif ans in keyWordDict:
        print(keyWordDict[ans])
    
    elif ans.upper() in diction['ExitList']:
        br = False
    
    elif act == '' and ans != '':
        chech = 0
        for x in ans:
            if x in ['+', '-', '*', '/', '%', '(', ')', ' ', '.'] or x.isdigit():
                chech += 1
        if chech == len(ans):
            execdict = {'ans' : ans, 'res' : 0}
            try:
                exec('res = ' + ans, execdict)
                print(ans + ' = ' + str(execdict['res']))
            except:
                print(diction['MathError'])
        elif ans[0] == '?':
            alis = list(ans)
            alis.remove('?')
            nnn = ''
            for num in alis:
                nnn += num
            if nnn.isdigit():
                analisys(int(nnn))
        else:
            print(diction['InputError'])
    else:
        a, b = getnum(act)
#                                   ALL MATH ACTIONS
        try:
        #if 1:
            if a != 'break' and not (act in ['^/', '>>|', '?']):  # REGULAR math actions, which matches with special symbols
                rdict = {'res' : 0, 'a' : a, 'act' : act, 'b' : b}
                exec('res = a ' + act + ' b', rdict)
                print(a, act, b, '=', rdict['res'])
                
            elif a != 'break' and act == '^/':   # ROOT (special symbol)
                print(a, act, b, '=', a ** (1 / b))
                
            elif a != 'break' and act == '>>|':  # Conversion to decimal number system (special symbol)
                a, b = round(a), round(b)
                print(a, '<|>', b, '<[10]> ', int(str(a), b))
                
            elif a != 'break' and act == '?':    # Analysis
                analisys(a)
        except:
            print('\n' + diction['MathError'])

#                                   UTILITE DIFITIONS
def analisys(a):
    global divise, diction
    print('\n  ' + str(a) + diction['Analisys'][5])
    
    long = len(str(a))  #1
    if '.' in str(a):
        long -= 1
    if str(a)[-1] == '0':
        long -= 1
    parity = True       #3
    if a % 2:
        parity = False
    summ = 0
    for x in str(round(a)):
        summ += int(x)
    divisors = ''       #4
    divise = get_decimals(a)
    if len(divise) < 10:
        for d in divise:
            if divisors == '':
                divisors = str(d)
            else:
                divisors += ' ' + str(d)
    else:
        divisors = diction['DivisorWarning'][0] + str(len(divise)) + diction['DivisorWarning'][1]
#                                           OUTPUT ANALISYS RESULT
    print(diction['Number of digits'], long)
    print(diction['Analisys'][0], parity)
    print(diction['Analisys'][1], summ)
    print(diction['Analisys'][2], divisors)
    print(diction['Analisys'][3], a ** (0.5))
    print(diction['Analisys'][4], a ** (1 / 3))

def getnum(act): #get numbers. just function. y im doin this??? ----- this is bcz i can
    a, b = 0, 0
    if act != '?':  # REGULAR input (twice)
        try:
            a = float(input('|a-> '))
            b = float(input(str(a) + ' ' + act + ' '))
        except:
            a = 'break'
    else:           # ANALYSIS input (once)
        try:
            a = float(input('|?-> '))
        except:
            a = 'break'
    return [a, b]

def settings():
    global diction, sactions, language, mode, br, \
           installdata, hideMenu, divisorLimit, firststart
    brs = True
    setShow = True
    while brs:
        if (hideMenu == '1' and setShow) or (hideMenu == '0'):
            print('\n' + diction['Choose action'] + ':\n |')
            for x in sactions:
                title = x
                x = sactions[x]
                if title == 'Hide Menu':
                    print(x[1] + '. ' + x[0] + ' ' * (20 - len(x[0])) + ': ' + x[2][hideMenu])
                elif title == 'Divisor Limit':
                    print(x[1] + '. ' + x[0] + ' ' * (20 - len(x[0])) + ': ' + divisorLimit)
                elif title == 'Language':
                    print(x[1] + '. ' + x[0] + ' ' * (20 - len(x[0])) + ': ' + language)
                else:
                    print(x[1] + '. ' + x[0])
            print(diction['ListEnd'])
        ans = input('|*] ')
        if ans in sactions['Language']: # CHANGING LANGUAGE
            print(diction['ChooseLanguage'])
            for x in sactions['Language'][2]:
                print(x[1] + '. ' + x[0])
            print(diction['ListEnd'])
            ans = input('|] ')
            for x in sactions['Language'][2]:
                if ans in x:
                    language = x[0]
            setConfig('language', language)
            print(diction['LangSet'], language)
            print(diction['Restart'])
            br = False
            brs = False
        elif ans in sactions['Divisor Limit']: # DIVISORS LIMIT
            print('\n' + sactions['Divisor Limit'][2][0] + '\n')
            ans = input('|] ')
            try:
                intans = int(ans)
                setConfig('divisorLimit', ans)
                br = False
                brs = False
                print('\n' + diction['Restart'])
            except:
                pass
        elif ans in sactions['Hide Menu']: #Hide menu
            if int(hideMenu):
                setConfig('hideMenu', '0')
            else:
                setConfig('hideMenu', '1')
            print(diction['Restart'])
            br, brs = False, False
        elif ans in sactions['Reset Installation']: # INSTALL RESET
            with open('content/config.txt', 'w') as confile:
                confile.write(installdata)
            print('\nINSTALLATION RESET\nRestart the program')
            br = False
            brs = False
        elif ans.upper() in diction['ExitList']:
            brs = False
            firststart = True
        setShow = False

def get_decimals(num):
    global debug, divisorLimit, diction, lenpers
    cur = 1
    dec = []
    try:
        num = int(num)
        percent = 0
        lenpers = 10
        if num >= 1000000000:
            lenpers = 1000
            print(diction['CtrlC Break'] + ' 1000=')
            print('_' * 100)
        elif num >= 1000000:
            lenpers = 100
            print(diction['CtrlC Break'] + ' 100=')
        if lenpers != 1000:
            print('_' * lenpers)
        while cur <= num: # Main cycle
            if int(debug):
                print('\n', cur, 'checking with LIMIT ', divisorLimit, end='')
            if int(num) % cur == 0: #adding divisor
                dec += [cur]
                if int(debug):
                    print('    TRUE')
            if int(cur / num * lenpers) != percent: #Percent Controller
                if lenpers == 1000 and percent % 100 == 0:
                    if percent != 0:
                        print('|>', str(perce(percent)) + '%')
                        print('_' * 100)
                percent += 1
                print('=', end='')
            if cur > int(divisorLimit) and divisorLimit != '-1': # Checking divisor limit
                print('|>', str(perce(percent)) + '%')
                print('  < ! > ' + diction['DivisorLimitBreak'], '(' + divisorLimit + ')')
                break
            cur += 1
        if percent == lenpers:
            print('|>', str(perce(percent)) + '%')
        print('')
    except:
        print('|>', str(perce(percent)) + '%')
    return dec

def perce(percent):
    global lenpers
    if lenpers == 1000:
        return percent / 10
    elif lenpers == 100:
        return percent
    elif lenpers == 10:
        return percent * 10

def setConfig(name, value):
    global debug
    with open('content/config.txt', 'r') as confile:
        context = confile.read()
    conlist = context.split('\n')
    for x in conlist:
        if x.split(':')[0] == name:
            tochange = conlist.index(x)
    conlist[tochange] = name + ':' + value
    context = ''
    for line in conlist:
        context += line + '\n'
    if int(debug):
        print('setConfig() called: output:')
        print(context)
    with open('content/config.txt', 'w') as confile:
        confile.write(context)
    
def harmed(error=None):
    global installdata
    print(' ----  Y O U R   C O N F I G U R A T I O N   F I L E   W A S   H A R M E D  ----\a\n')
    if error:
        print('                 Error:', error, '\n')
    print('                         Type "reset" to reset installation"\n                     Or:\n')
    print('             Try to download configuration file from github:')
    print('         - find a v1.6 release on  github.com/DaregonPL/Rozhok-Calc-Full')
    print('         - download source code')
    print('         - copy file "content/config.txt" to current directory')
    print('         - restart the program')
    ans = input()
    if ans == 'reset':
        with open('content/config.txt', 'w') as confile:
            confile.write(installdata)
        print('\nINSTALLATION RESET\nRestart the program')

#                   # cycle      ------ F  O  R  E  V  E  R ------ 
def s():
    global br, divise, firststart
    print('Welcome to RozhokCalc!       v1.6')
    firststart = True
    br = True
    while br:
        main()

#                                   P R E P A R I N G

installdata =\
'''
mode:installation
language:ENG
debug:0
divisorLimit:10000000
hideMenu:0
# modes aviable : installation/console/window
# languages : ENG/RUS/ARB'''

# CONFIGURATIONS

with open('content/config.txt', 'r') as file:
    txt = file.read()
for config in txt.split('\n'):
    if config != '' and config[0] != '#':
        varData = config.split(':')
        exec(varData[0] + ' = "' + varData[1] + '"')
        print((varData[0] + '\n') * 0, end='')

# KeyWords

with open('content/KeyWords.dictionary', 'r') as keys:
    dictStr = ''
    for key in keys.read().split('\n'):
        dictStr += ', ' * int(bool(dictStr)) + '"' + key.split(':')[0] + '":"' + key.split(':')[1] + '"'
    exec('keyWordDict = {' + dictStr + '}')

try:
    working = True
    trychecklist = [language, mode, debug, divisorLimit]
except:
    harmed()
    working = False

if working:
    divise=[]
    if language == 'RUS':
        from content.languages.RUS import *
    elif language == 'ARB':
        from content.languages.ARB import *
    else:
        from content.languages.ENG import *

    if mode == 'console':
        s()
    elif mode == 'installation':
        print('Welcome to RozhokCalc v1.6 installation wizard!')
        ibr = True
        modes = [['Console', '1'], ['Window', '2']]
        while ibr:
            print('Select an aviable mode for you:')
            for now in modes:
                print(now[1] + '. ' + now[0])
            ans = input('>>')
            if ans in modes[0]:
                mode = 'console'
                ibr = 0
            elif ans in modes[1]:
                print('Sorry, this mode will be aviable in version 2.0\nSet mode: console')
                mode = 'console'
                ibr = 0
        setConfig('mode', mode)
        from content.languages.ENG import *
        print('Installation complete')
        if mode == 'console':
            s()
        elif mode == 'window':
            import content.window
    elif mode == 'window':
        import content.window
    else:
        harmed('Unsupported mode')
