#https://projecteuler.net/problem=97

#Finds and returns the last <digits> digits of p*2**e + s
def findDigitsExpression(digits, s, p, e):
    add = bin(e)[2:]
    currentProduct = 1
    currentPower = 2
    for i in xrange(len(add)):
        if add[len(add) - 1 - i] == '1':
            currentProduct *= currentPower
            currentProduct %= 10**digits
        currentPower *= currentPower
        currentPower %= 10**digits
    currentProduct *= p
    currentProduct += s
    currentProduct %= 10**digits
    return currentProduct

print findDigitsExpression(10, 1, 28433, 7830457)