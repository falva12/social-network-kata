from unittest import TestCase

from social_network import User, Timeline


class TestUser(TestCase):
    def test_alice_post_comment(self):
        Alice = User(1, 'Alice')
        Alice.post_comment('Esto es una prueba')
        Alice.post_comment('Esto es otra prueba')
        posts = [Alice.timeline.posts[0].content]
        posts.append(Alice.timeline.posts[1].content)
        self.assertEqual(posts, ['Esto es una prueba', 'Esto es otra prueba'])

    def test_bob_can_view_alice_timeline(self):
        timeline = Timeline()
        Alice = User(1, 'Alice', timeline)
        Alice.post_comment('Esto es una prueba')
        Bob = User(2, 'Bob', timeline)
        Alice.post_comment('Esto es otra prueba')
        posts = [Bob.timeline.posts[0].content]
        posts.append(Bob.timeline.posts[1].content)
        self.assertEqual(posts, ['Esto es una prueba', 'Esto es otra prueba'])

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

        Alice.post_comment('Esto es una prueba')
        Alice.post_comment('Esto es otra prueba')
        Bob.post_comment('Esto no se tiene que ver')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: has started following Alice', 'Alice: Esto es una prueba', 'Alice: Esto es otra prueba'])

    def test_get_timeline_charlie_follows_bob(self):
        timeline = Timeline()

        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)

        Charlie.post_comment('el numero cero')
        Charlie.add_following(Bob.name)

        Alice.post_comment('primero')
        Bob.post_comment('segundo')
        Alice.post_comment('tercero')
        Bob.post_comment('cuarto')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: el numero cero', 'Charlie: has started following Bob', 'Bob: segundo', 'Bob: cuarto'])


    def test_get_timeline_charlie_follows_alice_and_bob(self):
        timeline = Timeline()

        Alice = User(1, 'Alice', timeline)
        Bob = User(2, 'Bob', timeline)
        Charlie = User(3, 'Charlie', timeline)

        Charlie.add_following(Alice.name)
        Charlie.add_following(Bob.name)

        Alice.post_comment('primero')
        Bob.post_comment('segundo')
        Alice.post_comment('tercero')

        self.assertEqual(Charlie.get_timeline(), ['Charlie: has started following Alice', 'Charlie: has started following Bob',
                                                          'Alice: primero', 'Bob: segundo', 'Alice: tercero'])