from pydantic import BaseModel


class FollowRequest(BaseModel):
    user_id: int  # الشخص الذي تريد متابعته