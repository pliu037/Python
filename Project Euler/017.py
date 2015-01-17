#https://projecteuler.net/problem=17

'''
Names for the ascending units of magnitude (i.e.: the 10**0 unit has no name but the 10**3 unit is
is called "thousand")
'''
UNITS = ['', 'thousand', 'million'] 

#Finds and returns the word representing a digit; 0 is represented by ''
def getDigits(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    else:
        return ''

#Finds or constructs and returns the word(s) representing the two "tens" digits
def getTens(n):
    word = ''
    
    #The tens digit is 1: return "ten" through "nineteen" as the ones digit ranges from 0 through 9
    if (n / 10 == 1):
        if (n % 10 == 1):
            return 'eleven'
        elif (n % 10 == 2):
            return 'twelve'
        elif (n % 10 == 3):
            return 'thirteen'
        elif (n % 10 == 4):
            return 'fourteen'
        elif (n % 10 == 5):
            return 'fifteen'
        elif (n % 10 == 6):
            return 'sixteen'
        elif (n % 10 == 7):
            return 'seventeen'
        elif (n % 10 == 8):
            return 'eighteen'
        elif (n % 10 == 9):
            return 'nineteen'
        else:
            return 'ten'
        
    #The tens digit is 2 through 9: set word to "twenty" through "ninety"
    elif (n / 10 == 2):
        word = 'twenty'
    elif (n / 10 == 3):
        word = 'thirty'
    elif (n / 10 == 4):
        word = 'forty'
    elif (n / 10 == 5):
        word = 'fifty'
    elif (n / 10 == 6):
        word = 'sixty'
    elif (n / 10 == 7):
        word = 'seventy'
    elif (n / 10 == 8):
        word = 'eighty'
    elif (n / 10 == 9):
        word = 'ninety'
    
    #Append the word representing the ones digit to word (word is '' if the tens digit is 0)
    word += getDigits(n % 10)
    
    return word

#Constructs and returns the word(s) representing the three "hundreds" digits
def getHundreds(n):
    word = ''
    
    '''
    The hundreds digit is greater than 0: set word to the word representing the hundreds digit and
    append 'hundred'
    '''
    if (n / 100 > 0):
        word += getDigits(n / 100)
        word += 'hundred'
        
        #The two tens digits are not 00: append 'and' to word
        if (n % 100 > 0):
            word += 'and'
            
    #Append the word(s) representing the tens digits to word (word is '' if the hundreds digit is 0)
    word += getTens(n % 100)
    
    return word
        
'''
Constructs and returns the word(s) representing n
Method:

'''
def getWords(n):
    word = ''
    i = 0
    while ((n >= 10**(3*(i)))):
        if ((n % (10**(3*(i + 1)))) / (10**(3*i)) != 0):
            word = UNITS[i] + word
            word = getHundreds((n % (10**(3*(i + 1)))) / (10**(3*i))) + word
        i += 1
    return word

'''   
Finds the total number of letters in the words representing the numbers between 1 and n, inclusive,
and returns the value
'''
def getNumLetters(n):
    sumLetters = 0
    for i in xrange(1, n + 1):
        print getWords(i)
        sumLetters += len(getWords(i))
    return sumLetters
    
print getNumLetters(1000)