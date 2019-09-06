import random
from acme import Product


naming_adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
naming_nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_name(naming_adjectives, naming_nouns):
    adjective = random.choice(naming_adjectives)
    noun = random.choice(naming_nouns)
    return adjective + ' ' + noun


def generate_products(num_products=30):
    product_list = []
    for _ in range(num_products):
        name = generate_name(naming_adjectives, naming_nouns)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        product_list.append(
            Product(
                    name=name,
                    price=price,
                    weight=weight,
                    flammability=flammability
                    )
            )
    return product_list


def inventory_report(product_list):
    unique_names = get_unique_names(product_list)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print('Unique product names: ', len(unique_names))
    print('Average price:', get_average(product_list, 'price'))
    print('Average weight: ', get_average(product_list, 'weight'))
    print('Average flammability:', get_average(product_list, 'flammability'))


def get_unique_names(product_list):
    names = []
    for product in product_list:
        names.append(product.name)
    return list(set(names))


def get_average(product_list, attribute):
    values = []
    for product in product_list:
        values.append(getattr(product, attribute))
    return sum(values)/len(values)


if __name__ == "__main__":
    inventory_report(generate_products())
