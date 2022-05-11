# AGNIK SAHA (ROLL: 21CS60A01)
# ASSIGNMENT 4
# Task 2

import ply.lex as lex
import ply.yacc as yacc
import re
import os


total_cases = []
active_cases = []
total_deaths = []
total_recovered = []
total_tests = []
death_per_million = []
test_per_million = []
new_case = []
new_death = []
new_recovered = []



def t_LTOTALCASE(t):
    r'<span\sstyle="color:\#aaa">'
    return t


def t_CLOSESPAN(t):
    r'</span>\n*'
    return t


def t_LRECOVERCASE(t):
    r'<div\sclass="maincounter-number"\sstyle="color:\#8ACA2B\s">\n*'
    return t


def t_LDEATH(t):
    r'<h1>Deaths:<\/h1>\n<div\sclass="maincounter-number">\n'
    return t

def t_LACTIVECASE(t):
    r'<div\sclass="number-table-main">*'
    return t
def t_EACTIVECASE(t):
    r'</div>\n<div\sstyle="font-size:13.5px">Currently'
    return t


def t_CLOSEDIV(t):
    r'</div>'
    return t

def t_OPENSPAN(t):
    r'<span>'
    return t


def p_start(t):
    '''start : total_cases
                | recovered_cases 
                | deaths
                | active_cases
             '''



def t_NUM(t):
    r"\d+"
    return t


t_ignore = " \t"

def t_error(t):
    t.lexer.skip(1)


def p_total_cases(t):
    'total_cases : LTOTALCASE pnum CLOSESPAN'
    t[0] = t[2]
    # print("Total Cases : ", t[2].replace(" ", ""))
    total_cases.append(t[2].replace(" ", ""))

def p_recovered_cases(t):
    'recovered_cases : LRECOVERCASE OPENSPAN pnum CLOSESPAN CLOSEDIV'
    t[0] = t[3]
    #print("Recovered Cases : ", t[3])
    total_recovered.append(t[3].replace(" ", ""))

def p_deaths(t):
    'deaths : LDEATH OPENSPAN pnum CLOSESPAN CLOSEDIV'
    t[0] = t[3]
    #print("total deaths : ", t[3])
    total_deaths.append(t[3].replace(" ", ""))

def p_active_cases(t):
    'active_cases : LACTIVECASE pnum EACTIVECASE'
    t[0] = t[2]
    #print("Active cases : ", t[2])
    active_cases.append(t[2].replace(" ", ""))

def p_pnum(t):
    'pnum : NUM'
    t[0] = t[1]


def p_pnum_multi(t):
    'pnum : NUM pnum'
    t[0] = t[1] + ' ' + t[2]


def p_error(t):
    pass



tokens = [
    'LTOTALCASE',
    'CLOSESPAN',
    'NUM',
    'LRECOVERCASE',
    'LDEATH',
    'CLOSEDIV',
    'OPENSPAN', 
    'LACTIVECASE',  
    'EACTIVECASE',
    ]  



inputFileName = "worldometers_countrylist.txt"

with open(inputFileName) as f:
    lines = [ line.strip('\n').lower().replace(' ', '-') for line in list(f) ]
    
a = lines
b = ["--------","--------","--------","--------", "","europe:", "---------","north-america:","asia","south-america","africa","oceania"]

country_list = [x for x in a if (x not in b)]

print("================   Country list:  ==================")
for l in country_list:
    print(l)


of = open("log_file_task2.txt","w")  # log file of the program

while True:
    country = str(input("Enter the country(country name in lower case): ") )
    if country not in country_list:
        print("Please Enter valid country name")
        continue
    country_path = "./COUNTRIES/" + country + ".html"
    text = open(country_path, 'r', errors = 'ignore').read()

    lexer = lex.lex()

    parser = yacc.yacc()
    parser.parse(text)

    
    while True:
        field_requested = input("Enter the field no.(1-8) \n1.Total cases\n2.Active cases\n3.Total deaths\n4.Total recovered\n5.Total tests\n6. New case\n7.New death\n8.New recovered\n")
        
        if int(field_requested) not in range(1,9):
            print("Enter Val in range !!!")
            sys.exit(0)
            
        if(field_requested  == "1"):
            if(len(total_cases) > 0):
                print("Total cases in "+ country+" = "+ total_cases[-1])
                field_val = total_cases[-1]
            else:
                print("Some Error has occured !!!")
                field_val = " "
            req = "Total_cases"     #<country><req><field_val>

        elif(field_requested == "2"):
            if(len(active_cases) > 0):
                print("Active cases in "+ country+" = "+ active_cases[-1])
                field_val = active_cases[-1]
            else:
                print("Some Error has occured !!!")
                field_val = " "
            req = "Active_cases"

        elif(field_requested == "3"):
            if(len(total_deaths) > 0):
                print("Total deaths in "+ country+" = "+ total_deaths[-1])
                field_val = total_deaths[-1]
            else:
                print("Some Error has occured !!!")
                field_val = " "
            req = "Total_deaths"

        elif(field_requested == "4"):
            if(len(total_recovered) > 0):
                print("Total recovered in "+ country+" = "+ total_recovered[-1])
                field_val = total_recovered[-1]
            else:
                print("Some Error has occured !!!")
                field_val = " "
            req = "Total_recovered"

        elif(field_requested =="5"):
            pass
        elif(field_requested == "6"):
            pass
        elif(field_requested == "7"):
            pass
        elif(field_requested == "8"):
            pass


        # Writing to the log file  #<country><req><field_val>
        text_to_write = ""
        text_to_write = str('\n') + "<" + str(country) + "><" + str(req) +  "><" + str(field_val) + ">" + str('\n')
        print(text_to_write)
        of.write(text_to_write)

        explore = input("Want to explore other datas on same country (y/n)> ")
        if(explore == 'y'):
            continue
        elif(explore == 'n'):
            break
        else:
            print("Enter valid code")
            sys.exit(10)
            
    explore2 = input("Do you want to explore other countries  (y/n)? ")
    if(explore2 == 'y'):
        continue
    elif(explore2 == 'n'):
        break
    else:
        print("Enter valid code")
        sys.exit(10)

of.close()
