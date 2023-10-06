print("Hay nhap so giay: ")
t = int(input())
hour = (t//3600)%24
minute = (t%3600)//60
second = (t%3600)%60
p = ""
if hour >= 12 :
     p="PM"
     hour -= 12
else:
     p = "AM"
time = str(hour)+":"+str(minute)+":"+str(second) + " " +p
print(time)