class Post:
    def __init__(self, user_name, message):
        self.message = message
        self.user_name = user_name
post_list = []
post1 = Post("MrsG","Hello 2B")
post_list.append(post1)
post2 = Post("MrsH","Hello 3B")
post_list.append(post2)
post3 = Post("MrsI","Hello 2A")
post_list.append(post3)
print(post_list)
del post_list[2]
print(post_list)
post4 = Post("MrsJ","Hello 6A")
post_list.append(post4)
print(post_list)
