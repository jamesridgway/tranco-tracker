import os

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import registry, relationship

db_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data.sqlite')

engine = create_engine(f"sqlite+pysqlite:///{db_filename}", echo=True, future=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True)
    domain = Column(String, unique=True)

    ranks = relationship("Rank", back_populates="domain")


class Rank(Base):
    __tablename__ = 'ranks'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    domain_id = Column(Integer, ForeignKey('domains.id'))
    domain = relationship("Domain", back_populates="ranks")
    rank = Column(Integer)
