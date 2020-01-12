# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:09:48 2017

@author: HP
"""

#%%
x,y=3,4
print(x,y)
#%%
a,b,c=10,11,12
print(b)
#%%
4,6,8
#%%
tup=('a','e','i','o','u')
#%%
print("tup is", tup)
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[-2])
print(tup[1:3])
print(tup[:3])
#%%
d={"Johnny": "5 years old", "Sally": "7 years old", "Eva": "10 years old", 
   "Peggy": "7 years old"}
#%%
for key,value in d.items():
    print(key, "--> ", value)
#%%
for item in d.items():
    print(item)
#%%
for item in d.items():
    print(item)
    print(item[0], "--> ", item[1])
#%%
for item in d.items():
    print(item[0], "--> ", item[1])
#%%
for key in d:
    print(key, "--> ",d[key])
#%%
for key in d.keys():
    print(key, "--> ", d[key])
#%%
for value in d.values():
    print(value)
#%%
ascars={"Ford": "Mustang","Mazda": "Miata","Scion": "FR-S","Subaru": "BRZ","Dodge":
    "Challenger","Nissan": "370Z","Chevy": "Camaro","Hyundai": "Genesis Coupe",
    "MINI Copper": "Roadster"}
#%%
for value in ascars.values():
    print(value)
#%%
for key in ascars.keys():
    print(key)
#%%
namelist=["George", "Sally", "Catherine", "James", "Peggy"]
x,y,z="George", "Sally","Catherine"
mytuple=x,y,z
agedict={"George": "17","Sally": "19","Catherine": "18"}
#%%
def print_file(filename):
    infile = open(filename)
    for line in infile:
        print(line, end=" ")
    infile.close()
#%%
def copy_file(infilename, outfilename):
    infile = open(infilename)
    outfile = open(outfilename, 'w')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()
#%%
def write_to_file(filename, myname, myage, major):
    outfile = open(filename, 'w')
    outfile.write("My name is "+myname+" \n")
    outfile.write("My age is "+str(myage)+" \n")
    outfile.write("I am majoring in "+major+" \n")
    outfile.close()
#%%
""" cd documents/pythoncoursera/lesson3
python hello.py
dir
dir hello*.py
cd ..
cd lesson3
"""
#%%
print("Hello World")
#%%
import sys # we need this library to deal with operating system
filename=sys.agrv[1]
infile=open(filename)
for line in infile:
    print(line,end="")
infile.close()
#%%
def copy_file1(infilename,outfilename):
    """ Opens two files and copies it into the other line by line """
    infile=open(infilename)
    outfile=open(outfilename,'w')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()
#%%
import sys
infilename=sys.argv[1]
outfilename=sys.argv[2]
""" Opens two files and copies it into the other line by line """
infile=open(infilename)
outfile=open(outfilename,'w')
for line in infile:
    outfile.write(line)
infile.close()
outfile.close()
#%%
import sys
filename=sys.argv[1]
# print("\n",filename,"\n")
text_file=open(filename)
linect=0
wordct=0
charct=0
for line in text_file:
    linect=linect+1
    for word in line.split():
        wordct=wordct+1
    charct=charct+len(line)
text_file.close()
print(linect,wordct,charct)
# python lwc.py xxx.txt
# type xxx.txt
#%%
def count_words(filename):
    text_file = open(filename)
      # Set up an empty dictionary to start a standard design pattern loop
    words_dic = {}
    
    # This loop adds each word to the dictionary and updates its count. Change 
    # all words to lower case so Horse and horse are seen as the same word.
    for line in text_file:
        for word in line.lower.split():
            word=word.strip("'?,.;!-/\"")
            if word not in words_dic:
                words_dic[word]=0
            words_dic[word]=words_dic[word]+1
            text_file.close()
     # Sorts the dictionary words into a list and then print them out
    print("List of words in the file with number of times each appear")
    word_list=sorted(words_dic)
    for word in word_list:
         print(words_dic[word],word)
#%%
import sys
filename = sys.argv[1]
text_file = open(filename)
      # Set up an empty dictionary to start a standard design pattern loop
words_dic = {}
for line in text_file:
    for word in line.lower.split():
        word=word.strip("'?,.;!-/\"")
        if word not in words_dic:
                words_dic[word]=0
                
                words_dic[word]=words_dic[word]+1
                text_file.close()
     # Sorts the dictionary words into a list and then print them out
print("List of words in the file with number of times each appear")
word_list=sorted(words_dic)
for word in word_list:
         print(words_dic[word],word)
#%%
import csv
def read_csv_file(filename):
    f=open(filename)
    for row in csv.reader(f):
        print(row)
    f.close()
#%%
import csv
def read_csv_file1(filename):
    f=open(filename)
    data=[]
    for row in csv.reader(f):
        data.append(row)
    print(data)
    f.close()
#%%
import csv
def read_csv_file2(filename):
    f=open(filename)
    for row in csv.reader(f):
        print(row[0],row[1],row[2])
    f.close()
#%%
def write_csv(filename):
    import csv
    L=[['Date','Name','Notes'],
       ['2016/1/18','Martin Luther King Day','Federal Holiday'],
       ['2016/2/2','Groundhog Day','Observance'],
       ['2016/2/8','Chinese New Year','Obeservance'],
       ['2016/2/14','Valentine\'s Day','Observance'],
       ['2016/5/8','Mother\'s Day','Observance'],
       ['2016/8/19','Statehood Day','Hawaii Holiday'],
       ['2016/10/28','Nevada Day','Nevada Holiday']]
    f=open(filename,'w',newline='')
    for item in L:
        csv.writer(f).writerow(item)
    f.close()
#%%
def name_phone(csv_filename):
    import csv
    f=open(csv_filename,'w',newline='')
    while True:
        nextname=input("Enter a friend's name, press return to end: ")
        if nextname=="":
            break
        nextphone=input("Enter your friend's phone number: ")
        print(nextname)
        print(nextphone)
        data=[]
        data.append(nextname)
        data.append(nextphone)
        csv.writer(f).writerow(data)
    f.close()
#%%
def update_csv(old_name,new_name):
    import csv
    fin=open(old_name)
    fout=open(new_name,'w',newline='')
    ct=0
    tot_weight=0.0
    for row in csv.reader(fin):
        if row[0]!="Date":
            ct=ct+1
            tot_weight=tot_weight+float(row[1])
        csv.writer(fout).writerow(row)
    row=["Average",tot_weight/ct]
    csv.writer(fout).writerow(row)
    fin.close()
    fout.close()
        