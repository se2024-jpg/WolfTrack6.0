from datetime import datetime
myFile = open('/Volumes/T6/WolfTrack2.0/Controller/append.txt', 'a') 
myFile.write('\n on ' + str(datetime.now()))