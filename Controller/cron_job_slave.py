from datetime import datetime
import os
curr_path=os.path.dirname(os.path.abspath(__file__))
myFile = open(curr_path+'/append.txt', 'a') 
myFile.write('\n on ' + str(datetime.now()))