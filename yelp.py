import rauth, time, json
from flask import Flask
from flask import render_template
from flask import request
app = Flask("MyApp")

@app.route("/")
def front_page():
	return render_template("yelp.html")


@app.route("/search", methods=['POST'])
def sign_up():
	form_data = request.form
	print form_data["cuisine"]
	locations = form_data['postcode']
	category = form_data['cuisine']
	api_calls = []
	#for lat,long in locations:
	params = get_search_parameters(locations, category)
	api_calls.append(get_results(params))
	print len(api_calls)
	#Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)
	print 'error' in api_calls
	if 'error' in api_calls:
		print "No address"
	else:
		#print api_calls
		numFound = int(api_calls[0]['total'])
		print numFound
		for i in range(0,numFound):
			name = api_calls[0]['businesses'][i]['name']
			print "Name %s." % name
			phone = api_calls[0]['businesses'][i]['display_phone']
			print "Phone number: %s" % phone
			address = api_calls[0]['businesses'][i]['location']['display_address']
			for g in range(0,len(address)):
				print "Address: %s" % address[g]
			rating = api_calls[0]['businesses'][i]['rating_img_url']
			print rating

	return "All OK"


def get_search_parameters(postcode, category):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	#params["ll"] = "{},{}".format(str(lat),str(long))
	params["location"] = postcode
	params["radius_filter"] = "2000"
	params["category_filter"] = category
	params["limit"] = "5"

	return params
#def make_api_calll(offset):
	#return request.json()

#def load_all_data():
	#data = []
	#while make_api_calll(offset)['name']:
		#name = "Name" + name


def get_results(params):
	consumer_key = "iSH3hBJx1Ij7TRwVnGzYCg"
	consumer_secret = "1h0M4HbgwNQQfu0MBj-QrT8Buho"
	token = "JI210sOcR0HTa4QEWAZcxRnqXNU9SfKO"
	token_secret = "oPOACj_tuslalhGhBZAHJ-182aQ"

	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)

	request = session.get("http://api.yelp.com/v2/search",params=params)

	#Transforms the JSON API response into a Python dictionary
	data = request.json()

	session.close()
	

	return data


def main():
	locations = raw_input()
	category = raw_input()
	#locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
	api_calls = []
	#for lat,long in locations:
	params = get_search_parameters(locations, category)
	api_calls.append(get_results(params))
	print len(api_calls)
	#Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)
	if api_calls[0]['error']:
		print "No address"
	else:
		#print api_calls
		numFound = int(api_calls[0]['total'])
		for i in range(0,numFound):
			name = api_calls[0]['businesses'][i]['name']
			print "Name %s." % name
			phone = api_calls[0]['businesses'][i]['display_phone']
			print "Phone number: %s" % phone
			address = api_calls[0]['businesses'][i]['location']['display_address']
			for g in range(0,len(address)):
				print "Address: %s" % address[g]
			rating = api_calls[0]['businesses'][i]['rating_img_url']

	#rating = api_calls[0]['businesses'][0]['rating_img_url']
	#print "Name " + name
	#print "Rating: " + 'rating_img_url'
	#print "Telephone: " + display_phone
	#print "Address: " + 'display_address'

     
if __name__=="__main__":
	app.run()
