from pydantic import BaseModel # type: ignore

class ChatRequest(BaseModel):
    session_id: str # its the unique id of the user
    query: str 
