# CreditSafe Helper Package

This is a simple package that wraps a Python client around the CreditSafe REST API.

After importing the CreditSafeHelper class:

```
from creditsafehelper.api import CreditSafeHelper
```

We initiate a session with:
```
cs_session = CreditSafeHelper(your_password,your_username)
```

This will automatically generate a security token for calling the API. The token is valid for one hour and will be automatically refreshed upon expiration.

### Methods

The package provides 4 different methods to query the API, one of which is currently implemented as experimental.

```
CreditSafeHelper.get_company_metadata(self, company_id:str, *args, **kwargs) -> dict:
```

*get_company_metadata* retrieves basic company information, provided the CreditSafe company ID. For instance, if querying UK companies we will get: Registration Number, Safe Number, Name, Address, Status, Type, Date Of Latest Change, Activity Code, Status Description.

```
CreditSafeHelper.get_full_report(self, company_id:str, *args, **kwargs) -> dict:
```

*get_full_report* retrieves full reports, including (when filed) number of employees, financial statements, historical data and more.

In case we can't or don't want to provide the CreditSafe company ID, we can use:

```
CreditSafeHelper.get_closest_matches(self, targetcompany: str, numentries: int, *args, **kwargs) -> list:
```

*get_closest_matches* is a method for sending out a company name and collecting the n best matches (set in the 'numentries' parameter) provided by CreditSafe's internal search engine. This method can be used when trying to match a company with a Credit Safe record, as results can be later inspected to identify the right match.

Finally, a method for *bulk export* is implemented.

```
CreditSafeHelper.bulk_export(self, country: str, page: int, pagesize: int) -> dict:
```

This method retrieves a list of all active companies without further filters, apart from the country. We can set the page and how many records per page, and we will collect a list of companies' basic information.
NOTE: this method is experimental, as CreditSafe currently does not allow unlimited exports, that is an error will be prompted after page 13 is reached.  
