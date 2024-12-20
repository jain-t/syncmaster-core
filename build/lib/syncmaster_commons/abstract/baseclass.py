from typing import override

# from abstract.enforcers import EnforceDocStringBaseClass
from pydantic import BaseModel

from syncmaster_commons.abstract.enforcers import EnforceDocStringBaseClass


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
    ThirdPartyPayload is an abstract base class that represents a payload from a third-party application.
    Attributes:
        task_id (int): The ID of the task.
        user_id (str): The ID of the user.
        org_id (int): The ID of the organization.
        org_name (str): The name of the organization.
    Property:
        app_name (str): Abstract property that should return the name of the application.
        _payload_type (str): Abstract property that should return the type of the payload.
        payload: Abstract property that should return the payload data.
        to_dict (dict): Converts the object to a dictionary representation, including the `app_name` attribute.
    """
    task_id: int
    user_id: str
    org_id: int
    org_name: str

    
    @property
    def app_name(self) -> str:
        """
        Returns the name of the application.

        This method should be implemented by subclasses to provide the
        specific name of the application.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Method app_name is not implemented.")
    
    @property
    def _payload_type(self) -> str:
        """
        Returns the type of the payload.

        This method should be implemented by subclasses to provide the
        specific payload type.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Method _payload_type is not implemented.")
    
    @property
    def payload(self):
        """
        Returns the payload data.

        This method should be implemented by subclasses to provide the
        specific payload data.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Method payload is not implemented.")
    
    @override
    def to_dict(self):
        """
        Convert the object to a dictionary representation.

        This method overrides the `to_dict` method from the superclass to include
        the `app_name` attribute in the dictionary representation.

        Returns:
            dict: A dictionary containing the object's data, including the `app_name` attribute.
        """
        _d_ = super().to_dict()
        _d_["app_name"] = self.app_name
        return _d_
