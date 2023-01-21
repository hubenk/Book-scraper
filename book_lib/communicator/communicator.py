""" Module containing Communicator class."""

import grequests
import requests


class Communicator(object):
    """
    Class that makes async requests and returns responses
    """

    def __init__(self, link_pool):
        """:param link_pool: list of page links"""
        self.__link_pool = link_pool

    def get_responses(self):
        """:return:  list of responses"""
        g_requests = (grequests.get(url) for url in self.pool)
        responses = grequests.map(g_requests, size=50)
        return responses

    def get_single_response(self):
        """:return: single response"""
        response = requests.get(self.pool)
        return response

    @property
    def pool(self):
        """:return: link pool generator"""
        return self.__link_pool
