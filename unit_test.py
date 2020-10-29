from unittest import TestCase

from social_network import User, Timeline, Message


class TestUser(TestCase):
    def test_alice_post_comment(self):
        timeline = Timeline()
        Alice = User(1, 'Alice', timeline)
        Alice.post_message('Esto es una prueba')
        Alice.post_message('Esto es otra prueba')
        messages = [timeline.messages[0].content]
        messages.append(timeline.messages[1].content)
        self.assertEqual(messages, ['Esto es una prueba', 'Esto es otra prueba'])

    def test_bob_can_view_alice_timeline(self):
        timeline = Timeline()
        Alice = User(1, 'Alice', timeline)
        Alice.post_message('Esto es una prueba')
        Bob = User(2, 'Bob', timeline)
        Alice.post_message('Esto es otra prueba')
        messages = [Bob.timeline.messages[0].content]
        messages.append(Bob.timeline.messages[1].content)
        self.assertEqual(messages, ['Esto es una prueba', 'Esto es otra prueba'])

    def test_charlie_follows_alice_and_bob(self):
        timeline = Timeline()
        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)
        Charlie.add_following(Alice.name)
        Charlie.add_following(Bob.name)
        self.assertEqual(Charlie.following, ['Alice', 'Bob'])

    def test_get_timeline_charlie_follows_alice(self):
        timeline = Timeline()

        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)

        Charlie.add_following(Alice.name)

        Alice.post_message('Esto es una prueba')
        Alice.post_message('Esto es otra prueba')
        Bob.post_message('Esto no se tiene que ver')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: has started following Alice', 'Alice: Esto es una prueba', 'Alice: Esto es otra prueba'])

    def test_get_timeline_charlie_follows_bob(self):
        timeline = Timeline()

        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)

        Charlie.post_message('el numero cero')
        Charlie.add_following(Bob.name)

        Alice.post_message('primero')
        Bob.post_message('segundo')
        Alice.post_message('tercero')
        Bob.post_message('cuarto')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: el numero cero', 'Charlie: has started following Bob', 'Bob: segundo', 'Bob: cuarto'])


    def test_get_timeline_charlie_follows_alice_and_bob(self):
        timeline = Timeline()

        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)

        Charlie.add_following(Alice.name)
        Charlie.add_following(Bob.name)

        Alice.post_message('primero')
        Bob.post_message('segundo')
        Alice.post_message('tercero')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: has started following Alice', 'Charlie: has started following Bob',
                                                          'Alice: primero', 'Bob: segundo', 'Alice: tercero'])