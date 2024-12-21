from abstract.baseclass import ThirdPartyPayload

from syncmaster_commons.gupshup.incoming_payloads import IncomingPayLoad


class _AgentRequestPayloadGupshup(ThirdPartyPayload):
    """
    AgentRequestPayload is a pydantic model for the agent request payload.

    """    
    _incoming_payload: IncomingPayLoad
    
    @property
    def app_name(self) -> str:
        return 'gupshup'
    
    @property
    def payload_type(self) -> str:
        return self._incoming_payload.payload.payload.payload_type
    
    @property
    def payload(self) -> dict:
        payload = self._incoming_payload.payload.payload.payload
        output_dict = payload.to_dict()
        output_dict["payload_type"] = self.payload_type
        return output_dict
        


    @classmethod
    def from_dict(cls, payload_dict: dict) -> "_AgentRequestPayloadGupshup":
        """
        Creates a AgentRequestPayload object from a dictionary.
        Args:
            payload_dict (dict): The dictionary containing the payload data.
        Returns:
            AgentRequestPayload: The AgentRequestPayload object created from the dictionary.
        """
        return cls(
            _incoming_payload=payload_dict["incoming_payload"],
            task_id=payload_dict["task_id"],
            user_id=payload_dict["user_id"],
            org_id=payload_dict["org_id"],
        )
    
