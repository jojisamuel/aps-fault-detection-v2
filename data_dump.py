import pandas as pd
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://jojis:2222222@cluster0.wj6gl.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME='aps'
COLLECTION_NAME='sensor'


if __name__=='__main__':
    df=pd.read_csv('https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv')
    df.reset_index(drop=True,inplace=True)
    json_records=list(json.loads(df.T.to_json()).values())
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
