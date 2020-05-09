# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CommitDateOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'datetime',
        'committer': 'datetime'
    }

    attribute_map = {
        'author': 'author',
        'committer': 'committer'
    }

    def __init__(self, author=None, committer=None):  # noqa: E501
        """CommitDateOptions - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._committer = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if committer is not None:
            self.committer = committer

    @property
    def author(self):
        """Gets the author of this CommitDateOptions.  # noqa: E501


        :return: The author of this CommitDateOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CommitDateOptions.


        :param author: The author of this CommitDateOptions.  # noqa: E501
        :type: datetime
        """

        self._author = author

    @property
    def committer(self):
        """Gets the committer of this CommitDateOptions.  # noqa: E501


        :return: The committer of this CommitDateOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this CommitDateOptions.


        :param committer: The committer of this CommitDateOptions.  # noqa: E501
        :type: datetime
        """

        self._committer = committer

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CommitDateOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommitDateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
