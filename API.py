######################


# YOUR CODE GOES HERE


# Import the modules you'll need for this assignment (json, requests)



import json

import requests


######################


# This is a working API key for the ProPublica Congress API. Don't change it.

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'


def get_votes_by_date(chamber, start_date, end_date):

	print chamber
	print start_date
	print end_date


###################


# YOUR CODE GOES HERE


# Define the proper URL here. It should use the chamber, start_date and end_date arguments

# provided by the function.



	url = 'https://api.propublica.org/congress/v1/' + chamber + '/votes/' + start_date + '/' + end_date + '.json'


	###################


	response = requests.get(url, headers={"X-API-Key": API_KEY}).content


	###################


	# YOUR CODE GOES HERE


	# Define the data variable here and use it to process the response into Python objects.


	data = json.loads(response) # Replace this with whatever the data variable should be


	###################


	return data



def format_nomination_votes(data):

	'''

	Your next task is to take the results of the API response, extract several of the most

	important pieces of information, and put them into a list. We do this at the Times to

	ultimately save the data into a database, but you could also use it to produce a CSV

	for analysis.

	Specifically, the information you'll need to extract from each result is:


	- Vote date

	- Vote question

	- Vote description

	- Vote result

	- Total number of votes for each "yes," "no," "present," and "not voting"

	The output of this function, which should be stored in the variable called output,

	should be a list of lists. Each list should contain the aforementioned pieces of

	information for each result you get back.

	For example (whitespace added to make this more clear):

	output = [

	['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting'],

	['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']

	]

	Hint: You'll have to use a loop. Remember that you can add items to a list using the

	"append" method. So if you want to add a new record to output, you could do something

	like output.append(record)
	'''

	output = [['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']]




	record = []

	#for d in data:

	record.append(data['results']['votes'][0]['date'])

	record.append(data['results']['votes'][0]['question'])

	record.append(data['results']['votes'][0]['description'])

	record.append(data['results']['votes'][0]['result'])

	record.append(data['results']['votes'][0]['total']['yes'])

	record.append(data['results']['votes'][0]['total']['no'])

	record.append(data['results']['votes'][0]['total']['present'])

	record.append(data['results']['votes'][0]['total']['not_voting'])

	output.append(record)


	###################


	return output



########## YOU CAN IGNORE THIS ##########


if __name__ == '__main__':
	votes = get_votes_by_date('senate', '2017-04-06', '2017-04-06')


if votes == None:

	print "Looks like you haven't finished implementing the get_votes_by_date method ..."

	exit()

elif type(votes) != dict:

	print "Something's wrong. You might still need to process the data using the json module."

	exit()

elif type(votes) == dict:

	print 'Your data looks ok!'

print votes


formatted = format_nomination_votes(votes)


if len(formatted) <= 1:

	print 'You only seem to have one item in your output. Did you append records for the others?'

	exit()


print 'Output:'

print formatted