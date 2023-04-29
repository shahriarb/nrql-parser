import re
import sys

class NRQLParser:
    def __init__(self):
        self.keywords = {
            "SELECT": "select",
            "FROM": "from",
            "WHERE": "where",
            "FACET": "facet",
            "LIMIT": "limit",
            "SINCE": "since",
        }

    def parse(self, query):
        tokens = re.split(r"\s+", query)
        select_list = []
        from_table = None
        where_expression = None
        facet_list = []
        limit = None
        since = None
        for token in tokens:
            if token in self.keywords:
                keyword = token
            else:
                if keyword == "SELECT":
                    select_list.append(token)
                elif keyword == "FROM":
                    from_table = token
                elif keyword == "WHERE":
                    where_expression = token
                elif keyword == "FACET":
                    facet_list.append(token)
                elif keyword == "LIMIT":
                    limit = token
                elif keyword == "SINCE":
                    since = token

        return {
            "select": select_list,
            "from": from_table,
            "where": where_expression,
            "facet": facet_list,
            "limit": limit,
            "since": since,
        }
    

if __name__ == "__main__":
    parser = NRQLParser()
    query =  sys.argv[1]
    result = parser.parse(query)
    print(result)
