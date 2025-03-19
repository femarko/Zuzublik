from datetime import datetime
from typing import Optional


class Zuzublik:
    def __init__(self, title, url, xpath, id: Optional[int] = None, creation_date: Optional[datetime] = None):
        self.id = id
        self.title = title
        self.url = url
        self.xpath = xpath
        self.creation_date = creation_date


def create_zuzublik(title, url, xpath) -> Zuzublik:
    return Zuzublik(title, url, xpath)
