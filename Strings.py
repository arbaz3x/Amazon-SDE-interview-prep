def word_count(str):
    words = str.split() # split the string into words

    count = dict() # create a dictionary to store the word count

    for word in words:
        if word in count:
            count[word] += 1 # if word is already present , increment it
        else:
            count[word] = 1  # if it is not present , add it

    return count
def letter_count(str):

    count = dict() #creates a dictionary to store the letter count

    for letter in str:         
        if letter in count:
            count[letter] += 1  # checking if it is present , then increment
        else :
            count[letter] = 1  # if it is not present then add it
    return count        

#word_count("Hello World")
#print(word_count("Hello World Hello"))
#print(letter_count('hello'))

# sorts words in comma separated string alphanumerically

def sort_words(str):
    words = str.split(',')
    words.sort()
    return ','.join(words)

#print(sort_words('python,java,perl,php')) 

# sorting strings in comma separated strings
def sort_string(str):
    words = str.split(',')
    sorted_words = sorted(words, key=lambda x: (x.isdigit(), x))
    return ','.join(sorted_words)

#print(sort_string('python,java,perl,php,123,456,abc,789'))

#validate an IP address 
#ipv4

def valid_ip(ip_string):
    ip = ip_string.split('.')
    if len(ip) != 4:
        return False
    for i in ip:
        if not ip or (len(i) > 1 and i[0] == '0'):
            return False
        if not i.isdigit() or int(i) < 0 or int(i) > 255:
            return False #improve this using try except
    return True

#X=input("Enter an IP address: ")
#print(valid_ip(X))

#multiply large numbers as strings

def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    n1 = len(num1)
    n2 = len(num2)
    result = [0] * (n1 + n2)
    for i in range(n1 -1 ,-1,-1):
        for j in range(n2 -1 ,-1 ,-1):
            mul = (ord(num1[i]) - ord('0'))* (ord(num2[j])-ord('0'))
            pl = i+ j
            ph = i+j+1
            sum = mul + result[ph]
            result[pl] += sum // 10
            result[ph] = sum % 10
    result = ''.join(map(str,result))
    return result.lstrip('0')

#print(multiply('4154','51454'))

#convert a string to integer without inbuilt ftns
# 
def atoi(str)->int:
    result = 0
    sign = 1
    i = 0
    if str[0]== '-':
        sign = -1
        i=1
    for i in range (i ,len(str)):
            if str[i] < '0' or str[i] > '9':
                return 0
            if not str[i].isdigit():
                return 0
            result = result * 10 + (ord(str[i]) - ord('0'))
            
    return sign * result
            

#print(atoi('-128282882828828')) 
              
#Longest substring without repeating characters
# sliding window approach
# Time complexity O(n)
# Space complexity O(min(m,n))

def longest_substring(s):
    n = len(s)
    ans = 0
    mp = {}
    i = 0
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)
        ans = max(ans ,j-i+1)
        mp[s[j]] = j+1
    return ans       

print(longest_substring('abcabcbbabc'))      