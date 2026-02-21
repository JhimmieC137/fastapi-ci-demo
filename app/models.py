from pydantic import BaseModel


class BaseParams(BaseModel):
    left: int | None = None
    right: int | None = None


class DivideParams(BaseParams):
    ...
