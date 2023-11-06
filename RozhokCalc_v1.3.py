'''
Rozhok Calc (console) v1.3
        by DaregonPL
'''
def main(): # just main. im not gonna describe that
    global br, diction, actions
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
        if ans in now:
            act = now[1]
        
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
                divisors = ''       #4
                for d in get_decimals(a):
                    if divisors == '':
                        divisors = str(d)
                    else:
                        divisors += ' ' + str(d)
#                                           OUTPUT ANALISYS RESULT
                print(diction[1], long)
                print(diction[9][0], parity)
                print(diction[9][1], summ)
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
    global diction, sactions, lang, mode, br
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
            if ans in sactions[0][2][0]:
                lang = 'ENG'
            elif ans in sactions[0][2][1]:
                lang = 'RUS'
            elif ans in sactions[0][2][2]:
                lang = 'ARB'
            with open('content/config.txt', 'w') as confile:
                confile.write('mode:' + mode + '\nlanguage:' + lang)
            print(diction[10], lang)
            print(diction[11])
            br = False
            brs = False
        elif ans in sactions[1]:
            with open('content/config.txt', 'w') as confile:
                confile.write('mode:installation\nlanguage:ENG')
            print('\nINSTALLATION RESET\nRestart the program')
            br = False
            brs = False
        elif ans.upper() in diction[8]:
            brs = False
def get_decimals(num):
    cur = 1
    dec = []
    while cur <= num:
        if num % cur == 0:
            num = num // cur
            dec += [cur]
        cur += 1
    return dec
#                   # cycle      ------ F  O  R  E  V  E  R ------ 
def s():
    global br, diction, sactions, actions, lang, mode
    print('Welcome to RozhokCalc!       v1.3')
    br = True
    
    while br:
        main()

with open('content/config.txt', 'r') as file:
    txt = file.read()
for config in txt.split('\n'):
    if config.split(':')[0] == 'mode':
        mode = config.split(':')[1]
    if config.split(':')[0] == 'language':
        lang = config.split(':')[1]
        
#                                   I M P O R T I N G   D I C T I O N A R I E S

if lang == 'ENG':
    from content.ENG import diction, actions, sactions
if lang == 'RUS':
    from content.RUS import diction, actions, sactions
if lang == 'ARB':
    from content.ARB import diction, actions, sactions

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
    with open('content/config.txt', 'w') as cnf:
        cnf.write('mode:' + mode + '\nlanguage:ENG')
        from content.ENG import diction, actions, sactions
    print('Installation complete')
    if mode == 'console':
        s()
    elif mode == 'window':
        import content.window
elif mode == 'window':
    import content.window
