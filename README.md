# NRQL Parser

This script parses NRQL queries and returns a dictionary of the query's components.

## Usage

```
python nrql_parser.py "SELECT count(distinct user) FROM PageView WHERE userAgent.os = 'Mac' FACET countryCode LIMIT 20 SINCE 1d"
```

The result:

```
{'select': ['count(distinct', 'user)'], 'from': 'PageView', 'where': "'Mac'", 'facet': ['countryCode'], 'limit': '20', 'since': '1d'}
```
