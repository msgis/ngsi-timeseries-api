# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.query_pattern import QueryPattern  # noqa: F401,E501
from swagger_server import util


class Query(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, entities: List[QueryPattern]=None, attributes: List[str]=None):  # noqa: E501
        """Query - a model defined in Swagger

        :param entities: The entities of this Query.  # noqa: E501
        :type entities: List[QueryPattern]
        :param attributes: The attributes of this Query.  # noqa: E501
        :type attributes: List[str]
        """
        self.swagger_types = {
            'entities': List[QueryPattern],
            'attributes': List[str]
        }

        self.attribute_map = {
            'entities': 'entities',
            'attributes': 'attributes'
        }

        self._entities = entities
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Query':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Query of this Query.  # noqa: E501
        :rtype: Query
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self) -> List[QueryPattern]:
        """Gets the entities of this Query.


        :return: The entities of this Query.
        :rtype: List[QueryPattern]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List[QueryPattern]):
        """Sets the entities of this Query.


        :param entities: The entities of this Query.
        :type entities: List[QueryPattern]
        """

        self._entities = entities

    @property
    def attributes(self) -> List[str]:
        """Gets the attributes of this Query.


        :return: The attributes of this Query.
        :rtype: List[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List[str]):
        """Sets the attributes of this Query.


        :param attributes: The attributes of this Query.
        :type attributes: List[str]
        """

        self._attributes = attributes