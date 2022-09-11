'''Fake data factories for MP Data'''
import factory
import pandas as pd
from util import AutoModel

MemberFactory = factory.make_factory(AutoModel,
    id = factory.Sequence(lambda n: n),
    firstname = factory.Faker('first_name'),
    lastname = factory.Faker('last_name')
)


if __name__ == "__main__":
    members = pd.DataFrame.from_records([i.props for i in MemberFactory.create_batch(10)])
    members.to_csv('members.csv')