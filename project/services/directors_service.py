from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """
        Получить режиссера по его id
        :param pk: id режиссера
        :return: director
        """
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None,  status: Optional[str] = None) -> list[Director]:
        """
        Получить всех режиссеров
        :param page: страница
        :param status: статус
        :return: list[directors]
        """
        return self.dao.get_all(page=page)
