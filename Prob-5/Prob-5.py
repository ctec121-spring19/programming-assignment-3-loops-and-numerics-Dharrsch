# Module 2
#   Programming Assignment 3
#     Prob-5.py

# YOUR NAME

# You purchased the following:
#    - 2 slices of pizza at $2.00 per slice
def main():
    print("___________________")
    p=2.00
    c=1.50
    d=0.56
    print("Pizza Slice:\t", p, sep="")
    print("Pizza Slice:\t", p, sep="")
#    - 1 large Coke at $1.50
    print("Coke:\t\t",c, sep="")
#    - 2 donuts at $0.56 each
    print("Donut:\t\t",d,sep="")
    print("Donut:\t\t",d,sep="")
#- print the total of all items
    sub=p+p+c+d+d
    import math
    sub= math.ceil(sub*100)/100
    print("______________")
    print("Subtotal:\t",sub,sep="")
#- print the sales tax (8.4% of the total)
    tax=0.084*sub
    tax= math.ceil(tax*100)/100
    print("Tax:\t\t",tax, sep="")
#- print the grand total
    tot=sub+tax
    tot= math.ceil(tot*100)/100
    print()
    print("Total:\t\t",tot,sep="")
    print()

#- ask the user to enter an amount
    tend=eval(input("Please enter amout paid: "))
    print()
    print("Tendered:\t",tend,sep="")
    chg=tend-tot
    chg= math.ceil(chg*100)/100
    print("Change Due:\t", chg,sep="")
    print("______________________________")


main()