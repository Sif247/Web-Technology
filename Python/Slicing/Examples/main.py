#######################     Slicing      ########################

#1.  slicing[inclusive, not inclusive]
#                 ^             ^
#                 |             |
#              from e1,      to e2 (- 1)
# "Start from the first param (inclusive) and take all until the second one (not inclusive) "
#                              ---------                                      ------------

#       0        1      2      3      4      5
l1 = ["hello", "world", "my", "name", "is", "isma"]

print(l1[1:5])
#            1     2    3    4
#output:   [world, my, name, is]

#################################################################

#2.  slicing[inclusive: (until the end of the list)]

print(l1[3:])

#            3    4    5
#output:   [name, is, isma]

############################################################

#3.  slicing[(start with the first element of List): not inclusive]

print(l1[:4])

# start 0 end 4(-1)
#             0      1    2    3
#output:   [hello, world, my, name]

############################################################

#4.  slicing[:] -> All elements


l2 = l1[:]
print(l2)

#  from 0 until the end (5 in this case)
#output:  [hello, world, my, name, is, isma]

###############################################################

#h.  slicing[:: jump] -> start from first element and jump every time of "jump" steps
#                |                                                         |
#                 ---------------------------------------------------------


l2 = l1[::2]
print(l2)

#  from 0 and jump 2 steps (one yes one no)

#             yes   no    yes  no   yes   no
#process:  [hello, world, my, name, is, isma]
#output:   [hello, my, is]

############################################################

#6.  slicing[i][start:end] -> just one element, number[i], and do the slicing of letters

print(l1[1][1:4])

#                 start         finish(4-1)
#           0       1       2       3          4
#process:  [w,      o,      r,      l,        d]
#output:   [orl]

###############################################################
