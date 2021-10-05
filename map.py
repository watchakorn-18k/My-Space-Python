question = [
            'No, Stop',
            '    2+   3 = 1        ',
            'what do you want?  ',
            'why you leave me ???',
            '1 '
]
print('--- map ---')
#----# USE MAP #----#
q_map = list(map(lambda q: q.strip(), question ))
            #^^---------^--^---------------^^
print(q_map)

#----# LIST ONE-LINED  #----#


clean_q = [q for q in question]
        #--^-----------------^


clean_q = [q.strip() for q in question]
print(clean_q)


#----# END #----#
print('--- end map ---')

