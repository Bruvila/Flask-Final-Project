
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'iPhone 14', 'description': 'The latest and most powerful A18 chip', 'price': 1099.99, 'url': 'https://i.ibb.co/r5n06vf/IMG-7445.jpg'},
    {'id': 2, 'name': 'Windows PhoneX', 'description': 'The most used OS with the latest hardware', 'price': 873.49, 'url': 'https://i.ibb.co/yp5c9L1/IMG-7446.jpg'},
    {'id': 3, 'name': 'Nokia XP1', 'description': 'The most durable phone is back', 'price': 829.99, 'url': 'https://i.ibb.co/SJkM9y5/IMG-7447.jpg'},
    {'id': 4, 'name': 'Windows OpenAI', 'description': 'The first AI phone with Chat-GPT integration', 'price': 629.99, 'url': 'https://i.ibb.co/dQFqD8j/IMG-7451.jpg'},
    {'id': 5, 'name': 'Samsung NH4', 'description': 'The most reliable Android phone in the market', 'price': 599.99, 'url': 'https://i.ibb.co/B2QXQXh/IMG-7453.jpg'},
    {'id': 6, 'name': 'Tesla Phone RM1', 'description': 'The only smartphone ready to go to the space', 'price': 789.99, 'url': 'https://i.ibb.co/xCvDs82/Xiaomi20.png'},
    {'id': 7, 'name': 'Xiaomi Plus10', 'description': 'Durability, quality and 100px camera', 'price': 699.99, 'url': 'https://i.ibb.co/bsBZ5gZ/Xiaomi10.png'},
    {'id': 8, 'name': 'Motorola Rz7', 'description': 'High frequency band available everywhere', 'price': 529.99, 'url': 'https://i.ibb.co/8X1mW3P/motorola10.png'}
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
