



def lemma3Exists(m,n,matrix):

    if (m == n):
    # case 1: square matrix
        # initialize top mapping array
        # initialize bottom mapping array
        #


# 0 : 0 1 0 0 0 1 0 1
# 1 : 1 0 1 1 0 0 0 0
# 2 : 0 1 0 1 1 0 1 0
# 3 : 1 0 0 1 0 1 0 0


#strategy - lemma 3 case 1,
#iterate through rows - we are looking for (0, 1) pattern
# initialize X_current = {0 .. n}
# for each row (from middle to top or middle to bottom of M): [O(m/2)]
#   X = {}
#   iterate through elements 0..n to get A0, A1 [O(n)]
#   for S in X_current: [O(?)]
#       S0 = A0.intersection(S)
#       S1 = A1.intersection(S)
#       for all in S0:
#           for all in S1:
#               map(S0, S1) //mapping not yet worked out, notes below
#       if(len(S0)) >= 2:
#           X.add(S0)
#       if(len(S1)) >= 2:
#           X.add(S1)
#   X_current = X


# ideas:
# X could be a queue containing sets. At the beginning of every loop through
# a new row we check its size then go through it that many times. might
# take less time than making new empty set every time we loop?





# row 3
# X = { {0 1 2 3 4 5 6 7} }
# A0 = { 1 2 4 6 7 }, A1 = { 0 3 5 }

# One set in X: S = {0 1 2 3 4 5 6 7}
# S0 = { 1 2 4 6 7 }, S1 = { 0 3 5 }
# 15 mappings done

# row 2
# X = { S_A = { 1 2 4 6 7 }, S_B = { 0 3 5 } }
# A0 = { 0 2 5 7 }, A1 = { 1 3 4 6 }

# S_A:
# S0 = S_A cap A0 = { 2 7 }, S1 = { 1 4 6 }
# 6 mappings done


# S_B:
# S0 = S_B cap A0 = { 0 5 }, S1 = { 3 }
# 2 mappings done

# row 1
# X = { S_A = { 2 7 }, S_B = { 1 4 6 }, S_C = { 0 5 } }
# A0 = { 1 4 5 6 7 }, A1 = { 0 2 3 }

# S_A:
# S0 = { 7 }, S1 = { 2 }
# 1 mapping done

# S_B:
# S0 = { 1 4 6 }, S1 = { }
# 0 mappings done

# S_C:
# S0 = { 5 }, S1 = { 0 }
# 1 mapping done

# row 0
# X = { {1 4 6} }
# A0 = { 0 2 3 4 6 }, A1 = { 1 5 7 }
# One set in X:  S = {1 4 6}
# S0 = { 4 6 }, S1 = { 1 }
# 2 mappings done

# reached the end
# X = { {4 6} } // note columns 4 and 6 are the same
# 27 mappings done

# ---

# total of 27 mappings done
# if there are n columns in topMatrix, the number of possible combinations of different indices is ( n! ) / ( 2 * (n - 2)! )




# what kind of mapping?

#lets say we're on row 2
# S0 = S_A cap A0 = { 2 7 }, S1 = { 1 4 6 }

# make mapping for {2 1}
# check out the link i put in google doc - might be a good lead






# would anything change if the matrix has an odd number of rows? topMatrix and bottomMatrix would have to have different numbers of rows

# note: in the paper it is given that S cap A0 = S0, S cap A1 = S1 for each S.
# When working through this example I used SA, SB etc to keep track of multiple S for each row.
# i.e. i got an S0 and an S1 for each SA, SB, SC etc
