#Write a function to compute simple interest using provided values as arguments 
# if rate of interest is not provided consider it as 3.5%.

def simple_interest(p,n,r=3.5):
    interest=p*r*n/100
    print('Simple interest with values p:',p,',r:',r,',n:',n ,'is:',interest)

simple_interest(p=5000,r=2,n=10)