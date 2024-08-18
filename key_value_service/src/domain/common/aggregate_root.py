from abc import ABC
from dataclasses import dataclass, field
from typing import List

from src.domain.common.event import BaseEvent
from src.domain.common.entity import BaseEntity


@dataclass()
class AggregateRoot(BaseEntity, ABC):
    _events: List[BaseEvent] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def raise_event(self, event: BaseEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> List[BaseEvent]:
        return self._events.copy()
