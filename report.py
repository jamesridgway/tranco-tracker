import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from models import mapper_registry, Base, engine, Domain

sns.set_theme(style="darkgrid")

load_dotenv()

mapper_registry.metadata.create_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def plot_domain(domain):
    fig, ax = plt.subplots()
    fig.set_figwidth(16)
    fig.set_figheight(9)

    dates = []
    ranks = []
    for rank in domain.ranks:
        dates.append(rank.date)
        ranks.append(rank.rank)
    ax.plot(dates, ranks)

    ax.set_title(domain.domain)
    ax.set_xlabel('Date')
    ax.set_ylabel('Rank')
    ax.set_ylim(ax.get_ylim()[::-1])
    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    fig.savefig(f'./output/{domain.domain}.png')


for domain in session.query(Domain).all():
    plot_domain(domain)
