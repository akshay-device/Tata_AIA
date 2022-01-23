import requests
import json
import datetime

# For Serializers
url = "http://127.0.0.1:8000/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'Ticket_ID': id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)


def post_data():
    # data = {'Form':'Online','Method':'ONLINE'}
    data = [{"Date_of_Issue": '2016-12-31', "Time_of_Issue": '5:00:00 AM', "Form": "TV", "Method": "DSL",
            "Issue": "Privacy", "Caller_ID_Number": "None", "Type_of_Call_or_Messge": 'Prerecorded Voice',
            "Advertiser_Business_Number": "None", "City": "Barry", "State": "OK", "Zip": 74429,
            "Location_Center_point_of_the_Zip_Code": "OK 74429(35.9528, -95.632954)"},
            {"Date_of_Issue": '2016-12-31', "Time_of_Issue": '5:00:00 AM', "Form": "TV", "Method": "DSL",
             "Issue": "Privacy", "Caller_ID_Number": "None", "Type_of_Call_or_Messge": 'Prerecorded Voice',
             "Advertiser_Business_Number": "None", "City": "Barry", "State": "OK", "Zip": 74429,
             "Location_Center_point_of_the_Zip_Code": "OK 74429(35.9528, -95.632954)"},
            {"Date_of_Issue": '2016-12-31', "Time_of_Issue": '5:00:00 AM', "Form": "TV", "Method": "DSL",
             "Issue": "Privacy", "Caller_ID_Number": "None", "Type_of_Call_or_Messge": 'Prerecorded Voice',
             "Advertiser_Business_Number": "None", "City": "Barry", "State": "OK", "Zip": 74429,
             "Location_Center_point_of_the_Zip_Code": "OK 74429(35.9528, -95.632954)"}
            ]

    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


