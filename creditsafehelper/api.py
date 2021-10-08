import requests
import json
from creditsafehelper.CSconfig import BaseURLs, Countries


class CreditSafeHelper(object):

    def __init__(self, password, username) -> None:
        """
        initializer, given username and password it will generate a token passing those credentials
        """
        self.username = username
        self.password = password
        self.token = self.get_new_token()

    def get_company_metadata(self, company_id: str, *args, **kwargs) -> dict:
        """
        Collects basic information of a company
        :param company_id: creditsafe company identifier
        :param args:
        :param kwargs:
        :return: json with basic company information
        """

        country: str = company_id[:2]

        url = BaseURLs.metadata_url.format(company_id, country)
        payload = {}
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.token = self.get_new_token()
        # do we need to repeat here?
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        return json_data

    def get_full_report(self, company_id: str, *args, **kwargs) -> dict:
        """
        Get the company full report

        :param company_id: creditsafe id of the company we want to query
        :param args:
        :param kwargs:
        :return: json with full report of the queried company
        """

        url = BaseURLs.report_url.format(company_id)
        payload = {}
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.token = self.get_new_token()

        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        return json_data

    def get_closest_matches(self, targetcompany: str, numentries: int, *args,
                            **kwargs) -> list:
        """
        This function will return the closest matches to a company name we send to creditsafe. Ampersands are removed
        from the company name as they cause errors

        :param targetcompany: name of the company we want to match
        :param numentries: number of matches we want creditsafe to return
        :param args:
        :param kwargs:
        :return: n best matches for a company name sent
        """

        targetcompany = targetcompany.replace('&', '')
        url = BaseURLs.matches_url.format(targetcompany, numentries)
        payload = {}
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.token = self.get_new_token()

        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        json_data_out = json_data['companies']
        if not json_data_out:
            print('No matches returned')
            return None
        else:
            return json_data_out

    def bulk_export(self, country: str, page: int, pagesize: int) -> dict:
        """
        Collects bulk export (basic company information) from the CS API. No filters are applied, except for the status
        of the company (will be automatically set to active) and the country
        NOTE: this method is experimental as currently CreditSafe limits the pages we can scroll through to export data
        :param page: page we want to query (up to 14 allowed currently)
        :param country: country we want to query
        :param pagesize: how many entries by page we want to export

        """
        if country not in Countries.CS_countries:
            print('Country not available. Legal country codes are: ' + str(Countries.CS_countries))

        url = BaseURLs.bulk_url.format(country, page, pagesize)
        payload = {}
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            self.token = self.get_new_token()

        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        return json_data

    def get_new_token(self, *args, **kwargs) -> str:
        """
        Sends a request for a new token when the previous one expires
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json', }
        credentials = '{"username":"%s","password":"%s"}' % (self.username, self.password)
        token_response = requests.post(BaseURLs.authenticate_url, headers=headers,
                                       data=credentials)
        try:
            token_response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(str(e))

        token_response = json.loads(token_response.text)
        token = token_response['token']
        return token


if __name__ == '__main__':
    pass
