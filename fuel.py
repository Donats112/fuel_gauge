from decimal import Decimal

def main():
    fraction = input("Ievadi veselu daļu (x/y): ")
    x,y=convert(fraction)
    gauge(x, y)

def convert(fraction):
    converted = fraction.split("/")
    x = int(converted[0])
    y = int(converted[1])
    return x, y

def gauge(x, y):
    if x >=0 and y >= 0:
        if x > y and y !=0:
            raise ValueError("skaitītājam jābūt mazākam par saucēju")
        elif y == 0:
            raise ZeroDivisionError("Nevar dalīt ar 0")
        elif x/y*100 >= 99:
            return("F")
        elif x/y*100 <= 1:
            return("E")
        else:
            percentage = Decimal(round(x/y*100, 2))
            percentage2 = percentage.quantize(Decimal('0.00'))
            percent = str(percentage2) + "%"
            return(percent)
    else:
        raise ValueError("bez negatīviem skaitliem!")

if __name__ == "__main__":
    main()