#Write a function to compute the sum of data of variable length.

def sum(arg1,*tuple):
    ans=arg1
    for var in tuple:
        ans+=var
    print(ans)

sum(1,2,3,4,5)