from datetime import datetime
from typing import Optional

from apscheduler.triggers.base import BaseTrigger
from pydantic import BaseModel, ConfigDict, field_serializer


class Trigger(BaseModel):
    id: str
    name: str
    schedule: BaseTrigger
    description: Optional[str] = __doc__
    params: Optional[BaseModel] = None
    paused: bool = False
    next_fire_time: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    @field_serializer('schedule')
    def serialize_bt(self, schedule: BaseTrigger, _info):
        return str(bt)
