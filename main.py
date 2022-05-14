from time import sleep

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from api_client import TrancoApi
from models import mapper_registry, Base, engine, Domain, Rank

load_dotenv()

mapper_registry.metadata.create_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.commit()

api = TrancoApi()

for domain in session.query(Domain).all():
    ranks = api.rank(domain.domain)
    for date in ranks.dates():
        instance = session.query(Rank).filter_by(domain=domain, date=date.strftime("%Y-%m-%d")).first()
        if not instance:
            session.add(Rank(domain=domain, date=date, rank=ranks.for_date(date)))
    session.commit()
    sleep(2)
