import numpy as np
import pandas as pd
from model import generate_recommendations
import json
import time

import pandas as pd
from google.cloud import storage

## set the output bucket that saved all recommendations
storage_client = storage.Client()
bucket = storage_client.get_bucket('mpd-recsys')
blob=bucket.blob('nst/recommend/recommendation_for_users.json')


## set number of items
k = 10

## load the recommendation latent factor file
user_map = np.load("trainer/model/user.npy")
item_map = np.load("trainer/model/item.npy")
row_factor = np.load("trainer/model/row.npy")
col_factor = np.load("trainer/model/col.npy")
already_rated = []
result_df = pd.DataFrame()

def recommend_for_user():	
	result_df = pd.DataFrame()
	already_rated = []
	recDict = {}
	recList = []

	k = 10


	for i in range(0, len(user_map) ):
	    client_id = user_map[i]
	    user_idx = np.searchsorted(user_map, client_id)
	    user_rated = [np.searchsorted(item_map, i) for i in already_rated]
	    recommendations = generate_recommendations(user_idx, user_rated, row_factor, col_factor, k)
	    article_recommendations =  [ int(item_map[i]) for i in recommendations ] 
	#     article_recommendations = article_recommendations  ## convert the array of item into list
	    try:
	    	recDict = { 'clientId': client_id.decode("utf-8") , "rec":article_recommendations }
	    except:
	    	recDict = { 'clientId': client_id , "rec":article_recommendations }

	    recList.append(recDict)
	#     result = pd.DataFrame( {'clientId':client_id.decode("utf-8") , "recommendations" : article_recommendations })
	#     result_df = result_df.append( result )
	    if i % 10000 == 0 : print(i)

	## save the result file
	with open('trainer/result/nst_recommend_for_users.json', 'w') as f:
	    json.dump(recList, f)

	## upload the content to GCP bucket
	blob.upload_from_filename('trainer/result/nst_recommend_for_users.json')



if __name__ == "__main__":
	start = time.time()
	recommend_for_user()
	end = time.time()
	duration = end - start
	duration



