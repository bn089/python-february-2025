def days():
    day = years*365
    return day

years=int(input("Enter the number of years: "))
x=days()
print(f"{x} days in {years} years")