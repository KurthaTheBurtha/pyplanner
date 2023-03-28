# import datetime
# x = datetime.datetime.now()
# today = x.strftime("%m/%d/%Y")
# month = today[0:today.index("/")]
# second = today.find("/",3)
# day = today[today.index("/")+1:second]
# year = today[second+1:len(today)]
# print(today)
# print(month)
# print(day)
# print(year)
# year = datetime.datetime.now().strftime("%Y")
#print(day)
index=0
k=3
a = []
for i in range(1,7+1):
    a.append(i)
while k>index:
        if a[index]<a[len(a)-index-1]:
            a[index],a[len(a)-index-1] = a[len(a)-index-1],a[index]
        index+=1
        if index>=k:
            break
print(a)

class Date:

    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year
    def __str__(self,month,day,year):
        return f"{self.month}/{self.day}/{self.year}"

