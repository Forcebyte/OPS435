#!/usr/bin/env python3
#First question mainly relies on calculating a child benefit, where the formula is given and you have to fix this code
#Here is the correct code modifications I made

#Original Definitions for the benefit values
ccb_u6 = 541
ccb_6to17 = 456

#Ask for input for the number of children aged under 6, and 6-17 respectively, store in seperate variables
child_u6 = int(input('What is the number of child under the age of 6? '))
child_6to17 = int(input('What is the nuber of child aged 6 to 17? '))

#Add the total in two seperate variables as its cleaner
ccb_childu6total = (ccb_u6 * child_u6)
ccb_child6to17total = (ccb_6to17 * child_6to17)

#Add the two totals to get your main total
ccb_total = ccb_childu6total + ccb_child6to17total

#Print the total to the customer, using ccb_total
print('The total Canada Child Benefit for the family is ' + str(ccb_total))
