def determine_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is NOT a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")

if __name__ == '__main__':
    year = int(input("Put in a year: "))
    determine_leap_year(year)