from os import environ
import os
import smtplib

import json

# env = environ.Env.read_env() # reading .env file
#
# SECRET_KEY = env('gmail_pass')

country_info= ''
abc = os.environ.get('gmail_pass')
print(abc)
message= ''
def send_email(email, msg):
    #message= msg
    print('this is from second one....', email, msg)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('kumarjay2107@gmail.com', abc)
        from_= 'kumajay2107@gmail.com'
        to_= email

        #messgage = "From: {}\r\nTo: {}\r\n\r\n{}\r\n".format(from_, to_, msg)
        sub= 'Corona information'
        message = f'subject : {sub} \n\n {msg}'

        smtp.sendmail(from_, to_, message)

        print('Successfulllll')

#print('mesage is....', message)

#send_email('kumarjay2107@gmail.com', message)


def corona_data(state):
    import requests

    url = "https://covid-19-india-data-by-zt.p.rapidapi.com/GetIndiaDistrictWiseDataForState"

    querystring = {"statecode": state}

    headers = {
        'x-rapidapi-host': "covid-19-india-data-by-zt.p.rapidapi.com",
        'x-rapidapi-key': "224638e204mshb839568221a2bdbp139574jsnc196b2b953b4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    datas = response.text

    return datas

def india_info(state, name):
    datas = corona_data(state)

    print('here is data corona_data..... ', datas)
    print('name is....', name)

    print(type(datas))

    datas = json.loads(datas)

    # print(datas['data']['name'])

    for data in datas['data']:
        if data['name'] == name:
            print(data)
            #country_info= data
            return data


import requests

# def world_data():
#
#     url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
#
#     querystring = {"country":"India"}
#
#     headers = {
#         'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
#         'x-rapidapi-key': "224638e204mshb839568221a2bdbp139574jsnc196b2b953b4"
#         }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     datas= response.text
#     return datas
#
# datas= world_data()
#
# print('this is worls data..... ', datas)
#
# def total():
#     import requests
#
#     url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
#
#     querystring = {"date": "2020-04-07"}
#
#     headers = {
#         'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
#         'x-rapidapi-key': "224638e204mshb839568221a2bdbp139574jsnc196b2b953b4"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     datas= response.text
#     return datas
#
# datas= total()
# print('This is total..... ', datas)

import requests


def total_with_all_country():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "224638e204mshb839568221a2bdbp139574jsnc196b2b953b4"
    }

    response = requests.request("GET", url, headers=headers)

    datas = response.text
    return datas


# print('this is total_with all_country...... ', datas)

name = "France"


def country_info(name):
    datas = total_with_all_country()
    datas = json.loads(datas)
    for data in datas['countries_stat']:
        if data['country_name'] == name:
            print(data)
            return data


data= country_info(name)
print('calling data....', data)