question = [
            'No, Stop',
            '    2+   3 = 1        ',
            'what do you want?  ',
            'why you leave me ???',
            '1 '
]
clean_q = [q.strip() for q in question]


#----# USE Filter #----#
print('--- filter ---')
q_filter = list(filter(lambda q: len(q)  >=6, clean_q))
print(q_filter)


#----# LIST ONE-LINED  #----#

q_filter = [q for q in q_filter if len(q) >= 6]
print(q_filter)


#----# END #----#
print('--- end filter ---')