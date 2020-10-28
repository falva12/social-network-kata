
class Timeline:
    def __init__(self):
        self.posts = {}
        self.posting_log = []

class User:
    def __init__(self, id=0, name='no name', timeline=Timeline()):
        self.id = id
        self.name = name
        self.wall = []
        self.timeline = timeline
        self.timeline.posts[name] = []
        self.following = [name]

    def post_comment(self, comment):
        self.wall.append(comment)
        self.timeline.posts[self.name].append(comment)
        self.timeline.posting_log.append(self.name)

    def add_following(self, user):
       self.following.append(user)
       self.post_comment(f'has started following {user}')

    def get_timeline(self):
        following_timeline = []
        for user in self.following:
            for post in self.timeline.posts[user]:
                following_timeline.append(user + ': '+ post)
        return following_timeline

    def get_ordered_timeline(self):
        following_posting_users = [user for user in self.timeline.posting_log if user in self.following]
        following_timeline = []
        posts_numbers = {}
        for user in following_posting_users:
            if user in posts_numbers.keys():
                posts_numbers[user] += 1
            else:
                posts_numbers[user] = 0
            user_posts = self.timeline.posts[user]
            user_post_number = posts_numbers[user]
            following_timeline.append(user + ': ' + user_posts[user_post_number])

        return following_timeline
