'''
Rozhok Calc (console) v1.5
        by DaregonPL
'''
def main(): # just main. im not gonna describe that
    global br, diction, actions, debug, divise
    print('\n' + diction[0] + ':\n |')
#                                   PRINTING POSSIBLE ACTIONS
    for x in actions:
        print(x[2] + '. ' + x[0])
    print(diction[2])
    print(diction[7])
#                                   WORK WITH INPUT(s)
    ans = input('|] ')
    print('')
    act = ''

    for now in actions:
        for element in now:
            if ans.upper() == element.upper():
                act = now[1]
                if int(debug):
                    print(ans.upper()+' = '+element.upper()+'  <<<<')
            elif ans.upper() != element.upper() and int(debug):
                print(ans.upper()+' ?= '+element.upper())
        
    if ans in diction[3]:
        settings()

    elif ans == '?div':
        if divise:
            for x in divise:
                print(x, end=' ')
    
    elif ans.upper() in diction[8]:
        br = False
    
    elif act == '' and ans != '':
        chech = 0
        for x in ans:
            if x in ['+', '-', '*', '/', '%', '(', ')', ' '] or x.isdigit():
                chech += 1
        if chech == len(ans):
            execdict = {'ans' : ans, 'res' : 0}
            try:
                exec('res = ' + ans, execdict)
                print(execdict['res'])
            except:
                print(diction[5])
        elif ans[0] == '?':
            alis = list(ans)
            alis.remove('?')
            nnn = ''
            for num in alis:
                nnn += num
            if nnn.isdigit():
                analisys(int(nnn))
        else:
            print(diction[4])
        
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
            print('\n' + diction[5])

#                                   UTILITE DIFITIONS
def analisys(a):
    global divise, diction
    print('\n  ' + str(a) + diction[9][5])
    
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
    if len(divise) < 6:
        for d in divise:
            if divisors == '':
                divisors = str(d)
            else:
                divisors += ' ' + str(d)
    else:
        divisors = 'Type "?div" to see all the divisors (' + str(len(divise)) + ' found)'
#                                           OUTPUT ANALISYS RESULT
    print(diction[1], long)
    print(diction[9][0], parity)
    print(diction[9][1], summ)
    print(diction[9][2], divisors)
    print(diction[9][3], a ** (0.5))
    print(diction[9][4], a ** (1 / 3))

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
    global diction, sactions, language, mode, br
    brs = True
    while brs:
        print('\n' + diction[0] + ':\n |')
        for x in sactions:
            print(x[1] + '. ' + x[0])
        print(diction[7])
        ans = input('|] ')
        if ans in sactions[0]: # CHANGING LANGUAGE
            print(diction[6])
            for x in sactions[0][2]:
                print(x[1] + '. ' + x[0])
            print(diction[7])
            ans = input('|] ')
            for x in sactions[0][2]:
                if ans in x:
                    language = x[0]
            setConfig('language', language)
            print(diction[10], language)
            print(diction[11])
            br = False
            brs = False
        elif ans in sactions[1]: # DIVISORS LIMIT
            print('\n' + sactions[1][2][0] + '\n')
            ans = input('|] ')
            try:
                intans = int(ans)
                setConfig('divisorLimit', ans)
                br = False
                brs = False
                print('\n' + diction[11])
            except:
                pass
        elif ans in sactions[2]: # INSTALL RESET
            with open('content/config.txt', 'w') as confile:
                confile.write('mode:installation\nlanguage:ENG\ndebug:0\ndivisorLimit:10000000')
            print('\nINSTALLATION RESET\nRestart the program')
            br = False
            brs = False
        elif ans.upper() in diction[8]:
            brs = False

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
            print('Press Ctrl+C to break 1000=')
            print('_' * 100)
        elif num >= 1000000:
            lenpers = 100
            print('Press Ctrl+C to break 100=')
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
                print('  < ! > ' + diction[12], '(' + divisorLimit + ')')
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
    print(' ----  Y O U R   C O N F I G U R A T I O N   F I L E   W A S   H A R M E D  ----\a\n')
    if error:
        print('                 Error:', error, '\n')
    print('             Try to download configuration file from github:')
    print('         - find a v1.5 release on  github.com/DaregonPL/Rozhok-Calc-Full')
    print('         - download source code')
    print('         - copy file "content/config.txt" to current directory')
    print('         - restart the program')
    print('\nOr type "reset" to reset installation"')
    ans = input()
    if ans == 'reset':
        with open('content/config.txt', 'w') as confile:
            confile.write('mode:installation\nlanguage:ENG\ndebug:0\ndivisorLimit:10000000')
        print('\nINSTALLATION RESET\nRestart the program')

#                   # cycle      ------ F  O  R  E  V  E  R ------ 
def s():
    global br, divise
    print('Welcome to RozhokCalc!       v1.5')
    br = True
    while br:
        main()

#                                   P R E P A R I N G

with open('content/config.txt', 'r') as file:
    txt = file.read()
for config in txt.split('\n'):
    if config != '':
        varData = config.split(':')
        exec(varData[0] + ' = "' + varData[1] + '"')

try:
    working = True
    trychecklist = [language, mode, debug, divisorLimit]
except:
    harmed()
    working = False

if working:
    divise=[]
    if language == 'RUS':
        from content.RUS import diction, actions, sactions
    elif language == 'ARB':
        from content.ARB import diction, actions, sactions
    else:
        from content.ENG import diction, actions, sactions

    if mode == 'console':
        s()
    elif mode == 'installation':
        print('Welcome to RozhokCalc v1.3 installation wizard!')
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
        from content.ENG import diction, actions, sactions
        print('Installation complete')
        if mode == 'console':
            s()
        elif mode == 'window':
            import content.window
    elif mode == 'window':
        import content.window
    else:
        harmed('Unsupported mode')
