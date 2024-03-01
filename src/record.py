from __future__ import annotations

import typing

from .logger import logger


class Record(typing.NamedTuple):
    id: int
    lic: int
    time: float
    
    
    @classmethod
    def parse(cls, text: str) -> list[Record]:
        str_records = text.split(";")
        str_records = [s.strip() for s in str_records]
        str_records = [s for s in str_records if len(s) > 0]
        records = []
        for s in str_records:
            try:
                record = cls._parse_record(s)
                records.append(record)
            except Exception as e:
                logger.error(f"{e}")
        return records
    
    @classmethod
    def _parse_record(cls, text: str) -> Record:
        fields = text.split(",")
        return cls(int(fields[1]), int(fields[3]), float(fields[2]))
    
