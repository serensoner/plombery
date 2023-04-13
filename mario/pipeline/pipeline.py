from typing import Any, Dict, List, Type

from pydantic import BaseModel, Field, validator

from .task import Task
from .trigger import Trigger
from ._utils import prettify_name


class Pipeline(BaseModel):
    id: str
    name: str = None
    description: str = None
    params: Type[BaseModel] = Field(exclude=True, default=None)
    tasks: List[Task] = Field(default_factory=list)
    triggers: List[Trigger] = Field(default_factory=list)

    @validator("name", always=True)
    def generate_default_name(cls, name: str, values: Dict[str, Any]) -> str:
        if not name:
            return prettify_name(values["id"]).title()

        return name

    @validator("description", always=True)
    def generate_default_description(
        cls, description: str, values: Dict[str, Any]
    ) -> str:
        if not description:
            return cls.__doc__

        return description
