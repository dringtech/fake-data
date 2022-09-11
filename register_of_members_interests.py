'''Fake data factories for MP Data'''
import os

import factory

import datagen

LOCALE = "en_GB"

members = datagen.Generator(
    id=factory.Sequence(lambda n: n),
    firstname=factory.Faker('first_name'),
    lastname=factory.Faker('last_name')
)

constituency = datagen.Generator(
    id=factory.Sequence(lambda n: n),
    name=factory.Faker('administrative_unit', locale=LOCALE),
)


if __name__ == "__main__":
    with factory.debug():
        os.chdir('working')

        constituency.build_batch(10)
        members.build_batch(10)
        print(members)
        members.save_csv('members.csv')
