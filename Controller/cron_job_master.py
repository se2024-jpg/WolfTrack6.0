from crontab import CronTab
import getpass
import os
curr_path=os.path.dirname(os.path.abspath(__file__))

cron = CronTab(user=getpass.getuser())
job = cron.new(command='python ' + curr_path + '/cron_job_slave.py')
job.minute.every(1)

cron.write()