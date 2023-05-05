
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'iPhone 14', 'description': 'Juicy organic strawberries.', 'price': 1099.99, 'url': 'https://i.ibb.co/r5n06vf/IMG-7445.jpg'},
    {'id': 2, 'name': 'Windows PhoneX', 'description': 'An individually-prepared tea or coffee of choice.', 'price': 873.49, 'url': 'https://i.ibb.co/yp5c9L1/IMG-7446.jpg'},
    {'id': 3, 'name': 'Nokia XP1', 'description': 'It has all the answers.', 'price': 829.99, 'url': 'https://i.ibb.co/SJkM9y5/IMG-7447.jpg'},
    {'id': 4, 'name': 'Windows OpenAI', 'description': 'Level up your programming skills.', 'price': 629.99, 'url': 'https://i.ibb.co/dQFqD8j/IMG-7451.jpg'},
    {'id': 5, 'name': 'Samsung NH4', 'description': '___________.', 'price': 599.99, 'url': 'https://i.ibb.co/B2QXQXh/IMG-7453.jpg'},
    {'id': 6, 'name': 'Tesla Phone RM1', 'description': '___________.', 'price': 789.99, 'url': 'https://i.ibb.co/tJSP595/IMG-7456.jpg'}
]


class Product:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.description = attrs.get("description")
        self.price = attrs.get("price")
        self.url = attrs.get("url")
        self.created_at = attrs.get("created_at")

    @property
    def to_row(self):
        return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
