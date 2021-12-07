from sqlalchemy import Boolean, Column, ForeignKey, Integer, \
    String, Date, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Clan(Base):
    __tablename__ = "clans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True)
    img_link = Column(String, unique=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    pass_hash = Column(String)
    img_link = Column(String, unique=True)
    clan = Column(Integer, ForeignKey("clans.id"))
    is_active = Column(Boolean, default=True)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    players_per_team = Column(Integer)
    points_join = Column(Integer)
    points_win = Column(Integer)
    points_loss = Column(Integer)
    points_tie = Column(Integer)
    max_bet = Column(Integer)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True)
    details = Column(String(300))
    date = Column(Date)


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True)
    details = Column(String(300))
    event = Column(Integer, ForeignKey("events.id"))
    game = Column(Integer, ForeignKey("games.id"))


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True)
    details = Column(String(300))


class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("users.id"))
    room = Column(Integer, ForeignKey("rooms.id"))
    action = Column(Integer, ForeignKey("actions.id"))
    date_time = Column(DateTime)
    points = Column(Integer)
