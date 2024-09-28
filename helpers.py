from faker import Faker


class RandomUserGeneration:
    @staticmethod
    def generate_user_data():
        fake = Faker(locale="ru_RU")
        payload = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return payload
