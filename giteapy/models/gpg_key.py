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


class GPGKey(object):
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
        'can_certify': 'bool',
        'can_encrypt_comms': 'bool',
        'can_encrypt_storage': 'bool',
        'can_sign': 'bool',
        'created_at': 'datetime',
        'emails': 'list[GPGKeyEmail]',
        'expires_at': 'datetime',
        'id': 'int',
        'key_id': 'str',
        'primary_key_id': 'str',
        'public_key': 'str',
        'subkeys': 'list[GPGKey]'
    }

    attribute_map = {
        'can_certify': 'can_certify',
        'can_encrypt_comms': 'can_encrypt_comms',
        'can_encrypt_storage': 'can_encrypt_storage',
        'can_sign': 'can_sign',
        'created_at': 'created_at',
        'emails': 'emails',
        'expires_at': 'expires_at',
        'id': 'id',
        'key_id': 'key_id',
        'primary_key_id': 'primary_key_id',
        'public_key': 'public_key',
        'subkeys': 'subkeys'
    }

    def __init__(self, can_certify=None, can_encrypt_comms=None, can_encrypt_storage=None, can_sign=None, created_at=None, emails=None, expires_at=None, id=None, key_id=None, primary_key_id=None, public_key=None, subkeys=None):  # noqa: E501
        """GPGKey - a model defined in Swagger"""  # noqa: E501

        self._can_certify = None
        self._can_encrypt_comms = None
        self._can_encrypt_storage = None
        self._can_sign = None
        self._created_at = None
        self._emails = None
        self._expires_at = None
        self._id = None
        self._key_id = None
        self._primary_key_id = None
        self._public_key = None
        self._subkeys = None
        self.discriminator = None

        if can_certify is not None:
            self.can_certify = can_certify
        if can_encrypt_comms is not None:
            self.can_encrypt_comms = can_encrypt_comms
        if can_encrypt_storage is not None:
            self.can_encrypt_storage = can_encrypt_storage
        if can_sign is not None:
            self.can_sign = can_sign
        if created_at is not None:
            self.created_at = created_at
        if emails is not None:
            self.emails = emails
        if expires_at is not None:
            self.expires_at = expires_at
        if id is not None:
            self.id = id
        if key_id is not None:
            self.key_id = key_id
        if primary_key_id is not None:
            self.primary_key_id = primary_key_id
        if public_key is not None:
            self.public_key = public_key
        if subkeys is not None:
            self.subkeys = subkeys

    @property
    def can_certify(self):
        """Gets the can_certify of this GPGKey.  # noqa: E501


        :return: The can_certify of this GPGKey.  # noqa: E501
        :rtype: bool
        """
        return self._can_certify

    @can_certify.setter
    def can_certify(self, can_certify):
        """Sets the can_certify of this GPGKey.


        :param can_certify: The can_certify of this GPGKey.  # noqa: E501
        :type: bool
        """

        self._can_certify = can_certify

    @property
    def can_encrypt_comms(self):
        """Gets the can_encrypt_comms of this GPGKey.  # noqa: E501


        :return: The can_encrypt_comms of this GPGKey.  # noqa: E501
        :rtype: bool
        """
        return self._can_encrypt_comms

    @can_encrypt_comms.setter
    def can_encrypt_comms(self, can_encrypt_comms):
        """Sets the can_encrypt_comms of this GPGKey.


        :param can_encrypt_comms: The can_encrypt_comms of this GPGKey.  # noqa: E501
        :type: bool
        """

        self._can_encrypt_comms = can_encrypt_comms

    @property
    def can_encrypt_storage(self):
        """Gets the can_encrypt_storage of this GPGKey.  # noqa: E501


        :return: The can_encrypt_storage of this GPGKey.  # noqa: E501
        :rtype: bool
        """
        return self._can_encrypt_storage

    @can_encrypt_storage.setter
    def can_encrypt_storage(self, can_encrypt_storage):
        """Sets the can_encrypt_storage of this GPGKey.


        :param can_encrypt_storage: The can_encrypt_storage of this GPGKey.  # noqa: E501
        :type: bool
        """

        self._can_encrypt_storage = can_encrypt_storage

    @property
    def can_sign(self):
        """Gets the can_sign of this GPGKey.  # noqa: E501


        :return: The can_sign of this GPGKey.  # noqa: E501
        :rtype: bool
        """
        return self._can_sign

    @can_sign.setter
    def can_sign(self, can_sign):
        """Sets the can_sign of this GPGKey.


        :param can_sign: The can_sign of this GPGKey.  # noqa: E501
        :type: bool
        """

        self._can_sign = can_sign

    @property
    def created_at(self):
        """Gets the created_at of this GPGKey.  # noqa: E501


        :return: The created_at of this GPGKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GPGKey.


        :param created_at: The created_at of this GPGKey.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def emails(self):
        """Gets the emails of this GPGKey.  # noqa: E501


        :return: The emails of this GPGKey.  # noqa: E501
        :rtype: list[GPGKeyEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this GPGKey.


        :param emails: The emails of this GPGKey.  # noqa: E501
        :type: list[GPGKeyEmail]
        """

        self._emails = emails

    @property
    def expires_at(self):
        """Gets the expires_at of this GPGKey.  # noqa: E501


        :return: The expires_at of this GPGKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this GPGKey.


        :param expires_at: The expires_at of this GPGKey.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def id(self):
        """Gets the id of this GPGKey.  # noqa: E501


        :return: The id of this GPGKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GPGKey.


        :param id: The id of this GPGKey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key_id(self):
        """Gets the key_id of this GPGKey.  # noqa: E501


        :return: The key_id of this GPGKey.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GPGKey.


        :param key_id: The key_id of this GPGKey.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def primary_key_id(self):
        """Gets the primary_key_id of this GPGKey.  # noqa: E501


        :return: The primary_key_id of this GPGKey.  # noqa: E501
        :rtype: str
        """
        return self._primary_key_id

    @primary_key_id.setter
    def primary_key_id(self, primary_key_id):
        """Sets the primary_key_id of this GPGKey.


        :param primary_key_id: The primary_key_id of this GPGKey.  # noqa: E501
        :type: str
        """

        self._primary_key_id = primary_key_id

    @property
    def public_key(self):
        """Gets the public_key of this GPGKey.  # noqa: E501


        :return: The public_key of this GPGKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this GPGKey.


        :param public_key: The public_key of this GPGKey.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def subkeys(self):
        """Gets the subkeys of this GPGKey.  # noqa: E501


        :return: The subkeys of this GPGKey.  # noqa: E501
        :rtype: list[GPGKey]
        """
        return self._subkeys

    @subkeys.setter
    def subkeys(self, subkeys):
        """Sets the subkeys of this GPGKey.


        :param subkeys: The subkeys of this GPGKey.  # noqa: E501
        :type: list[GPGKey]
        """

        self._subkeys = subkeys

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
        if issubclass(GPGKey, dict):
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
        if not isinstance(other, GPGKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
