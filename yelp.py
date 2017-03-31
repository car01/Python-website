<<<<<<< HEAD
import rauth, time, json


def get_search_parameters(postcode, category):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	#params["ll"] = "{},{}".format(str(lat),str(long))
	params["location"] = postcode
	params["radius_filter"] = "2000"
	params["category_filter"] = category
	params["limit"] = "1"

	return params

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
	#Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)
	
	print "Name" + Name
	#print "Rating: " + 'rating_img_url'
	#print "Telephone: " + 'display_phone'
	#print "Address: " + 'display_address'

     
if __name__=="__main__":
	main()
=======
def get_search_parameters(lat,long):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat),str(long))
  params["radius_filter"] = "2000"
  params["limit"] = "10"
 
  return params

  def get_results(params):
 
  #Obtain these from Yelp's manage access page
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
>>>>>>> origin/master
