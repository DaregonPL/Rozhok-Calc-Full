'''
Rozhok Calc (console) v1.4
        by DaregonPL
'''
def main(): # just main. im not gonna describe that
    global br, diction, actions, debug
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
        
    elif ans.upper() in diction[8]:
        br = False
    
    elif act == '' and ans != '':
        print(diction[4])
        
    else:
        a, b = getnum(act)
#                                   ALL MATH ACTIONS
        try:
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
                print(diction[1], long)
                print(diction[9][0], parity)
                print(diction[9][1], summ)
                divisors = ''       #4
                for d in get_decimals(a):
                    if divisors == '':
                        divisors = str(d)
                    else:
                        divisors += ' ' + str(d)
#                                           OUTPUT ANALISYS RESULT
                print(diction[9][2], divisors)
                print(diction[9][3], a ** (0.5))
                print(diction[9][4], a ** (1 / 3))
        except:
            print(diction[5])

#                                   UTILITE DIFITIONS

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
                confile.write('mode:installation\nlanguage:ENG\ndebug:0\ndivisorLimit:1000000000')
            print('\nINSTALLATION RESET\nRestart the program')
            br = False
            brs = False
        elif ans.upper() in diction[8]:
            brs = False

def get_decimals(num):
    global debug, divisorLimit, diction
    cur = 1
    dec = []
    #try:
    if 1:
        int(num)
        while cur <= num:
            if int(debug):
                print('\n', cur, 'checking with LIMIT ', divisorLimit, end='')
            if num % cur == 0:
                num = num // cur
                dec += [cur]
                if int(debug):
                    print('    TRUE')
            if cur > int(divisorLimit) and int(divisorLimit) != (-1):
                print('  < ! > ' + diction[12], '(' + divisorLimit + ')')
                break
            cur += 1
    #except:
     #   pass
    return dec

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
    print('         - find a v1.4 release on  github.com/DaregonPL/Rozhok-Calc-Full')
    print('         - download source code')
    print('         - copy file "content/config.txt" to current directory')
    print('         - restart the program')
    print('\nOr type "reset" to reset installation"')
    ans = input()
    if ans == 'reset':
        with open('content/config.txt', 'w') as confile:
            confile.write('mode:installation\nlanguage:ENG\ndebug:0\ndivisorLimit:1000000000')
        print('\nINSTALLATION RESET\nRestart the program')

#                   # cycle      ------ F  O  R  E  V  E  R ------ 
def s():
    global br
    print('Welcome to RozhokCalc!       v1.4')
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
                mode = 'window'
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
