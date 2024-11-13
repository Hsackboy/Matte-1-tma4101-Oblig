import matplotlib.pyplot as plt
import numpy as np


f = open("data/maaling 1.xls")

timeClockData = []
voltageValueData =[]

startIndex = 16

count = 0
for line in f:
    if count > 16:
        dataSplit = line.split("	")
        timeClockData.append(dataSplit[1])
        dataSplit[3] = dataSplit[3].replace(",",".")
        dataSplit[3] = float(dataSplit[3])
        if dataSplit[4]=="mV":
            voltageValueData.append(dataSplit[3]*10**-3)
        else:
            voltageValueData.append(dataSplit[3])
    count+=1
    

tSplitSart = timeClockData[0].split(":")
tSplitEnd = timeClockData[-1].split(":")

totalTid = float(float(tSplitEnd[0])-float(tSplitSart[0]))*3600 +float(float(tSplitEnd[1])-float(tSplitSart[1]))*60 +float(float(tSplitEnd[2])-float(tSplitSart[2]))
dt = totalTid/len(timeClockData)
tMesurment = [i*dt for i in range(len(timeClockData))]


RTol = 0.01
CTol = 0.05
R = 101.2*10**(3)
C = 102*10**(-6)
Vs = 9.9

def Vc(t,Vs,R,C):
    return Vs *(1-np.e**(-t/(R*C)))


t = np.linspace(0,120)
x1 = Vc(t,Vs,R,C)
x2 = Vc(t,Vs,R+R*RTol,C+C*CTol)
x3 = Vc(t,Vs,R-R*RTol,C-C*CTol)


plt.axvline(x=0,color="black")
plt.axhline(y=0,color="black")
plt.plot(t,x1, label="Vc(t) med mer nøyaktige komponent verdier")
plt.plot(tMesurment,voltageValueData, label="Vc(t) Målt")
plt.title("Spenning over tid for RC krets målt mot utregnet verdi")
plt.xlabel("t(s)")
plt.ylabel("U(v)")
plt.legend()
plt.savefig("maaling1plotJustering")
plt.show()
