#https://projecteuler.net/problem=17

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

#Finds or constructs and returns the string representing two digits (tens)
def getTens(n):
    strng = ''
    
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
        
    #The tens digit is 2 through 9: set strng to "twenty" through "ninety"
    elif (n / 10 == 2):
        strng = 'twenty'
    elif (n / 10 == 3):
        strng = 'thirty'
    elif (n / 10 == 4):
        strng = 'forty'
    elif (n / 10 == 5):
        strng = 'fifty'
    elif (n / 10 == 6):
        strng = 'sixty'
    elif (n / 10 == 7):
        strng = 'seventy'
    elif (n / 10 == 8):
        strng = 'eighty'
    elif (n / 10 == 9):
        strng = 'ninety'
    
    #Append the word representing the ones digit to strng (strng is '' if the tens digit is 0)
    strng += getDigits(n % 10)
    
    return strng

#Constructs and returns the string representing three digits (hundreds)
def getHundreds(n):
    strng = ''
    
    '''
    The hundreds digit is greater than 0: set strng to the word representing the hundreds digit and
    append 'hundred'
    '''
    if (n / 100 > 0):
        strng += getDigits(n / 100)
        strng += 'hundred'
        
        #The two tens digits are not 00: append 'and' to strng
        if (n % 100 > 0):
            strng += 'and'
            
    #Append the string representing the tens digits to strng (strng is '' if the hundreds digit is 0)
    strng += getTens(n % 100)
    
    return strng
        
'''
Constructs and returns the string representing n
Method:
Given a number, n, starting with i = 0, increment i while n is smaller than 10**(3*i). Each iteration,
prepend the name of the unit of magnitude represented by 10**(3*i) to strng. Then prepend the string
representing the three digits within that unit of magnitude (i.e.: xxx, 456, xxx is "fourhundredand-
fiftysix") to strng. Thus, strng grows from right to left into the string representing n.
Observation:
Since every number can be represented as the conjunction of a substring representing the current unit
of magnitude and a substring representing a number of smaller magnitude (i.e.: 9 123 is the
conjunction of "ninethousand" and "onehundredandtwentythree"), caching results can speed up
construction of strings representing numbers of greater magnitude. Furthermore, since every unit of
magnitude contains the substring representing the three digits within the unit, caching just these
substrings can still speed up construction. The latter requires significantly less memory than the
former.
'''
def getNumString(n):
    
    '''
    Names for the ascending units of magnitude (i.e.: the 10**0 unit has no name but the 10**3 unit
    is called "thousand")
    '''
    UNITS = ['', 'thousand', 'million']
    
    strng = ''
    i = 0
    while ((n >= 10**(3*(i)))):
        
        #(n % (10**(3*(i + 1)))) / (10**(3*i)) are the digits between 10**(3*(i + 1)) and 10**(3*i)
        if ((n % (10**(3*(i + 1)))) / (10**(3*i)) != 0):
            strng = UNITS[i] + strng
            strng = getHundreds((n % (10**(3*(i + 1)))) / (10**(3*i))) + strng
            
        i += 1
    return strng

'''   
Finds the total number of letters in the strings representing the numbers between 1 and n, inclusive,
and returns the value
'''
def getNumLetters(n):
    sumLetters = 0
    for i in xrange(1, n + 1):
        strng = getNumString(i)
        sumLetters += len(strng)
    return sumLetters
    
print getNumLetters(1000)