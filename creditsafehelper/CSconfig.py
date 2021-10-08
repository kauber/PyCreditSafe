class BaseURLs:
    authenticate_url: str = 'https://connect.creditsafe.com/v1/authenticate'
    metadata_url: str = "https://connect.creditsafe.com/v1/companies?id={}&countries={}&page=1&pageSize=10"
    report_url: str = 'https://connect.creditsafe.com/v1/companies/{}?language=en'
    matches_url: str = 'https://connect.creditsafe.com/v1/companies?name={}&countries=GB&page=1&pageSize={}'
    bulk_url: str = 'https://connect.creditsafe.com/v1/companies?countries={}&status=Active&page={}&pageSize={}'


class Countries:
    CS_countries: list = ['GB', 'US', 'SE', 'NO', 'NL', 'MX', 'LU', 'JP', 'IT', 'IE', 'DE', 'FR', 'DK', 'BE']
