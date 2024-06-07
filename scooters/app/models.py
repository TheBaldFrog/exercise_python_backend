from __future__ import annotations

import dataclasses
import typing as tp

import asyncpg


@dataclasses.dataclass
class User:
    id: str

    @classmethod
    def from_db(cls, user_id: tp.Optional[str]) -> User:
        if user_id:
            return User(id=user_id)
        return None


@dataclasses.dataclass
class Location:
    lat: float
    lon: float


@dataclasses.dataclass
class Scooter:
    id: str
    location: Location
    user: tp.Optional[User] = None

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Scooter:
        return cls(
            id=row["id"],
            location=Location(lat=row["location"][0], lon=row["location"][1]),
            user=User.from_db(row["user"]),
        )
