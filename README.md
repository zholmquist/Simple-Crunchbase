# Simple Crunchbase
Simple Crunchbase is a terse Crunchbase.com REST API client built for Python.
You can find out more regarding the Crunchbase API in the [Official Crunchbase.com REST API Documentation](https://developer.crunchbase.com).

## Example
Getting information from Crunchbase is fairly straightforward.
Once you creat the ```Crunchbase``` object, simply append the Item/Operation ( Organizations, Organization, People, Person, etc. ) you want to query, and provide the paremters needed.

### For example:

```
from crunchbase import CrunchBase
cb = CrunchBase(user_key='xXxxXxxXxxXxxXxxXxxXxxXx')
print cb.Organization.get(permalink='eventboard')
```

```
from crunchbase import CrunchBase
cb = CrunchBase(user_key='xXxxXxxXxxXxxXxxXxxXxxXx')
print cb.Organizations.get(name='eventboard')
```

## Inspiration
This library was inspired by [Simple Salesforce](https://github.com/neworganizing/simple-salesforce).