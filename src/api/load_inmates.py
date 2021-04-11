import requests
import json
from .mugshot import Mugshot
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class InmateList:
    def __init__(self, num):
        self.source_path = "api/sources.txt"
        self.api_key = "api/key.txt"
        self.black_list = []
        self.inmate_list = []
        self.source_ids = []
        self.populate_inmates(num)
        self.replace_names()

    def populate_inmates(self, num):
        response = requests.get("https://web3.clackamas.us/roster/extract/inmates", verify=False)
        inmates = json.loads(response.text)['results']

        for i in inmates[:num]:
            inmate = {'name':    i['name'],
                      'mugshot': Mugshot(i['image']),
                      'charges': [c['charge'][14:].lstrip().lstrip('-').lstrip() for c in i['charges']],
                      'sex':     i['sex'],
                      'source':  ""}
            self.inmate_list.append(inmate)

    # Replaces names of inmates
    #   Makes two api calls, one for each sex
    def replace_names(self):
        num_inmates = len(self.inmate_list)

        # Male names
        payload = {'nameOptions': 'boy_names'}
        response = requests.get('http://names.drycodes.com/' + str(num_inmates), params=payload)
        male_names = json.loads(response.text)

        # Female names
        payload = {'nameOptions': 'girl_names'}
        response = requests.get('http://names.drycodes.com/' + str(num_inmates), params=payload)
        female_names = json.loads(response.text)

        # Iterate through inmate list, replacing name
        # with one from the list that matches the sex
        for inmate in self.inmate_list:
            if inmate['sex'] == 'Male':
                name = male_names.pop()
            else:
                name = female_names.pop()

            inmate['name'] = name.replace('_', ' ')
