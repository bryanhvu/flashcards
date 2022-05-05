from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
engine = create_engine('sqlite:///card_bank.db')

Base = declarative_base()


class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False, unique=True)
    cards = relationship("Card", backref="card")


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    front = Column(String(250), nullable=False, unique=True)
    back = Column(String(500), nullable=False)
    deck_id = Column(Integer, ForeignKey('decks.id'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# cards = session.query(Card).all()
# decks = session.query(Deck).all()
