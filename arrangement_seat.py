# -*- coding: UTF-8 -*-
import random

array = []
table = [[],[],[],[],['office-Sarah','office-Flora','market-Mia','market-Leo','market-Salina','editor-wenming','tech-Doris','tech-renren','tech-Bryan',]]
table_count = 4
staff = [['ads-Mary','ads-Athena','ads-Winnie'],
         ['market-Maggie','market-Miley','market-Tracy','market-vivi','market-junior','market-Ariel'],
         ['editor-Hans','editor-Mary','editor-Kelvin','editor-Alex','editor-Justin','editor-Shirley','editor-Sarah','editor-Arlena','editor-jiayin'],
         ['tech-Patrick','tech-xiayang','tech-Shawn','tech-Max','tech-linan','tech-Simon','tech-Kevin','tech-Alice','tech-Conan','tech-Govia','tech-Eric','tech-Mark'],
         ['journalist-1','journalist-2','journalist-3','journalist-4','journalist-5','journalist-6','journalist-7','journalist-8','journalist-9','journalist-10','pt-1','pt-2','pt-3','pt-4','pt-5']]

def shuffle_table(str):
    "This function for shuffle"
    for key_0 in str:
        random.shuffle(key_0)
        for key_1 in key_0:
            array.append(key_1)
    return

def assign(str):
    "This function for assign table(reminder)"
    for key_2 in str:
        reminder = str.index(key_2) % table_count
        if reminder ==0:
            table[0].append(key_2)
        elif reminder == 1:
            table[1].append(key_2)
        elif reminder == 2:
            table[2].append(key_2)
        elif reminder == 3:
            table[3].append(key_2)

    return

shuffle_table(staff)
assign(array)

print 'table1 is:',table[0]
print 'table2 is:',table[1]
print 'table3 is:',table[2]
print 'table4 is:',table[3]
print 'table5 is:',table[4]
print len(staff[0])+len(staff[1])+len(staff[2])+len(staff[3])+len(staff[4])