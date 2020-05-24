from abc import ABC, abstractmethod


class TableQuery(ABC):
    async def body(self, filters=None):
        return [dict(
            columns=self._columns(),
            rows=await self._rows(filters),
            type='table'
        )]

    @abstractmethod
    def _columns(self):
        pass

    @abstractmethod
    async def _rows(self, filters):
        pass
