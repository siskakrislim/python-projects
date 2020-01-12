# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:59:08 2017

@author: HP
"""

#%%
lstr1="A very long string can be tied together using " +\
        "a backslash (also called the escape character)."
lstr2=("A very long string can also be tied together using "
        "parentheses to enclose the various parts.")
#%%
import random
def make_random():
    numlis=[]
    for i in range(0,10):
        numlis.append(random.randint(1,100))
    return numlis
def call_make_random():
    random_integers=make_random()
    print("The list of random numbers is", random_integers)
#%%
import random
def make_same_random():
    numlis=[]
    random.seed(17)
    for i in range(0,10):
        numlis.append(random.randint(1,100))
    return numlis
def call_make_random1():
    random_integers=make_same_random()
    print(random_integers)
    random_integers1=make_same_random()
    print(random_integers1)
#%%
import random
def make_random_real():
    numlis=[]
    random.seed(17)
    for i in range(0,10):
        numlis.append(random.random())
    return numlis
#%%
numlist=[67,54,39,47,38,23,99,91,91,70]
#%%
print(numlist)
numlist.sort()
print(numlist)
#%%
print(sorted(numlist))
#%%
def make_alpha_list():
    import random
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z']
    random.seed(17)
    alpha_list=[]
    for i in range(0,10):
        alpha_list.append(random.choice(alphabet))
    return alpha_list
#%%
alphlist=make_alpha_list()
#%%
alphlist=['q','n','z','j','l','j','f','y','w','w']
#%%
print(alphlist)
alphlist.sort()
print(alphlist)
#%%
Alphlist=['e','F','h','A','D','F','b','D','b','J']
#%%
print(Alphlist)
Alphlist.sort()
print(Alphlist)
#%%
print(Alphlist)
Alphlist.sort(key=str.lower)
print(Alphlist)
#%%
strlist=['now','is','the','time','for','all','good','men','to','come','to',
         'the','aid','of','their','country']
#%%
print(strlist)
strlist.sort()
print(strlist)
#%%
Strlist=['Now','is','The','time','For','All','Good','men','To','come','to',
         'the','aid','of','Their','country']
#%%
print(Strlist)
Strlist.sort(key=str.lower)
print(Strlist)
#%%
nlist=[2,4,13,3,7,8,5]
nlisteven=nlist+[9]
print(nlisteven)
rlist=[3.14,2.71,-8.43,5.25,10.11,-23.78,44.45]
rlisteven=rlist+[90.3]
#%%
import statistics
#%%
statistics.mean(nlist)
#%%
statistics.mean(rlist)
#%%
print(nlist)
print(sorted(nlist))
#%%
statistics.median(nlisteven)
#%%
print(rlist)
print(sorted(rlist))
#%%
statistics.median(rlist)
#%%
print(rlisteven)
print(sorted(rlisteven))
#%%
statistics.median(rlisteven)
#%%
mlist=[2,3,4,5,4,5,3,6,1,3,4,3]
#%%
print(mlist)
print(sorted(mlist))
#%%
statistics.mode(mlist)
#%%
statistics.stdev(rlist)
#%%
statistics.variance(rlist)
#%%
nlis=[3.14,-4,25,8,106,32]
print("The maximum of nlis is",max(nlis))
print("The minimum of nlis is",min(nlis))
print("The sum of nlis is",sum(nlis))
#%%
import random
stat_list=[]
for i in range(0,100):
    stat_list.append(1000*random.random()+5000)
ilis=[3,1,5,2,1,3,7,3]
#%%
def my_stats(slis):
    import statistics
    print("Mean: ",statistics.mean(slis))
    print("Median: ",statistics.median(slis))
#    print("Mode: ",statistics.mode(slis))
    try:
        print("Mode: ",statistics.mode(slis))
    except statistics.StatisticsError as e:
        print("Mode error: ",e)
    print("Standard Deviation: ",statistics.stdev(slis))
    print("Variance: ",statistics.variance(slis))
#%%
def test_try():
    numb=input("Enter a number: ")
    print(type(numb))
    try:
        num=float(numb)
        print(num)
    except Exception as e:
        print("Exception was: ",e)
#%%
import random
random.seed(77)
temperatures=[]
for i in range(0,20):
    temperatures.append(random.randint(20,95))
def temp_stat(temps):
    import statistics
    print(temps)
    print("Mean: ",statistics.mean(temps))
    print("Median: ",statistics.median(temps))
    print("Standard Deviation: ",statistics.stdev(temps))
    print("Variance: ",statistics.variance(temps))  
#%%
def temp_stat1(temps):
    import statistics
    random.seed(277)
    print(temps)
    print("Mean: ",statistics.mean(temps))
    print("Median: ",statistics.median(temps))
    print("Standard Deviation: ",statistics.stdev(temps))
    print("Variance: ",statistics.variance(temps))   
    try:
        print("Mode: ",statistics.mode(temps))
    except statistics.StatisticsError as e:
        print("Mode error: ", e)
#%%
nam1='"Teddy" Roosevelt'
nam2='Theodore "Teddy" Roosevelt'
age=60
wt=199.1515115
#%%
out1="name: {0}   age: {1}   weight: {2}"
#%%
print("name: {0}   age: {1}   weight: {2}".format(nam1,age,wt))
print("name: {0}   age: {1}   weight: {2}".format(nam2,age,wt))
#%%
out2="name: {0:>26}   age: {1:>4}   weight: {2:>10}"
#%%
print("name: {0:>26}   age: {1:>4}   weight: {2:>10}".format(nam1,age,wt))
print("name: {0:>26}   age: {1:>4}   weight: {2:>10}".format(nam2,age,wt))
#%%
out3="name: {0:>26}   age: {1:>4}   weight: {2:>5.2f}"
#%%
print("name: {0:>26}   age: {1:>4}   weight: {2:>5.2f}".format(nam1,age,wt))
print("name: {0:>26}   age: {1:>4}   weight: {2:>5.2f}".format(nam2,age,wt))
#%%
print(out3.format(nam1,age,wt))
print(out3.format(nam2,age,wt))
#%%
s1= "my short string"
n=5.1234
#%%
print("Start||{0:25}||End".format(s1))
print("Start||{0:25}||End".format(n))
print("Start||{0}||End".format(s1))
print("Start||{0:>25}||End-width 25, right aligned".format(s1))
print("Start||{0:<25}||End-width 25, left aligned".format(s1))
print("Start||{0:^25}||End-width 25, centered".format(s1))
#%%
s="hello, there"
print("Start||{0}||End".format(s))
print("Start||{0:25}||End-minimum width 25".format(s))
print("Start||{0:>25}||End-width 25, right aligned".format(s))
print("Start||{0:<25}||End-width 25, left aligned".format(s))
print("Start||{0:^25}||End-width 25, centered".format(s))
#%%
def delete_phone():
    print("Deleting")
def edit_phone():
    print("Editing")
def save_phone_list():
    print("Saving")
def load_phone_list():
    print("Loading")
def show_phones():
    print("Showing phones")
def create_phone():
    print("Adding a phone")
def menu_choice():
    print("Choose one of the following options?")
    print("    s) Show")
    print("    n) New")
    print("    d) Delete")
    print("    e) Edit")
    print("    q) Quit")
    choice=input("Choice: ")
    if choice.lower() in ['n','d','s','e','q']:
        return choice.lower()
    else:
        print(choice+"?"+" That is an invalid option!!!")
        return None
def main_loop():
    load_phone_list()
    while True:
        choice=menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print("Exiting...")
            break
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            delete_phone()
        elif choice == 's':
            show_phones()
        elif choice == 'e':
            edit_phone()
        else:
            print("Invalid choice")
            break
    save_phone_list()
if __name__ == '__main__':
    main_loop()
#%%
phones=[['Jerry Seinfield','(212) 344-3784'],['Cosmo Kramer','(212) 559-8185']]
name_pos=0
phone_pos=1
phone_header=['Name','Phone Number']
def delete_phone():
    print("Deleting")
def edit_phone():
    print("Editing")
def save_phone_list():
    print("Saving")
def load_phone_list():
    print("Loading")
def show_phones():
    show_phone(phone_header,"")
    index=1
    for phone in phones:
        show_phone(phone,index)
        index=index+1
    print()
def show_phone(phone,index):
    outputstr="{0:>3} {1:<20} {2:>16}" 
    print(outputstr.format(index,phone[name_pos],phone[phone_pos]))
def create_phone():
    print("adding a phone")
def menu_choice():
    print("Choose the following options?")
    print("    s) Show")
    print("    n) New")
    print("    d) Delete")
    print("    e) Edit")
    print("    q) Quit")
    choice=input("Choice: ")
    if choice.lower() in ['n','d','s','e','q']:
        return choice.lower()
    else:
        print(choice+"?"+" That is an invalid option!!!")
        return None
def main_loop():
    load_phone_list()
    while True:
        choice=menu_choice()
        if choice==None:
            continue
        if choice=='q':
            print("Exiting...")
            break
        elif choice=='n':
            create_phone()
        elif choice=='d':
            delete_phone()
        elif choice=='s':
            show_phones()
        elif choice == 'e':
            edit_phone()
        else:
            print("Invalid choice")
    save_phone_list()
if __name__ == '__main__':
    main_loop()
#%%
import csv
phones=[['Jerry Seinfield','(212) 344-3784'],['Cosmo Kramer','(212) 559-8185']]
name_pos=0
phone_pos=1
phone_header=['Name', 'Phone Number']
def proper_menu_choice(which):
    if not which.isdigit():
        print("'"+which+"'needs to be the number of a phone!")
        return False
    which=int(which)
    if which < 1 or which > len(phones):
        print("'"+str(which)+"'needs to be the number of a phone!")
        return False
    return True
def delete_phone(which):
    if not proper_menu_choice(which):
        return
    which=int(which)
    del phones[which-1]
    print("Deleted phone #",which)
def edit_phone(which):
    if not proper_menu_choice(which):
        return
    which=int(which)
    phone=phones[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    print(phone[name_pos])
    newname=input("Enter phone name to change or press return: ")
    if newname=="":
        newname=phone[name_pos]
    print(phone[phone_pos])
    newphone_num=input("Enter new phone number to change or press return: ")
    if newphone_num=="":
        newphone_num=phone[phone_pos]
    phone=[newname,newphone_num]
    phones[which-1]=phone
    print("Editing")
def save_phone_list():
    f=open("myphones.csv",'w',newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
    print("Saving")
def load_phone_list():
    print("loading")
def show_phones():
    show_phone(phone_header,"")
    index=1
    for phone in phones:
        show_phone(phone,index)
        index=index+1
    print()
def show_phone(phone,index):
    outputstr="{0:>3} {1:<20} {2:>16}"
    print(outputstr.format(index, phone[name_pos],phone[phone_pos]))
def create_phone():
    print("Enter data for a new phone:")
    newname=input("Enter name:")
    newphone_num=input("Enter a phone number: ")
    phone=[newname,newphone_num]
    phones.append(phone)
    print()
def menu_choice():
    print("Choose one of the following options?")
    print("    s) Show")
    print("    n) New")
    print("    d) Delete")
    print("    e) Edit")
    print("    q) Quit")
    choice=input("Choice: ")
    if choice.lower() in ['n','s','d','e','q']:
        return choice.lower()
    else:
        print(choice+"?"+" That is an invalid option!!!")
        return None
def main_loop():
    load_phone_list()
    while True:
        choice=menu_choice()
        if choice==None:
            continue
        if choice=='q':
            print("Exiting...")
            break
        elif choice=='n':
            create_phone()
        elif choice=='d':
            which=input("Which item do you want to delete?")
            print("which is",which)
            delete_phone(which)
        elif choice=='s':
            show_phones()
        elif choice =='e':
            which=input("Which item do you want to edit?")
            print("which is",which)
            edit_phone(which)
        else:
            print("Invalid choice")
    save_phone_list()
if __name__=='__main__':
    main_loop()
#%%
import csv
import os
phones=[]
name_pos=0
phone_pos=1
phone_header=['Name', 'Phone Number']
def proper_menu_choice(which):
    if not which.isdigit():
        print("'"+which+"'needs to be the number of a phone!")
        return False
    which=int(which)
    if which < 1 or which > len(phones):
        print("'"+str(which)+"'needs to be the number of a phone!")
        return False
    return True
def delete_phone(which):
    if not proper_menu_choice(which):
        return
    which=int(which)
    del phones[which-1]
    print("Deleted phone #",which)
def edit_phone(which):
    if not proper_menu_choice(which):
        return
    which=int(which)
    phone=phones[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    print(phone[name_pos])
    newname=input("Enter phone name to change or press return: ")
    if newname=="":
        newname=phone[name_pos]
    print(phone[phone_pos])
    newphone_num=input("Enter new phone number to change or press return: ")
    if newphone_num=="":
        newphone_num=phone[phone_pos]
    phone=[newname,newphone_num]
    phones[which-1]=phone
    print("Editing")
def save_phone_list():
    f=open("myphones.csv",'w',newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
    print("Saving")
def load_phone_list():
    if os.access("myphones.csv",os.F_OK):
        f=open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()
    print("loading")
def show_phones():
    show_phone(phone_header,"")
    index=1
    for phone in phones:
        show_phone(phone,index)
        index=index+1
    print()
def show_phone(phone,index):
    outputstr="{0:>3} {1:<20} {2:>16}"
    print(outputstr.format(index, phone[name_pos],phone[phone_pos]))
def create_phone():
    print("Enter data for a new phone:")
    newname=input("Enter name:")
    newphone_num=input("Enter a phone number: ")
    phone=[newname,newphone_num]
    phones.append(phone)
    print()
def menu_choice():
    print("Choose one of the following options?")
    print("    s) Show")
    print("    n) New")
    print("    d) Delete")
    print("    e) Edit")
    print("    q) Quit")
    choice=input("Choice: ")
    if choice.lower() in ['n','s','d','e','q']:
        return choice.lower()
    else:
        print(choice+"?"+" That is an invalid option!!!")
        return None
def main_loop():
    load_phone_list()
    while True:
        choice=menu_choice()
        if choice==None:
            continue
        if choice=='q':
            print("Exiting...")
            break
        elif choice=='n':
            create_phone()
        elif choice=='d':
            which=input("Which item do you want to delete?")
            print("which is",which)
            delete_phone(which)
        elif choice=='s':
            show_phones()
        elif choice =='e':
            which=input("Which item do you want to edit?")
            print("which is",which)
            edit_phone(which)
        else:
            print("Invalid choice")
    save_phone_list()
if __name__=='__main__':
    main_loop()        
    
        
            

