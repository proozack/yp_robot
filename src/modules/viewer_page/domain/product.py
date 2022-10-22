from dataclasses import dataclass


@dataclass(unsafe_hash=False)
class Product():
    url: str
    title: str
    price: float
    currency: str
    main_image: str
    brand: str

    def __repr__(self):
        return '<Product {} {}{}>'.format(self.title, self.price, self.currency)
