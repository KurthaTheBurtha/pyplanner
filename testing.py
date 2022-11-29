import datetime
x = datetime.datetime.now()
today = x.strftime("%m/%d/%Y")
month = today[0:today.index("/")]
second = today.find("/",3)
day = today[today.index("/")+1:second]
year = today[second+1:len(today)]
print(today)
print(month)
print(day)
print(year)
year = datetime.datetime.now().strftime("%Y")
#print(day)

class Date:

    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year
    def __str__(self,month,day,year):
        return f"{self.month}/{self.day}/{self.year}"

