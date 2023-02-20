#Q2

#Initialaize variables
Year = 0
month = 0
day = 0

#Input
year = int(input("Enter the year :"))
month = int(input("Enter the month :"))
day = int(input("Enter the day :"))

#Process
#Months contain 31 days
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    max_days=31
#Months contain 30 days
elif (month==4 or month==6 or month==9 or month==11) :
    max_days=30
#Check leap year or not
elif (year%4==0 and year%100!=0 or year%400==0) :
    max_days=29
else :
    max_days=28
#Conditions for valid date and invalid date
if (year<0) :
    print("Date is invalid")
    print("check the year")
elif (month<1 or month>12) :
    print("Date is invalid")
    print("check the month")
elif (day<1 or day>max_days) :
    print("Date is invalid")
    print("check the day")
#Conditions for increment date
elif (day==max_days and month!=12) :
    day=1
    month=month+1
    print("The next date is:","Year",year,"-","Month",month,"-","Day",day)
elif(day==31 and month==12):
   day=1
   month=1
   year=year+1
   print("The next date is:","Year",year,"-","Month",month,"-","Day",day)
else :
    day=day+1
    print("The next date is:","Year",year,"-","Month",month,"-","Day",day)
    
