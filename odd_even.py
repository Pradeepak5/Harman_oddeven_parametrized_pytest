def odd_even(x):
    if x%2==0:
        return True
    else:
        return False

if __name__=="__main__":
    x=int(input("Enter the Number :"))
    result=odd_even(x)
    print(result)
