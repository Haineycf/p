import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Chris', 'Georgia', 'Fiona', 'Pete', 'Katie')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('How fast do you want to go today?')
 
plt.show()