# STRING SLICING
name = "govind"
print (name[0:3]) # it represent that  0 (0th index isincluded) to 3 (3rd index is exculded)

# NEGATIVE SLICING
name = "govind" # in negative slicing index would start from last character to first character (-1,-2,-3,-4...)
print(name[-4:-1]) # at here name = "govind" index start from (-6,-5,-4,-3,-2,-1) to("govind") respectively to the string order

# ADVANCE TECHNIQUE OF STRING SLICING
name = "govind"
print(name[:5]) # it represent print(name[0:5])
print(name[0:]) # it represent print(name[0:(string length)]) eg. here in my case it would be print(name[0:6])

# STRING SLICING BY SKIPING VALUE
name = "govind"
print(name[1:5:2]) # it represent that slice string to [1:5] and skip 2 index from that value at every interval
