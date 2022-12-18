import re
from typing import Generator, Iterable, List, Optional, Dict, Callable

from HW23.functions import filter_query, map_query, unique_query, sort_query, limit_query, regex_query

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_FUNCTION: Dict[str, Callable]
CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query,
}


def iter_file(file_name: str) -> Iterable[str]:
    with open(file_name) as file:
        for row in file:
            yield row


def query_builder(data: Optional[Iterable[str]], cmd: str, value: str) -> List[str]:
    if data is None:
        prepared_data=iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
    return list(result)



