class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        for post_number in range(len(self.posts)):
            print(f'Post #{post_number+1}:')
            print(f'"{self.posts[post_number]}"')
            print('----------------------------------')

def main():
    User1 = SocialMediaProfile('johndoe')
    User1.add_post("Hello, world!")
    User1.add_post("Had a great day at the park!")
    User1.add_post("What's up, Natalie? How are you?")
    User1.display_timeline()

if __name__ == "__main__":
    main()