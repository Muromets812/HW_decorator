import requests
from dekorator import logger


class Marvel():
    hero_book = []

    def _load_heroes_info(self):
        url = 'https://akabab.github.io/superhero-api/api'
        params = '/all.json'
        resp = requests.get(f'{url}/{params}')
        info = resp.json()
        return info

    @logger
    def add_hero_info(self, name):
        info = self._load_heroes_info()
        hero = [hero for hero in info if name == hero["name"]]
        for attr in hero:
            self.hero_book.append({'name': attr['name'], 'intelligence': attr['powerstats']['intelligence']})
        return

    @logger
    def sorted_hero(self):
        smart_hero = {'name': '', 'intelligence': 0}
        for value in self.hero_book:
            if int(value['intelligence']) > int(smart_hero['intelligence']):
                smart_hero = value
        print(f"Самый умный герой из выбранных для сравнения {smart_hero['name']}")
        return


if __name__ == '__main__':
    heroes = Marvel()
    heroes.add_hero_info('Thanos')
    heroes.add_hero_info('Captain America')
    heroes.add_hero_info('Hulk')
    heroes.sorted_hero()
