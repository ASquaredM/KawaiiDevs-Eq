import numpy as np
from WinFns import WinFn as WF

freq = np.ones(30000)
Gains = [1,0,1,0,1,0,1,0,1,0]
Bands = np.array([[20,40],[40,80],[80,160]
                    ,[160,300],[300,600],[600,1200]
                    ,[1200,2400],[2400,5000],[5000,10000]
                    ,[10000,20000]])
data = np.ones(30000)
Win_Fn = np.array(['Rectangular','Hamming','Hanning'])

out = WF(Win_Fn[1],freq,Bands,Gains,data)

i = 0
while i < 10000:
    print(out[i],out[i+1],out[i+2],out[i+3],out[i+4],out[i+5],out[i+6],out[i+7],out[i+8],out[i+9])
    i += 9