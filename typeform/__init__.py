from .forms import Forms
from .responses import Responses
from .client import Client
from .insights import Insights

__all__ = ['Typeform']


class Typeform:
    """Typeform API client"""

    def __init__(self, token: str, headers: dict = {}):
        """Constructor for Typeform API client"""
        client = Client(token, headers=headers)
        self.__forms = Forms(client)
        self.__responses = Responses(client)
        self.__insights = Insights(client)

    @property
    def forms(self) -> Forms:
        return self.__forms

    @property
    def responses(self) -> Responses:
        return self.__responses

    @property
    def insights(self) -> Insights:
        return self.__insights
