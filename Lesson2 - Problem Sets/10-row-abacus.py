#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    # 4 STAR SOLUTION
    s = "00000*****"
    for i in "0"*(10-len(str(value))) + str(value):
        print "|" + s[0:10-int(i)] + " "*3 + s[10-int(i):] + "|"
    
    # 4 STAR SOLUTION (2-liner)
    # for i in "0"*(10-len(str(value))) + str(value):
    #     print "|" + "00000*****"[0:10-int(i)] + " "*3 + "00000*****"[10-int(i):] + "|"
    
    
    # 3 STAR SOLUTION
    # s = "00000*****"
    # val = str(value)
    # val = "0"*(10-len(val)) + val
    # for i in val:
    #     print "|" + s[0:9-int(i)] + " "*3 + s[9-int(i)+1:] + "|"
    
    
    # 1 STAR (first attempt)
    # s = "00000*****"
    # val = str(value)
    # l = len(val)
    # row = 0
    # while (row<10):
    #     x = 10-l
    #     if (row>=x):
    #         i = int(val[row-x])
    #         if (i>0):
    #             print "|" + s[0:10-i] + " "*3 + s[10-i:] + "|"
    #         else:
    #             print "|" + s + " "*3 + "|"
    #     else:
    #         print "|" + s + " "*3 + "|"
    #     row+=1
            

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|