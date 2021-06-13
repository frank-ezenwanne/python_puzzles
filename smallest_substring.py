#This program find the smallest substring in a group of characters that contain all the xters on request.
#e.g looking for the substring in "doghouse" that contains "he" should return "house"
#The first string entered is the total string
#The 2nd string entered is the group of xters in question

A = input("input the first string, A\n")     #accepts inputs of strings
B = input("input the second string, B\n")
result = []    #will contain list of substrings of the same sizes
a = list(A)    #make all characters of the string into single iterable elements
b = list(set(B))    #Same as above but made with "set" to avoid duplicates,errors..quality not quantity.
assert len(a) >= len(b),"String B has more characters than string A"    #doesn't make any sense if b is more than a..
len_a = len(a)    #len_a is length of string a
len_b = len(b)
while len_b <= len_a:    #Loops until len_b variable is greater than len_a.
    beg = 0     #index of first character of substring 
    end = len_b     #index of last character of substring
    while end <= len_a:    #loops until index of last character is the last of indices in the list
        for char in b:    # Checks if every character in list b is present in the current substring under check
            if char not in a[beg:end]:   #exits loop if character in list b is not in the current substring under check
                break
            else:
                if char == b[len(b)-1]:      #checks if current character is list b's last character
                    substring = "".join(a[beg:end])      #joins pieces of substring characters back into a complete substring
                    if substring not in result:          #Appends to "result"
                        result.append(substring)
        beg += 1                                   #increments to move to the next substring set
        end += 1
    if result:                                  #prints substrings if any exist
        for res in result:
            print("".join(res))
        break                           #breaks out of above while loop if least size substring(s) have already been derived.
    len_b += 1              #if no values at this stage, then length of substrings being checked increases by one character and loops again
if not result:              #if nothing still at the end of all loops, give the word...NO SUBSTRING FOUND 
    print("no substring found")       
                                         

        
    

     
    

                  

