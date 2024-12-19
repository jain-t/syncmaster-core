from typing import override
from pydantic import BaseModel

from abstract.enforcers import EnforceDocStringBaseClass


class SMBaseClass(BaseModel, metaclass=EnforceDocStringBaseClass):
    """SMBaseClass is an abstract base class for implementing a syncmaster library."""

    def to_dict(self):
        """
        Converts the object to a dictionary representation. Checks if the object has a `to_dict()` method and calls it.
        If the object does not have a `to_dict()` method, it raises a `NotImplementedError`. Also includes the object's
        attributes in the dictionary. If object is another class, it calls `to_dict()` on the related instance.

        Returns:
            dict: A dictionary containing the key-value pairs representing the object's attributes.
        """
        dict_obj = {}
        for field in self.model_fields:
            field_value = getattr(self, field)
            if hasattr(field_value, "to_dict"):
                dict_obj[field] = field_value.to_dict()
            else:
                dict_obj[field] = field_value
        return dict_obj

    @classmethod
    def from_dict(cls, payload: dict):
        """
        Create an instance of the class from a dictionary.

        Args:
            payload (dict): A dictionary containing the attributes to initialize the class.

        Returns:
            An instance of the class.
        """
        return cls(**payload)



class ThirdPartyPayload(SMBaseClass):
    """
    ThirdPartyPayload is a pydantic model for the third party payload.

    """
    
    @property
    def app_name(self) -> str:
        raise NotImplementedError("Method app_name is not implemented.")
    
    @override
    def to_dict(self):
        dict__ = super().to_dict()
        dict__["app_name"] = self.app_name
        return dict__
