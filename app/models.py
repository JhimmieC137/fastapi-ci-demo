from pydantic import BaseModel


class BaseParams(BaseModel):
    left: int
    right: int | None = None


class DivideParams(BaseParams):
    ...
