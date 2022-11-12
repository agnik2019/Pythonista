monthsMap=dict()
 
# Function which initializes the monthsMap
def sort_months():
 
    monthsMap["Jan"] = 1
    monthsMap["Feb"] = 2
    monthsMap["Mar"] = 3
    monthsMap["Apr"] = 4
    monthsMap["May"] = 5
    monthsMap["Jun"] = 6
    monthsMap["Jul"] = 7
    monthsMap["Aug"] = 8
    monthsMap["Sep"] = 9
    monthsMap["Oct"] = 10
    monthsMap["Nov"] = 11
    monthsMap["Dec"] = 12
 
def cmp(date):
    date=date.split()
    return int(date[2]),monthsMap[date[1]],int(date[0]),
 
 
# Utility function to print the contents
# of the array
def printDates(dates, n):
    for i in range(n):
        print(dates[i])
 

 
dates = [ "24 Jul 2017", "25 Jul 2017", "11 Jun 1996",
                    "01 Jan 2019", "12 Aug 2005", "01 Jan 1997" ]
n = len(dates)

# Order the months
sort_months()

# Sort the dates
dates.sort(key=cmp)

# Print the sorted dates
printDates(dates, n)