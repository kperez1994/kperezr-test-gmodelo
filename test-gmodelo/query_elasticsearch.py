from cmath import log
import json, sys
from urllib import parse



def create_query_elasticsearch(event, size):
    print("create_query_elasticsearch", event)
    """
    parse.urlsplit(event)
    event = dict(parse.parse_qsl(parse.urlsplit(event).query))
    name = event["q"]
    latitude = event["latitude"]
    longitude = event["longitude"]
    """
    name = event["q"] if "q" in event else ""
    latitude = event["latitude"] if "latitude" in event else ""
    longitude = event["longitude"] if "longitude" in event else ""

    response = {
        "status" : "",
        "data" : "",
        "details" : ""
    }

    try:
        query = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "wildcard": {
                                "name": f"*{name}*"
                            }
                        },
                        {
                            "wildcard": {
                                "latitude": f"*{latitude}*"
                            }
                        },
                        {
                            "wildcard": {
                                "longitude": f"*{longitude}*"
                            }
                        }
                    ],
                    "filter": [
                        {
                            "match_all": {}
                        }
                    ]
                }
            },
            "sort": {
                "_score": {
                    "order": "desc"
                },
                "name": {
                    "order": "asc"
                }
            },
            "highlight": {
                "fields": {
                    "longitude": {}
                }
            },
            "from": 0,
            "size": size
        }

        response["status"] = 200
        response["data"] = query
        
        return response
    except Exception as e:
        return f"Error in (create_query_elasticsearch) {e}"