import yelp


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
  yelp_api = yelp.Api(consumer_key='iSH3hBJx1Ij7TRwVnGzYCg',
                    consumer_secret='1h0M4HbgwNQQfu0MBj-QrT8Buho',
                    access_token_key='JI210sOcR0HTa4QEWAZcxRnqXNU9SfKO',
                    access_token_secret='oPOACj_tuslalhGhBZAHJ-182aQ')

  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
  request = session.get("http://api.yelp.com/v2/search",params=params)
   
  #Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()

  