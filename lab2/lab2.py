import os

def cls():                      # cleans previous terminal
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

cls()


def check_pnr(pn_list):
    checkvalue = pn_list[-1]
    true_false = True
    
    worth, multiplier_list, products = control(pn_list)

    if worth % 10 == 0:
        if checkvalue == 0: true_false = True
        else: true_false = False
    else:
        conf_value = 10 - (worth % 10)
        #print(conf_value)
        if conf_value == checkvalue: true_false = True
        else: true_false = False

    closest_higher = int((worth + 10)/10)
    if (worth + 10)%10 != 0: closest_higher *= 10
    else: closest_higher = (closest_higher * 10) -10

    writing(pn_list,multiplier_list, products, worth, closest_higher, true_false)


def control(pn_list):
    worth = 0
    multiplier_write = []
    produkter = []
    for i in range(len(pn_list[:-1])):
        talsumma = pn_list[i]
        times_two = talsumma
        multiplier_write.append((i+1)%2+1)

        if i % 2 == 0: 
            talsumma = times_two = talsumma*2

            if talsumma >= 10: 
                tal1 = talsumma%10
                tal2 = int((talsumma-tal1)/10)
                talsumma = tal1+tal2
            
        produkter.append(times_two)
        worth += talsumma

    return worth, multiplier_write, produkter


def writing(pn_list,multiplier_list,products,numbersum, closest_higher, true_false):

    print('Personnummer:   ', pn_list[:-1])
    print('Multiplecerar:  ', multiplier_list)
    print('------------------------------------')
    print('Produkten:      ', products)
    print('siffersumman är:', numbersum)
    print('closest higher: ', closest_higher)
    print('Knotrollsiffra: ', closest_higher, '-', numbersum, '=', closest_higher - numbersum)
    if true_false == True: print('Personnummret Stämmer!')
    elif true_false == False: print('Personnummret Stämmer Inte!')
    else: print('något gick fel')

#pna = '0408266377'
# pn = [0,4,0,8,2,6,6,3,7,6]
# check_pnr(pn)
#print(list(pna))