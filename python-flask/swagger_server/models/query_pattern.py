# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class QueryPattern(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, id_pattern: str=None, type: str=None, type_pattern: str=None):  # noqa: E501
        """QueryPattern - a model defined in Swagger

        :param id: The id of this QueryPattern.  # noqa: E501
        :type id: str
        :param id_pattern: The id_pattern of this QueryPattern.  # noqa: E501
        :type id_pattern: str
        :param type: The type of this QueryPattern.  # noqa: E501
        :type type: str
        :param type_pattern: The type_pattern of this QueryPattern.  # noqa: E501
        :type type_pattern: str
        """
        self.swagger_types = {
            'id': str,
            'id_pattern': str,
            'type': str,
            'type_pattern': str
        }

        self.attribute_map = {
            'id': 'id',
            'id_pattern': 'idPattern',
            'type': 'type',
            'type_pattern': 'typePattern'
        }

        self._id = id
        self._id_pattern = id_pattern
        self._type = type
        self._type_pattern = type_pattern

    @classmethod
    def from_dict(cls, dikt) -> 'QueryPattern':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryPattern of this QueryPattern.  # noqa: E501
        :rtype: QueryPattern
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this QueryPattern.


        :return: The id of this QueryPattern.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this QueryPattern.


        :param id: The id of this QueryPattern.
        :type id: str
        """

        self._id = id

    @property
    def id_pattern(self) -> str:
        """Gets the id_pattern of this QueryPattern.


        :return: The id_pattern of this QueryPattern.
        :rtype: str
        """
        return self._id_pattern

    @id_pattern.setter
    def id_pattern(self, id_pattern: str):
        """Sets the id_pattern of this QueryPattern.


        :param id_pattern: The id_pattern of this QueryPattern.
        :type id_pattern: str
        """

        self._id_pattern = id_pattern

    @property
    def type(self) -> str:
        """Gets the type of this QueryPattern.


        :return: The type of this QueryPattern.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this QueryPattern.


        :param type: The type of this QueryPattern.
        :type type: str
        """

        self._type = type

    @property
    def type_pattern(self) -> str:
        """Gets the type_pattern of this QueryPattern.


        :return: The type_pattern of this QueryPattern.
        :rtype: str
        """
        return self._type_pattern

    @type_pattern.setter
    def type_pattern(self, type_pattern: str):
        """Sets the type_pattern of this QueryPattern.


        :param type_pattern: The type_pattern of this QueryPattern.
        :type type_pattern: str
        """

        self._type_pattern = type_pattern