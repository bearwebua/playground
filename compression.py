import sys

def compression(chars:str)->str:
    # Time complexity is linear
    # We need to go through the whole string, so it is O(n)
    output = ''
    i = 0
    if not type(chars) is str or not chars:
        return ''
    while (i < len(chars)):    
        cur_count = 0
        cur_symbol = chars[i]
        if  i+1 < len(chars) and chars[i] == chars[i+1]:  # if chars are the same AND  we are not on the last char
            cur_count += 2
            for j in range(i+1,len(chars)):  # move in the string until chars do not match anymore, then move the cursor(i)
                if  j+1 == len(chars) or chars[j] != chars[j+1]:  # if chars are not the same OR we are on the last char
                    i = j+1  # moving i in string since we reviewed this char already
                    break
                else:  # can remove this "else" -> but better for visibility/readability to leave it
                    cur_count += 1
            output = output + cur_symbol + str(cur_count)           
        else:
            output = output + cur_symbol 
            i += 1        
    return output

print(compression(sys.argv[1]))    

# assert compression ('abcaaabbb') == 'abca3b3'
# assert compression ('abcd') == 'abcd'
# assert compression ('a') == 'a'
# assert compression ('') == ''
# assert compression ('aaabaaaaccaaaaba') == 'a3ba4c2a4ba'
# assert compression ('abcaaabbbxwqqqqqqqwqqqqq') == 'abca3b3xwq7wq5'

# example: `$ python3 compression.py "aaabaaaaccaaaaba"`
