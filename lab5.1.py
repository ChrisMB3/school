#1

import datetime

rightNow = datetime.datetime.now()
julafton = datetime.datetime(2020, 12, 13)

daysLeft = (julafton - rightNow).days
daysLeftCor = (daysLeft+1)
print("Det är", daysLeftCor, "dagar kvar till Emma fyller år")

#tirtyDaysAgo = julafton + rightNow(days=-30)