import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def process(c, yvar):
    headers = ['Server_Number', 'Num_Channels','Avg_IOD','Max_IOD', 'Avg_IFD', 'Max_IFD', 'Throughput', 'Finish Time']
    df = pd.read_csv(c,names=headers)

    df.drop(index=df.index[0], axis=0, inplace=True)
    df = df.astype('float')

    df[['Avg_IOD_a', 'Avg_IFD_a', 'Finish Time_a', 'Throughput_a']] = df.groupby(['Server_Number', 'Num_Channels'])[['Avg_IOD', 'Avg_IFD', 'Finish Time', 'Throughput']].transform('mean')

    df['Avg_IOD_std'] = df.apply(lambda x: abs(x['Avg_IOD']-x['Avg_IOD_a']), axis=1)

    df['Avg_IOD_std_a'] = df.groupby(['Server_Number', 'Num_Channels'])['Avg_IOD_std'].transform('mean')

    x_s1 = df[df['Server_Number'] == 1.0]['Num_Channels']
    y_s1 = df[df['Server_Number'] == 1.0][yvar]

    x_s2 = df[df['Server_Number'] == 2.0]['Num_Channels']
    y_s2 = df[df['Server_Number'] == 2.0][yvar]

    return (x_s1, y_s1, x_s2, y_s2)


plt.xlabel('Number of Channels Allotted to Job 1') # Text for X-Axis
plt.ylabel('Average IFD') # Text for Y-Axis
plt.title(f"Average IFD for 2 SRARQ and 2 RLNC jobs across 10 channels")

# plot all the points
#plt.scatter(x_s1, y_s1, color='blue', marker='.', linewidths=0)

#plt.scatter(x_s2, y_s2, color='orange', marker='.', linewidths=0)

#Avg_IOD_a, Avg_IFD_a, Finish Time_a, Throughput_a
x1s, y1s, x2s, y2s = process('e1_1000_SRARQ.csv', 'Avg_IFD_a')
#x1r, y1r, x2r, y2r = process('e1_rlnc_eqn.csv', 'Finish Time_a')

plt.plot(x1s, y1s, 'r-', label = "SRARQ Job 1")
plt.plot(x2s, y2s, 'b-', label = "SRARQ Job 2")

#plt.plot(x1r, y1r, 'r--', label = "RLNC Job 1")
#plt.plot(x2r, y2r, 'b--', label = "RLNC Job 2")

plt.legend()

plt.savefig(f'e1_srarq_IFD.png')