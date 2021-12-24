import json
from datetime import date


class ShoppingCart:
    def __init__(self):
        self.__shopping_cart = []

    def get_shopping_cart(self):
        return self.__shopping_cart

    def set_shopping_cart(self, shopping_cart):
        self.__shopping_cart = shopping_cart

    def addProduct(self, p):
        # Using the unique_identifier to identify the product
        unique_identifier = p.get_unique_identifier()
        for item in self.__shopping_cart:
            if item.get_unique_identifier() == unique_identifier:
                print("\n\t\tERROR\t\t\n")
                print(">>>>>>>>> The Identifier is not unique, it has been occupied by another product(s).<<<<<<<<<\n")
                return False
        self.__shopping_cart.append(p)
        return True

    def removeProduct(self, p):
        try:
            self.__shopping_cart.remove(p)
            return True
        except Exception as e:
            print("\n\t\tERROR\t\t\n")
            return False

    def getContents(self):
        content_list = [str(item) for item in self.__shopping_cart]
        # Sort the product in alphabetical order.
        content_list.sort()
        return content_list

    def changeProductQuantity(self, p, q):
        for item in self.__shopping_cart:
            if item.get_unique_identifier() == p:
                item.set_quantity(q)
                return True
        return False

    def to_json(self):
        return json.dumps({"shopping_cart":
                               [item.to_dict() for item in self.__shopping_cart]},
                          separators=(',', ': '), indent=4)

    def __str__(self):
        return str([str(item) for item in self.__shopping_cart])


class Product:

    def __init__(self, name: str, price: float, unique_identifier: str, quantity: int, brand: str):
        """

        :param name: The Product name
        :param price: The product price
        :param unique_identifier: The unique_identifier which has a fixed length, 13, and can only contain digits
        :param quantity: The quantity of the product in shopping cart.
        :param brand: The product brand
        """
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__unique_identifier = unique_identifier
        assert len(self.__unique_identifier) == 13, "The Length of this Unique_Identifier is not 13"
        assert self.__unique_identifier.isnumeric(), "Not every char is a digit in this Unique_Identifier"
        self.__brand = brand

    def to_dict(self):
        new_dict = {str(type(self).__name__): {attr_name.split("__")[1]: self.__dict__[attr_name] for attr_name in
                                               self.__dict__.keys()}}
        return new_dict

    def to_json(self):
        new_dict = self.to_dict()
        return json.dumps(new_dict, separators=(',', ': '), indent=4)

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity: int):
        self.__quantity = quantity

    def get_unique_identifier(self):
        return self.__unique_identifier

    def set_unique_identifier(self, unique_identifier: str):
        self.__unique_identifier = unique_identifier

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand


class Clothing(Product):

    def __init__(self, name, price, unique_identifier, quantity, brand, size: str, material: str):
        """

        :param name:
        :param price:
        :param unique_identifier:
        :param quantity:
        :param brand:
        The above attributes are father's attributes
        :param size: The clothing size.
        :param material: The clothing material.
        """
        super().__init__(name, price, unique_identifier, quantity, brand)
        self.__size = size
        self.__material = material

    def set_size(self, size: str):
        self.__size = size

    def get_size(self) -> str:
        return self.__size

    def set_material(self, material: str):
        self.__material = material

    def get_material(self) -> str:
        return self.__material


class Food(Product):

    def __init__(self, name, price, unique_identifier, quantity, brand, expiry_date, gluten_free: bool,
                 suitable_for_vegans: bool):
        """

        :param name:
        :param price:
        :param unique_identifier:
        :param quantity:
        :param brand:
        The above attributes are father's attributes
        :param expiry_date: The date
        :param gluten_free: A flag to tell whether it's gluten free or not
        :param suitable_for_vegans: A flag to tell whether it's suitable for vegans or not
        """
        super().__init__(name, price, unique_identifier, quantity, brand)
        self.__expiry_date = expiry_date
        self.__gluten_free = gluten_free
        self.__suitable_for_vegans = suitable_for_vegans

    def get_expiry_date(self):
        return self.__expiry_date

    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    def get_gluten_free(self) -> bool:
        return self.__gluten_free

    def set_gluten_free(self, gluten_free: bool):
        self.__gluten_free = gluten_free

    def get_suitable_for_vegans(self) -> bool:
        return self.__suitable_for_vegans

    def set_suitable_for_vegans(self, suitable_for_vegas: bool):
        self.__suitable_for_vegans = suitable_for_vegas


