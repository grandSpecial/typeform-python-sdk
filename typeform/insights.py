from .client import Client

class Insights:
    """Typeform Insights API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Insights class"""
        self.__client = client

    def summary(self, uid: str) -> str:
        """
        Returns form level and individual question level insights for a given form.
        """
        return self.__client.request('get', '/insights/%s/summary' % uid)