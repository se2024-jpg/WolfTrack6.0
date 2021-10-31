from crontab import CronTab
import getpass

cron = CronTab(user=getpass.getuser())
job = cron.new(command='python3 /Volumes/T6//WolfTrack2.0/Controller/cron_job_slave.py')
job.minute.every(1)

cron.write()