# ========================= SHOPPING APP =========================
# SECTION- A1
# GROUP MEMBERS
# 1-KHUSHI AGRAWAL
# 2-KASHISH BANSAL
# 2-DIYA BANSAL
# 3-JAYANT SHARMA

e_item = ['EAROHONES', 'MOBILE', 'SMART WATCHES']
e_cost = [299, 10000, 450]
f_item = ['SHIRTS', 'SHOES', 'JEANS']
f_cost = [600, 750, 829]
g_item = ['CEREALS', 'FROZEN FOODS', 'DAIRY']
g_cost = [350, 499, 726]
c_item = []
c_cost = []
while 1:
    print('\n================= H O M E =================\n')

    c = input('PRESS 1 for Continue =>')
    if c == '1':
        while 1:
            print(
                '\n================= D A S H B O A R D =================\nWelcome to this App...\n1- USER\n2- ADMIN\n3- EXIT\nChoose the options by enter any number...')
            choice = int(input('\nEnter your choice =>'))
            if choice == 3:
                break
            if choice == 1:
                while 1:
                    print('\n1- LOGIN\n2- LOGOUT\n3- ONLY VIEW\n4- < BACK >')
                    c2 = int(input('Enter Option => '))
                    if c2 == 2 or c2 == 4:
                        break
                    if c2 == 3:
                        while 1:
                            print('\n================= B R O W S E =================\n')
                            print('\n1- ELECREONICS\n2- FASHION\n3- GROCERY\n4- BACK')
                            c3 = int(input('Enter Choice =>'))
                            if c3 == 4:
                                break
                            if c3 == 1:
                                while 1:
                                    print('\n================= E L E C T R O N I C S =================\n')
                                    print('ITEMS - COST')
                                    for i in range(len(e_item)):
                                        print(f'{i + 1}- {e_item[i]}-Rs {e_cost[i]}')
                                    print(f'{len(e_item) + 1}- <EXIT>')
                                    eb = int(input('=>'))
                                    if eb == len(e_item) + 1:
                                        break
                            if c3 == 2:
                                while 1:
                                    print('\n================= F A S H I O N =================\n')
                                    print('ITEMS - COST')
                                    for i in range(len(f_item)):
                                        print(f'{i + 1}- {f_item[i]}-Rs {f_cost[i]}')
                                    print(f'{len(f_item) + 1}- <EXIT>')
                                    fb = int(input('=>'))
                                    if fb == len(f_item) + 1:
                                        break
                            if c3 == 3:
                                while 1:
                                    print('\n================= G R O C E R Y =================\n')
                                    print('ITEMS - COST')
                                    for i in range(len(g_item)):
                                        print(f'{i + 1}- {g_item[i]}-Rs {g_cost[i]}')
                                    print(f'{len(e_item) + 1}- <EXIT>')
                                    gb = int(input('=>'))
                                    if gb == len(g_item) + 1:
                                        break
                    if c2 == 1:
                        while 1:
                            print('\n================= A U T H E N T I C A T I O N =================\n')
                            kh = 'KHUSHI'
                            ks = 'KASHISH'
                            ja = 'JAYANT'
                            di = 'DIYA'
                            pssd = 'GLAU789'
                            un = input('Please Enter valid User name => ')
                            un = un.upper()
                            password = input('Please Enter PASSWORD => ')
                            if ((un == kh or un == ks or un == ja or un == di) and password == pssd):
                                print('You are successfully LOGIN')
                                bauth1 = int(input('PRESS 1- for CONTINUE\nPRESS 2- for BACK\n=> '))
                                if bauth1 == 2:
                                    break
                                else:

                                    while 1:
                                        print('\n================= B R O W S E =================\n')
                                        print('\n1- ELECREONICS\n2- FASHION\n3- GROCERY\n4- <MY CART>\n5- <BACK>')
                                        c3 = int(input('Enter Choice =>'))
                                        if c3 == 5:
                                            break
                                        if c3 == 1:
                                            while 1:
                                                print('\n================= E L E C T R O N I C S =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(e_item)):
                                                    print(f'{i + 1}- {e_item[i]}-Rs {e_cost[i]}')
                                                print(f'{len(e_item) + 1}- <EXIT>')
                                                eb = int(input('=>'))
                                                if eb == (len(e_item) + 1):
                                                    break
                                                if eb > (len(e_item) + 1):
                                                    print('YOU SELECT OUT OF RANGE OPTION')
                                                if eb <= len(e_item):
                                                    c_item.append(e_item[eb - 1])
                                                    c_cost.append(e_cost[eb - 1])
                                                    print('ITEM ADDED')
                                        if c3 == 2:
                                            while 1:
                                                print('\n================= F A S H I O N =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(f_item)):
                                                    print(f'{i + 1}- {f_item[i]}-Rs {f_cost[i]}')
                                                print(f'{len(f_item) + 1}- <EXIT>')
                                                fb = int(input('=>'))
                                                if fb == (len(f_item) + 1):
                                                    break
                                                if fb > (len(f_item) + 1):
                                                    print('YOU SELECT OUT OF RANGE OPTION')
                                                if fb <= len(f_item):
                                                    c_item.append(f_item[fb - 1])
                                                    c_cost.append(f_cost[fb - 1])
                                                    print('ITEM ADDED')

                                        if c3 == 3:
                                            while 1:
                                                print('\n================= G R O C E R Y =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(g_item)):
                                                    print(f'{i + 1}- {g_item[i]}-Rs {g_cost[i]}')
                                                print(f'{len(e_item) + 1}- <EXIT>')
                                                gb = int(input('=>'))
                                                if gb == (len(g_item) + 1):
                                                    break
                                                if gb > (len(g_item) + 1):
                                                    print('YOU SELECT OUT OF RANGE OPTION')
                                                if gb <= len(g_item):
                                                    c_item.append(g_item[gb - 1])
                                                    c_cost.append(g_cost[gb - 1])
                                                    print('ITEM ADDED')
                                        if c3 == 4:
                                            while 1:
                                                print('\n================= M Y   C A R T =================\n')
                                                for i in range(len(c_item)):
                                                    print(f'{i + 1}- {c_item[i]}-Rs {c_cost[i]}')
                                                print('**** OPTIONS ****')
                                                print('\n1- DELETE ITEM\n2- PURCHASE\n3- BACK')
                                                mb = int(input('=>'))
                                                if mb == 3:
                                                    break
                                                if mb == 1:
                                                    mb1 = int(input('ITEM U WANT TO DELETE=>'))
                                                    c_item.remove(c_item[mb1 - 1])
                                                    c_cost.remove(c_cost[mb1 - 1])
                                                if mb == 2:
                                                    while 1:
                                                        print('\n================= B I L L =================\n')
                                                        tcost = 0
                                                        for i in range(len(c_item)):
                                                            tcost = tcost + c_cost[i]
                                                            print(f'{i + 1}- {c_item[i]}-Rs {c_cost[i]}')
                                                        print(f'\nTOTAL COST=> Rs{tcost}')
                                                        print('**** OPTIONS ****')
                                                        print('1- PAYMENT\n2- BACK')
                                                        mbx = int(input('=>'))
                                                        if mbx == 2:
                                                            break
                                                        if mbx == 1:
                                                            print(
                                                                '\n================= P A Y M E N T =================\n')
                                                            print('1- CASH ON DELEVERY\n2- NET BANKING\n3- BACK')
                                                            mbp = int(input('=>'))
                                                            if mbp == 3:
                                                                break
                                                            if mbp == 1:
                                                                print(
                                                                    '\n================= D O N E =================\n\nYour items ordered successfully')
                                                                exit()
                                                            if mbp == 2:
                                                                pin = input('Enter 4 digit pin =>')
                                                                print(
                                                                    '\n================= D O N E =================\n\nYour items ordered successfully')
                                                                exit()


                            else:
                                print('INCORRECT USER ID AND PASSWORD')
                                bauth2 = int(input('PRESS 1- for BACK => '))
                                if bauth2 == 1:
                                    break
            if choice == 2:
                while 1:
                    print('\n================= A D M I N *  P A N E L =================\n')
                    print('\n1- LOGIN\n2- LOGOUT\n3- < EXIT >')
                    ac = int(input('=>'))
                    if ac == 2 or ac == 3:
                        break
                    if ac == 1:
                        while 1:
                            print('\n================= A U T H E N T I C A T I O N =================\n')
                            kh = 'AKHUSHI'
                            ks = 'AKASHISH'
                            ja = 'AJAYANT'
                            di = 'ADIYA'
                            pssd = 'GLAU789'
                            un = input('Please Enter valid User name => ')
                            un = un.upper()
                            password = input('Please Enter PASSWORD => ')
                            if ((un == kh or un == ks or un == ja or un == di) and password == pssd):
                                print('You are successfully LOGIN')
                                bauth1 = int(input('PRESS 1- for CONTINUE\nPRESS 2- for BACK\n=> '))
                                if bauth1 == 2:
                                    break
                                else:
                                    while 1:
                                        print('\n================= M A N A G E =================\n')
                                        print('\n1- ELECREONICS\n2- FASHION\n3- GROCERY\n4- <BACK>')
                                        a3 = int(input('=>'))
                                        if a3 == 4:
                                            break
                                        if a3 == 1:
                                            while 1:
                                                print('\n================= E L E C T R O N I C S =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(e_item)):
                                                    print(f'{i + 1}- {e_item[i]}-Rs {e_cost[i]}')
                                                print('\n**** OPTIONS ****\n')

                                                print('1- ADD\n2- DELETE\n3- BACK')
                                                ea = int(input('=>'))
                                                if ea == 3:
                                                    break
                                                if ea == 1:
                                                    print('\n================= A D D =================\n')
                                                    eit = input('Enter name of item =>')
                                                    ect = int(input('Enter cost of item =>'))
                                                    e_item.append(eit)
                                                    e_cost.append(ect)
                                                if ea == 2:
                                                    print('\n================= D E L E T E =================\n')
                                                    edt = int(input('ITEM U WANT TO DELETE=>'))
                                                    e_item.remove(e_item[edt - 1])
                                                    e_cost.remove(e_cost[edt - 1])
                                        if a3 == 2:
                                            while 1:
                                                print('\n================= F A S H I O N =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(f_item)):
                                                    print(f'{i + 1}- {f_item[i]}-Rs {f_cost[i]}')
                                                print('\n**** OPTIONS ****\n')

                                                print('1- ADD\n2- DELETE\n3- BACK')
                                                fa = int(input('=>'))
                                                if fa == 3:
                                                    break
                                                if fa == 1:
                                                    print('\n================= A D D =================\n')
                                                    fit = input('Enter name of item =>')
                                                    fct = int(input('Enter cost of item =>'))
                                                    f_item.append(fit)
                                                    f_cost.append(fct)
                                                if fa == 2:
                                                    print('\n================= D E L E T E =================\n')
                                                    fdt = int(input('ITEM U WANT TO DELETE=>'))
                                                    f_item.remove(f_item[fdt - 1])
                                                    f_cost.remove(f_cost[fdt - 1])
                                        if a3 == 3:
                                            while 1:
                                                print('\n================= G R O C E R Y =================\n')
                                                print('ITEMS - COST')
                                                for i in range(len(g_item)):
                                                    print(f'{i + 1}- {g_item[i]}-Rs {g_cost[i]}')
                                                print('\n**** OPTIONS ****\n')

                                                print('1- ADD\n2- DELETE\n3- BACK')
                                                ga = int(input('=>'))
                                                if ga == 3:
                                                    break
                                                if ga == 1:
                                                    print('\n================= A D D =================\n')
                                                    git = input('Enter name of item =>')
                                                    gct = int(input('Enter cost of item =>'))
                                                    g_item.append(git)
                                                    g_cost.append(gct)
                                                if ga == 2:
                                                    print('\n================= D E L E T E =================\n')
                                                    gdt = int(input('ITEM U WANT TO DELETE=>'))
                                                    g_item.remove(g_item[gdt - 1])
                                                    g_cost.remove(g_cost[gdt - 1])

                            else:
                                print('INCORRECT ID AND PASSWORD')
                                break



