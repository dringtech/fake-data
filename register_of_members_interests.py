'''Fake data factories for MP Data'''
import os

import factory

import datagen

members = datagen.Generator(
    id=factory.Sequence(lambda n: n),
    firstname=factory.Faker('first_name'),
    lastname=factory.Faker('last_name')
)

if __name__ == "__main__":
    os.chdir('working')
    members.create_batch(10)
    print(members)
    members.save_csv('members.csv')
