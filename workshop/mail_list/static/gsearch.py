#!/usr/bin/python
import re
__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

from googleapiclient.discovery import build

class Search():
    """
    Searches the required books on google.
    This class implements the google search for the books on amazon online web store.
    The class will return required number of search result.
    The class will raise a error if it is unable to connect to
    the server.
    Usage:
            s = Search()
            s.search_book("Machine Learning", max_limit=6) - For book search
            s.search_paper("Machine Learning", search_book(self, query, max_limit=5):max_limit=6)
                                - For research paper search
            s.search_next() - For next page of book search result
            s.search_next(1) - For next page of research paper search result
    Methods:
            search_book(query, max_limit=5) - returns the json file of the required book search result
            search_paper(self, query, max_limit=5): returns the json file of the required
                                                        research paper search result
            search_next(self, default=0): returns the json file for the next page of search result
                                            0 for book
                                            1 for research paper
    """
    def __init__(self, key):
        self.__dv_key = key #your google developer api key to be given
        self.__book_query = ""
        self.__paper_query = ""
        self.__book_index = 1
        self.__paper_index = 1
        return

    def __search(self, query, index, max_limit=5):
        """
        Searches the required query and return the result
        :param query: the required query string.
        :param max_limit: the number of search result to be return, default is 5
        :return:
            returns the JSON file of required search result.
        :raises:
            raises the error if unable to connect the google search api (customsearch).
        """
        service = build("customsearch", "v1",
                        developerKey=self.__dv_key)
        res = service.cse().list(q=query,
                                 cx='015974940825320028887:zqooin_a9z4',
                                 num=max_limit,
                                 start=index,
                                 ).execute()
        data = '{"Books":['
        for i in range(5):
            data += '{"'+res['items'][i]['htmlTitle'] + '":"' + res['items'][i]['link'] + '"},'
        data += "],"
        data = data.encode('ascii', errors='ignore')
        data = self.strip_html(data)
        return data

    def strip_html(self,data):
        p = re.compile(r'<.*?>')
        return p.sub('',data)
    def search_book(self, query, max_limit=5):
        """
        Provides the books search result on amazon site as per the query
        :param query: Topic to search
        :param max_limit: Maximum number of search result to be shown
        :return: returns the JSON file of required search result.
        """
        query += " books"
        self.__book_query =  query
        return self.__search(self.__book_query, max_limit=max_limit, index=self.__book_index)

    def search_paper(self, query, max_limit=5):
        """
        Provides the research paper search result as per the query
        :param query: Topic to search
        :param max_limit:  Maximum number of search result to be shown
        :return: returns the JSON file of required search result.
        """
        query = "filetype:pdf ' " + query + "' research paper"
        self.__paper_query = query
        return self.__search(self.__paper_query, max_limit=max_limit, index=self.__paper_index)

    def search_next(self, default=0):
        """
        Provides the next search result from google search api
        :param default: If set to 0 research paper search result
                        is returned else books search result is returned
        :return: returns the JSON file of required search result.
        """
        if default:
            self.__book_index += 5
            return self.__search(self.__book_query, index=self.__book_index)
        else:
            self.__paper_index += 5
            return self.__search(self.__paper_index, index=self.__paper_index)

if __name__ == '__main__':
    with open('gsearch','r') as cred_file:
        key = cred_file.readline()
    gse = Search(key)
    print gse.search_book("data structure")
