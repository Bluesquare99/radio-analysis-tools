# from datetime import datetime
# import csv

# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.interval import IntervalTrigger

# scheduler = BlockingScheduler()
# @scheduler.scheduled_job(IntervalTrigger(seconds=20))
# def train_model():
# 	print('hi')
# 	# day = 'hi'
# 	# with open('cron_test.csv', mode='w') as f:
# 	# 	writer = csv.writer(f)
# 	# 	writer.writerow(day)


# train_model()

# scheduler.start()

# # def sayHi():
# # 	print('Hi there')
# # if __name__ == '__main__':
# # 	print('Hello')

if __name__ == '__main__':
	with open('/Users/bluesquarez/Documents/Coding/Projects/Radio Analysis/cron_test.txt', 'a') as f:
		f.write('Hello World!\n')
		print('hi there!')

