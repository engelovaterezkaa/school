import datetime as dt #lze importovat pod jiným názvem, viz. ... as dt


now = dt.datetime.now() #funkce dt ma funkce datetime ktera ma funkci now, momentalni cas

# print(now) #muzeme dat cely cas nebo konkretni cast casu
# print(now.second)
# print(now.day)
# print(now.month)
# print(now.year)

# #odecitani casu
# delta = dt.timedelta
# print("delta je,", delta)

print("teď je,", now)
minus10 = now - dt.timedelta(minutes = 10)
print(minus10)

new_time = dt.datetime(2024,11,14,14,15,0,0)
how_long_till_break = new_time - now
print("Do přestávky zbývá", how_long_till_break)

#datetime ma mnoho funkci: vse na googlu

time = now + dt.timedelta(minutes = 1)
print(time)


