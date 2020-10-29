import datetime

class Timeline:
    def __init__(self):
        self.posts = []

class message:
    def __init__(self, content, user_name):
        self.user_name = user_name
        self.content = content
        self.timestamp = datetime.datetime.now().timestamp()

class User:
    def __init__(self, id=0, name='no name', timeline=Timeline()):
        self.id = id
        self.name = name
        self.timeline = timeline
        self.following = []

    def post_comment(self, comment):
        self.timeline.posts.append(message(comment, self.name))

    def add_following(self, user):
       self.following.append(user)
       self.post_comment(f'has started following {user}')

    def get_timeline(self):
        user_list = self.following
        user_list.append(self.name)
        return [x.user_name + ': '+ x.content for x in self.timeline.posts if x.user_name in user_list]