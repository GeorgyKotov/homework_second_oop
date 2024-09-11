import pprint


def get_my_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            ingredients = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    my_cook_book = get_my_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish in my_cook_book.keys():
            for ingredient in my_cook_book[dish]:
                ingredients = {}
                ingredient_name = ingredient['ingredient_name']
                ingredients['measure'] = ingredient['measure']
                if ingredient_name in shop_list.keys():
                    recurring_ingredient = shop_list[ingredient_name]
                    ingredients['quantity'] = ingredient['quantity'] * person_count + recurring_ingredient['quantity']
                else:
                    ingredients['quantity'] = ingredient['quantity'] * person_count
                shop_list[ingredient_name] = ingredients
    return dict(sorted(shop_list.items()))


pprint.pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2), width=80)
