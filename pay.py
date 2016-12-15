def computepay(h,r):
    if h >40:
        x = ((1.5*r*(h-40)) + (40*r))
        return x
    else:
        x = r * h
        return x
        

hrs = "45"
rate = "10.50"
h = float(hrs)
r = float(rate)

p = computepay(45,10.5)
print ("Pay",p)
