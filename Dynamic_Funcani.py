
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import numpy as np
import warnings
import matplotlib.dates as mdates
warnings.filterwarnings("ignore")

plt.style.use('fivethirtyeight')


df = pd.read_excel('/Users/seop/Downloads/logs.xlsx')
df.drop('Unnamed: 0',axis=1,inplace=True)
df = df.drop(622,axis = 0)
df['time'] = np.nan
df['score'] = np.nan
for i in range(len(df)):

    df['logs'][i]= df['logs'][i].replace('fire','1').replace('black smoke','0.5').replace('gray smoke','0.2')
    df['time'][i] = ' '.join(df.loc[i,'logs'].split(' ')[:2])
    df['score'][i] = df.loc[i,'logs'].split(' ')[2]

df['score'] = df['score'].astype('float32')
df['time'] = pd.to_datetime(df['time'])
df.drop('logs',axis=1,inplace=True)
df_g = df.groupby('time',as_index=False)


x_val = []
y_val = []
 
index = 0

fig, ax = plt.subplots(figsize=(10, 7))

def animate(i):
    global index,x_val,y
    
    t = df_g.sum().iloc[index]['time']
    score = df_g.sum().iloc[index]['score']

    x_val.append(t)
    y_val.append(score)

    plt.cla()
    plt.plot(x_val, y_val)

    plt.xticks(rotation=20)
    index+=1

    ax.set_xlim([pd.to_datetime(x_val[0], format = '%Y-%m-%d'),
    pd.to_datetime(x_val[-1], format = '%Y-%m-%d')])
    
    ax.set_xlabel('timestamp')

    if index >= df_g.sum().shape[0]-1:
        print("exiting the program")
        print(quit())
        
ani = FuncAnimation(plt.gcf(), animate, interval = 1000,repeat=False,)
# writervideo = animation.FFMpegWriter(fps=10)
# ani.save('e.mp4')
 
 
plt.tight_layout()
plt.show()

