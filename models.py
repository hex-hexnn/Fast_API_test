from typing import Optional
from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str = Field(index=True)
    description: Optional[str] = None
    is_done: bool = False
    priority: int = Field(default=3, ge=1, le=5, description="Priority item (1-5)")
