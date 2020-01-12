# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:48:33 2017

@author: HP
"""

#%%
lis = ["a","b","c","d","e","f"]
#%%
def who_is_there(lis):
    if "bear" in lis:
        print("There is a bear.")
    if "lion" in lis:
        print("There is a lion.")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers.")
    if "daisy" in lis and "iris" in lis:
        print("There are at least two flowers.")
    if "donkey" in lis:
        print("There is a donkey.")
    if "horse" not in lis:
        print("There is no horse in the list.")
    print("The list has",len(lis),"items.")
#%%
alion = ['lion']
ld = ['lion','daisy']
lbf = ['lion','bear','iris']
#%%
lis = ["a","b","c","d","e","f"]
lis1 = ["a","b","a","r","c","a","a"]
#%%
def count_a(alist):
    ct = 0
    for let in alist:
        if let == 'a':
            ct = ct + 1
    print("There are",ct,"letter a's in the list.")
#%%
nlis = [2,4,8,105,210,-3,47,8,33,1]
rlis = [3.14,7.26,-4.76,0,8.24,9.1,-100.7,4]
#%%
def average(numlis):
    ct = 0
    for i in range(0,len(numlis)):
        ct = ct + numlis[i]
        print(numlis[i])
    average = ct/len(numlis)
    print("average is",average,"its count is",len(numlis))
#%%
newEngland = ["Maine","New Hamsphire","Vermont","Rhodes Island","Massachusetts",
              "Connecticut"]
def for_state(slis):
    for state in slis:
        print(state)
#%%
letter_list = ['a','b','c']
cap_list = ['A','B','C','D']
misc_list = ['ball',3.14,-50,'university','course']
#%%
def print_list(lis):
    for item in lis:
        print(item)
#%%
x = 17
y = 3.14
z = "The Walrus and the Carpenter"
z1 = "30"
z2 = '40'
vowels = ['a','e','i','o','u']
nums = ['1','2','3','3.14']
phrases = ["'Twas brillig, and the slithy toves",
           "Did grye and gimble in the wabe:"]
r = True
s = False
#%%
def multiply():
    numstr1 = input("Enter a number: ")
    numstr2 = input("Enter another number: ")
    num1 = float(numstr1)
    num2 = float(numstr2)
    print("Their product is ", num1*num2)
#%%
print(list(range(2,20,3)))
print(range(2,20,3))
#%%
print(12345678)
print(12,345,678)
#%%
newEngland = [["Massachusetts", 6692824],["Connecticut",3596080],["Maine",1328302],
["New Hamsphire",1323459],["Rhode Island",1051511],["Vermont",626630]]
def for_states(state_list):
    for state in state_list:
        print(state)
#%%
print(newEngland[0])
print(newEngland[1])
state = newEngland[1]
print(state)
print("population:",state[1],"     name:",state[0])
print(newEngland[1][0])
print(newEngland[1][1])
#%%
newEngland = [["Massachusetts", 6692824],["Connecticut",3596080],["Maine",1328302],
["New Hamsphire",1323459],["Rhode Island",1051511],["Vermont",626630]]
def report1(state_data):
    print("Population        State")
    for state_item in state_data:
        print(state_item[1],"         ",state_item[0])
#%%
midAtlantic = [["New York",19746227],["New Jersey",8938175],["Pennsylvania",12787209]]
#%%
newEngland = [["Massachusetts", 6692824],["Connecticut",3596080],["Maine",1328302],
["New Hamsphire",1323459],["Rhode Island",1051511],["Vermont",626630]]
def report2(state_data):
    print("Population        State")
    for i in range(0,len(state_data)):
        print(state_data[i][1],"        ",state_data[i][0])
#%%
newEngland = [["Massachusetts", 6692824],["Connecticut",3596080],["Maine",1328302],
["New Hamsphire",1323459],["Rhode Island",1051511],["Vermont",626630]]
def population(state_data):
    sum_ =  0
    num_states = len(state_data)
    for i in range(0,num_states):
        one_state = state_data[i]
        pop = one_state[1]
        sum_ = sum_ + pop
    print("The total population of this list is",sum_)
    print("There are",num_states,"in this list of states")
#%%
def population1(state_data):
    population =1
    sum_ = 0
    num_states = len(state_data)
    for state in range(0,num_states):
        sum_ = sum_ + state_data[state][population]
    print("The total population of this list of states is",sum_)
    print("There are",num_states,"states in this list of states.")
#%%
numlis = [65,44,3,56,48,74,7,97,95,42]
numlis2 = [4,6,8,12,2,7,19]
def average1(nlis):
    sum_ = 0
    num_states = len(nlis)
    for i in range(0,num_states):
        print(nlis[i],end=" ")
        sum_ = sum_ + nlis[i]
    average = sum_/num_states
    print()
    print("the average is",average)
#%%
def average2(nlis):
    sum_ = 0
    for num in nlis:
        sum_ = sum_ + num
        print(num,end = " ")
    print()
    print("average is",sum_/len(nlis))
#%%
import random
#%%
print(random.random())
#%%
print(random.randint(3,8))
#%%
import random
verbs = ["goes","cooks","shoots","faints","chews","screams"]
nouns = ["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs = ["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles = ["a","the","that","this"]
def sentence():
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    print(our_sentence)
#%%
import random
verbs = ["goes","cooks","shoots","faints","chews","screams"]
nouns = ["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs = ["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles = ["a","the","that","this"]
def simple_poem():
    for i in range(4):
        article = random.choice(articles)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)
    
        our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
        our_sentence = our_sentence.capitalize()
        print(our_sentence)
#%%

        
     