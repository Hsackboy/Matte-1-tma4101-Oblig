import matplotlib.pyplot as plt
import numpy as np

RTol = 0.01
CTol = 0.05
R = 100*10**(3)
C = 100*10**(-6)
Vs = 10

def Vc(t,Vs,R,C):
    return Vs *(1-np.e**(-t/(R*C)))


t = np.linspace(0,60)
x1 = Vc(t,Vs,R,C)
x2 = Vc(t,Vs,R+R*RTol,C+C*CTol)
x3 = Vc(t,Vs,R-R*RTol,C-C*CTol)


plt.axvline(x=0,color="black")
plt.axhline(y=0,color="black")
plt.plot(t,x1, label="Vc(t)")
plt.plot(t,x3,linestyle="dashed", label="Vc(t) øvre estemering")
plt.plot(t,x2,linestyle="dashed", label="Vc(t) nedre estemering")
plt.title("Spenning over tid for RC krets med 100kohm og 100mircoF")
plt.xlabel("t(s)")
plt.ylabel("U(v)")
plt.legend()
plt.savefig("100100capPlotPErfekt")
plt.show()
