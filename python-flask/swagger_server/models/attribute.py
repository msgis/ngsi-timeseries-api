# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Attribute(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, value: object=None, type: str=None, metadata: object=None):  # noqa: E501
        """Attribute - a model defined in Swagger

        :param value: The value of this Attribute.  # noqa: E501
        :type value: object
        :param type: The type of this Attribute.  # noqa: E501
        :type type: str
        :param metadata: The metadata of this Attribute.  # noqa: E501
        :type metadata: object
        """
        self.swagger_types = {
            'value': object,
            'type': str,
            'metadata': object
        }

        self.attribute_map = {
            'value': 'value',
            'type': 'type',
            'metadata': 'metadata'
        }

        self._value = value
        self._type = type
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'Attribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Attribute of this Attribute.  # noqa: E501
        :rtype: Attribute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> object:
        """Gets the value of this Attribute.


        :return: The value of this Attribute.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value: object):
        """Sets the value of this Attribute.


        :param value: The value of this Attribute.
        :type value: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def type(self) -> str:
        """Gets the type of this Attribute.


        :return: The type of this Attribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Attribute.


        :param type: The type of this Attribute.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def metadata(self) -> object:
        """Gets the metadata of this Attribute.


        :return: The metadata of this Attribute.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this Attribute.


        :param metadata: The metadata of this Attribute.
        :type metadata: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata