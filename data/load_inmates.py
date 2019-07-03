import requests
import random
import json
import time

'''
 Data provided by JailBase.com
 
 Individuals are innocent until proven guilty in a court of law. 
 Data is believed to be reliable but is provided "as is". 
 Contact the appropriate governmental agency to verify.
 
 Terms of Service:
    https://www.jailbase.com/api/terms/
'''


class InmateList:
    def __init__(self, num):
        self.source_path = "data/sources.txt"
        self.api_key = "data/key.txt"
        self.black_list = []
        self.inmate_list = []
        self.source_ids = []
        self.load_sources()
        self.populate_inmates(num)

    def load_sources(self):
        # Online
        try:
            response = requests.get("http://api.open-notify.org/iss-pass.json")

        # Offline
        except ConnectionError:
            return

        # Read in api key
        self.api_key = open(self.api_key).read()

        # Read in sources
        raw_sources = open(self.source_path).read().splitlines()
        for source in raw_sources:
            line = source.rsplit('\t')
            self.source_ids.append(line[0])

    def populate_inmates(self, number_of_inmates):
        headers = {
                   'X-RapidAPI-Host': 'jailbase-jailbase.p.rapidapi.com',
                   'X-RapidAPI-Key': self.api_key
                 }

        count = 0
        while count < number_of_inmates:
            source_id = random.choice(self.source_ids)
            try:
                response = requests.get("https://jailbase-jailbase.p.rapidapi.com/recent/?source_id="
                                        + source_id,
                                        headers=headers).json()['records']

                i = 0
                while i < 10 and i < len(response):
                    if self.can_add(response[i]):
                        break
                    i += 1

                if i < 10:
                    response = response[i]
                    inmate = {'name':    response['name'],
                              'mugshot': response['mugshot'],
                              'charges': response['charges'],
                              'source':  response['more_info_url']}

                    print(inmate)
                    self.inmate_list.append(inmate)
                    count += 1

                # remove source from list
                else:
                    self.source_ids.remove(source_id)

            except json.decoder.JSONDecodeError:
                pass

            # API TOS is rate limited
            time.sleep(1.25)

        # Write changed source list back to file
        with open('sources.txt', 'w') as file:
            for source_id in self.source_ids:
                file.write(source_id + '\n')

    def can_add(self, inmate_to_add):
        # Need charges to define enemy stats
        if not inmate_to_add['charges']:
            return False

        # Only inmates with pictures
        if inmate_to_add['mugshot'] == 'https://imgstore.jailbase.com/widgets/NoMug.gif':
            return False

        # If inmate already in list
        for i in self.inmate_list:
            if inmate_to_add['name'] == i['name']:
                return False

        return True
