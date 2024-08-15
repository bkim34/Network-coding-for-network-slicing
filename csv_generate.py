import pandas as pd
  
dict = {'Server Number' : [],
        'Num_Channels': [], #Avg_Error : [],
        'Avg_IOD':[],
        'Max_IOD': [],
        'Avg_IFD': [],
        'Max_IFD': [],
        'Throughput': [],
        'Finish Time': []
       }
  
df = pd.DataFrame(dict)

#df.to_csv('graphing.csv', index=False)
df.to_csv('graphing.csv', index=False)