class Phone(Product):

    def __init__(self, name: str, price, unique_identifier, quantity, brand, size: str, memory: str, storage: str):
        """
        :param name:
        :param price:
        :param unique_identifier:
        :param quantity:
        :param brand:
        The above attributes are father's attributes
        The additional attributes, 3 of them, size, memory, storage respectively
        :param size: The screen size, such as 6 inches
        :param memory: The memory of phones such as 8Gb
        :param storage: The Storage capacity of phones such as 128 Gb
        """
        super().__init__(name, price, unique_identifier, quantity, brand)
        self.__size = size
        self.__memory = memory
        self.__storage = storage

    def get_size(self) -> str:
        return self.__size

    def set_size(self, size: str):
        self.__size = size

    def get_memory(self) -> str:
        return self.__memory

    def set_memory(self, memory: str):
        self.__memory = memory

    def get_storage(self) -> str:
        return self.__storage

    def set_storage(self, storage: str):
        self.__storage = storage


if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    print('The program has started')
    terminated = False
    while not terminated:
        c = input(">>> Insert your next command (H for help): ")
        if c == 'T':
            break

        # Adding product to the shopping cart
        elif c == "A":
            print(">>> Adding a new Product")
            product_type = input(">>> Insert its type: ")

            if product_type == "Clothing":
                name = input(">>> Insert its name: ")

                try:
                    price = float(input(">>> Insert its price (£): "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The price you enter is not a number!")
                    continue

                try:
                    quantity = int(input(">>> Insert its quantity: "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The quantity you enter is not a number!")
                    continue

                brand = input(">>> Insert its brand: ")

                ean_code = input(">>> Insert its EAN code: ")
                if not ean_code.isnumeric() or len(ean_code) != 13:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The ean_code you enter is not validated!")
                    continue

                size = input(">>> Insert its size: ")
                material = input(">>> Insert its material: ")
                cloth_item = Clothing(name=name, price=price, quantity=quantity,
                                      brand=brand, unique_identifier=ean_code,
                                      size=size, material=material)
                if shopping_cart.addProduct(cloth_item):
                    print(">>> The product {} has been added to the cart".format(name))
                    print(">>> The cart contains {} products".format(len(shopping_cart.getContents())))
                else:
                    print(">>> The ean_code is overlapping")

            elif product_type == "Food":
                name = input(">>> Insert its name: ")
                try:
                    price = float(input(">>> Insert its price (£): "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The price you enter is not a number!")
                    continue
                try:
                    quantity = int(input(">>> Insert its quantity: "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The quantity you enter is not a number!")
                    continue

                brand = input(">>> Insert its brand: ")

                ean_code = input(">>> Insert its EAN code: ")
                if not ean_code.isnumeric() or len(ean_code) != 13:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The ean_code you enter is not validated!")
                    continue
                expiry_date = input(">>> Insert its expiry date (DD/MM/YYYY): ")
                # using datetime to make sure the expiry date is valid
                try:
                    date_data = expiry_date.split("/")
                    assert len(date_data) == 3, "\n>>> The date format is not correct!"
                    [day, month, year] = expiry_date.split("/")
                    date_type_data = date(int(year), int(month), int(day))
                except Exception as e:
                    print(e)
                    print(">>> Please check the date!")
                    print()
                    continue
                gluten_free = input(">>> Insert it's Gluten Free or not(Y or N): ")
                if gluten_free in ["Y", "N"]:
                    gluten_free = True if gluten_free == "Y" else False
                else:
                    print(">>> The letter you entered is not Y nor N, please check it.")
                    continue

                suitable_for_vegans = input(">>> Insert it's suitable for vegans or not(Y or N): ")
                if suitable_for_vegans in ["Y", "N"]:
                    suitable_for_vegans = True if suitable_for_vegans == "Y" else False
                else:
                    print(">>> The letter you entered is not Y nor N, please check it.")
                    continue

                food_item = Food(name=name, price=price, quantity=quantity, brand=brand, unique_identifier=ean_code,
                                 expiry_date=expiry_date, gluten_free=gluten_free,
                                 suitable_for_vegans=suitable_for_vegans)

                if shopping_cart.addProduct(food_item):
                    print(">>> The product {} has been added to the cart".format(name))
                    print(">>> The cart contains {} products".format(len(shopping_cart.getContents())))
                else:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The ean_code is overlapping")

            elif product_type == "Phone":
                name = input(">>> Insert its name: ")
                try:
                    price = float(input(">>> Insert its price (£): "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The price you enter is not a number!")
                    continue

                try:
                    quantity = int(input(">>> Insert its quantity: "))
                except Exception as e:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The quantity you enter is not a number!")
                    continue

                brand = input(">>> Insert its brand: ")

                ean_code = input(">>> Insert its EAN code: ")
                if not ean_code.isnumeric() or len(ean_code) != 13:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The ean_code you enter is not validated!")
                    continue

                size = input(">>> Insert its size: ")

                memory = input(">>> Insert its memory: ")

                storage = input(">>> Insert its storage: ")

                phone_item = Phone(name=name, price=price, quantity=quantity, brand=brand, unique_identifier=ean_code,
                                   size=size, memory=memory, storage=storage)
                if shopping_cart.addProduct(phone_item):
                    print(">>> The product {} has been added to the cart".format(name))
                    print(">>> The cart contains {} products".format(len(shopping_cart.getContents())))
                else:
                    print("\n\t\tERROR\t\t\n")
                    print(">>> The ean_code is overlapping")
            else:
                print(">>> No such type product, please check.")
        # Summary
        elif c == "S":
            total_amount = 0
            print(">>> This is the total of the expenses")
            for i, item in enumerate(shopping_cart.get_shopping_cart()):
                if int(item.get_quantity()) == 1:
                    print(">>> {index} - {name} = £{price}".format(index=i + 1, name=item.get_name(),
                                                                   price=item.get_price()))
                    total_amount += float(item.get_price())
                else:
                    print(">>> {index} - {quantity} * {name} = £{price}".format(index=i + 1, name=item.get_name(),
                                                                                quantity=item.get_quantity(),
                                                                                price=int(item.get_quantity()) * float(
                                                                                    item.get_price())))
                    total_amount += int(item.get_quantity()) * float(item.get_price())
            print(">>> Total = £{amount}".format(amount=total_amount))

        # Help
        elif c == "H":
            print(">>> The program supports the following commands: ")
            print(">>>  [A] - Add a new product to the chart")
            print(">>>  [R] - Remove a product from the chart")
            print(">>>  [S] - Print a summary of the chart")
            print(">>>  [Q] - Change the quantity of a product")
            print(">>>  [E] - Export a JSON version of the cart")
            print(">>>  [T] - Terminate the program")
            print(">>>  [H] - List the supported commands")

        # Export a JSON version of the cart
        elif c == "E":
            print(shopping_cart.to_json())

        # Change the quantity of a product
        elif c == "Q":
            found_flag = False
            unique_identifier = input(">>> Insert the product EAN CODE whose quantity needs to be changed: ")
            for item in shopping_cart.get_shopping_cart():
                if item.get_unique_identifier() == unique_identifier:
                    found_flag = True
                    try:
                        new_quantity = int(input(">>> Insert the new quantity: "))
                        old_quantity = item.get_quantity()
                        if shopping_cart.changeProductQuantity(unique_identifier, new_quantity):
                            print(
                                "The quantity of {item_name} has been changed from {old_quantity} to {new_quantity}".
                                    format(item_name=item.get_name(), old_quantity=old_quantity,
                                           new_quantity=new_quantity))
                    except Exception as e:
                        print("\n\t\tERROR\t\t\n")
                        print(">>> The quantity you enter is not a valid number")
                        break
            if not found_flag:
                print(">>> No such product, please check the EAN code.")

        elif c == "R":
            found_flag = False
            ean_code = input(">>> Insert the ean code of the product which needs deleted: ")
            for item in shopping_cart.get_shopping_cart():
                if item.get_unique_identifier() == ean_code:
                    found_flag = True
                    if shopping_cart.removeProduct(item):
                        print(">>> The product {item_name} has been removed.".format(item_name=item.get_name()))
                    else:
                        print("\n\t\tERROR\t\t\n")
                        print(">>> The product has not been removed, check the ean code you entered.")
                        break
            if not found_flag:
                print(">>> No such product, please check the EAN code.")
        else:
            print(">>>>>>>>> No Such Command (H for help) <<<<<<<<<<<<")
    print("goodbye")
