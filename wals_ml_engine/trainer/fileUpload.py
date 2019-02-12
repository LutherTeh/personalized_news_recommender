
import pandas as pd
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('mpd-recsys')

blob=bucket.blob('recommendation_for_users')
blob.upload_from_filename('trainer/result/nst_recommend_for_users.json')