import json, requests, os
from query_elasticsearch import create_query_elasticsearch
from requests_aws4auth import AWS4Auth
import requests

#environment_variables
size_results = os.environ['size_results']
index_name_elasticsearch = os.environ['index_name_elasticsearch']
url_elasticsearch = os.environ['url_elasticsearch']
access_key = os.environ['access_key']
secret_access_key = os.environ['secret_access_key']
headers = {"Content-Type" : "application/json"}

def search(event, context):
    print("Input_request: ", event)
    
    searcher = Searcher()
    try:
        query = create_query_elasticsearch(event, size_results)
        print("query: ", query)
        data = searcher.get_data_elasticsearch(query["data"])
        print("data: ", data)
        formated_data = searcher.format_data(data["data"])
        
        search_response = {'search' : formated_data["data"]}
        print("Output_response: ", search_response)
        return search_response
    except Exception as e:
        return f"Error in (search) {e}"


class Searcher:
    def __init__(self):
        self.response = {
            "status" : "",
            "data" : "",
            "details" : ""
        }

    def response_format(self, data, details):
        try:
            self.response["status"] = 200
            self.response["data"] = data
            return self.response
        except Exception as e:
            self.response["status"] = 400
            self.response["details"] = details
            return self.response

    def get_data_elasticsearch(self, data):
        try:
            awsauth = AWS4Auth(access_key, secret_access_key, "us-east-1", 'es')

            response_elasticsearch = requests.get(f"{url_elasticsearch}/{index_name_elasticsearch}/docs/_search", auth=awsauth, data=json.dumps(data), headers = headers)
            response_data = response_elasticsearch.json()
            
            return self.response_format(response_data, "")
        except Exception as e:
            return f"Error in (get_data_elasticsearch) {e}"


    def format_data(self, data):
        try:
            results = []
            for source in data["hits"]["hits"]:
                results.append({
                    "name" : source["_source"]["name"]+", "+source["_source"]["countryName"],
                    "latitude": source["_source"]["latitude"],
                    "longitude": source["_source"]["longitude"],
                    "score" : source["_score"]
                })
            
            return self.response_format(results, "")
        except Exception as e:
            return f"Error in (format_data) {e}"

    