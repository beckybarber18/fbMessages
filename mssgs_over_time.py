from sys import argv
import matplotlib.pyplot as plt 
import os, re, json, datetime
import numpy as np
from math import *

def graph_over_time(data_list, people):

	print(people)
	fig, ax = plt.subplots()

	# get min and max times
	min_date = None
	max_date = None
	for data in data_list:

		times = []
		mssgs = data['messages']
		n = len(mssgs)

		# get all of the message times
		for i in range(n):
			msg = mssgs[n-1-i]
			time = msg["timestamp_ms"]/1000
			t = datetime.datetime.fromtimestamp(time)
			if min_date == None or t < min_date:
				min_date = t
			if max_date == None or t > max_date:
				max_date = t

	delta = max_date-min_date
	all_times= []
	for i in range(delta.days + 1):
		this_time = min_date + datetime.timedelta(days=i)
		all_times.append(this_time.strftime('%Y/%m/%d'))

	# plot data for each person
	for data in data_list:

		times = []
		cum_msgs = []
		mssgs = data['messages']
		n = len(mssgs)

		# get message times for that person
		for i in range(n):
			msg = mssgs[n-1-i]
			time = msg["timestamp_ms"]/1000
			t = datetime.datetime.fromtimestamp(time).strftime('%Y/%m/%d')
			if t not in times: 
				times.append(t)
				if len(cum_msgs) == 0:
					cum_msgs.append(1)
				else:
					cum_msgs.append(cum_msgs[len(cum_msgs)-1]+1)
			else:
				cum_msgs[len(cum_msgs)-1] += 1

		# get cum messages for all dates
		cum_msgs_all = np.zeros(len(all_times))
		time_index = 0

		for i in range(len(all_times)):
			this_time = all_times[i]
			# messages happened that day
			if this_time in times:
				cum_msgs_all[i] = cum_msgs[time_index]
				time_index+=1
			# no messages then
			else:
				# no messages yet
				if time_index == 0:
					cum_msgs_all[i] = 0
				else:
					cum_msgs_all[i] = cum_msgs_all[i-1]

		ax.plot(all_times,cum_msgs_all)


	# graph!
	x_labels = []
	step = floor(len(all_times)/10)
	for i in range(len(all_times)):
		if i % step == 0:
			x_labels.append(all_times[i])
		else:
			x_labels.append('')

	plt.legend(people, loc='upper left')
	title = 'messages over time'
	ax.xaxis.set_ticks(x_labels)
	plt.xticks(rotation=45)
	plt.xlabel('time') 
	plt.ylabel('cumulative messages') 
	plt.title(title) 
	plt.show()


def main():

	people_file = open("people.txt","r+")  
	people = people_file.readlines()
	for i in range(len(people)-1):
		people[i] = people[i][0:len(people[i])-1]

	people_folders = []
	people_copy = []
	for dirs in os.walk("./inbox"):
		folders = list(dirs)[1]
		for f in folders:
			for p in people:
				if re.search(p, f, re.IGNORECASE):
					people_folders.append(str(f))
					people_copy.append(p)
					people.remove(p)

	data_list = []
	for folder in people_folders:
		json_file = './inbox/'+folder+'/message_1.json'
		with open(json_file) as json_file:
			data_list.append(json.load(json_file))

	graph_over_time(data_list, people_copy)

if __name__ == '__main__':
	main()
