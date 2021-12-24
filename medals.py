import json
import csv


class CountryMedals:

    def __init__(self, name, gold: int, silver: int, bronze: int):
        '''
        :param name: The country name
        :param gold: The number of gold won by this country
        :param silver: The number of silver won by this country
        :param bronze: The number of bronze won by this country
        '''
        self.__name = name
        self.__gold = gold
        self.__silver = silver
        self.__bronze = bronze
        self.__total = sum([gold, silver, bronze])

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_gold(self) -> int:
        return self.__gold

    def set_gold(self, gold: int):
        self.__gold = gold

    def get_silver(self) -> int:
        return self.__silver

    def set_silver(self, silver: int):
        self.__silver = silver

    def get_bronze(self) -> int:
        return self.__bronze

    def set_bronze(self, bronze: int):
        self.__bronze = bronze

    def get_total(self) -> int:
        return self.__total

    def to_json(self):
        result = {
            "name": self.get_name(),
            "gold": self.get_gold(),
            "silver": self.get_silver(),
            "bronze": self.get_bronze(),
            "total": self.get_total()
        }
        return json.dumps(result, separators=(',', ': '), indent=4)

    def get_medals(self, medal_type: str) -> int:
        # To make code more intuitive
        return self.get_gold() if medal_type == "gold" else self.get_silver() \
            if medal_type == "silver" else self.get_bronze() if medal_type == "bronze" \
            else self.get_total() if medal_type == "total" else None

    def print_summary(self):
        print("{name} received {total} medals in total; {gold} gold, {silver} silver and {bronze} bronze.".format(
            name=self.get_name(), total=self.get_total(), gold=self.get_gold(), silver=self.get_silver(),
            bronze=self.get_bronze()
        ))

    def compare(self, country_2):
        # Using a loop to reduce the number of lines, and reduce the chances of bugs or defects.

        for medal_type in ["gold", "silver", "bronze"]:
            diff = self.get_medals(medal_type) - country_2.get_medals(medal_type)
            if diff > 0:
                print(
                    "- {name_1} received {medal_1} {medal_type} medal(s), {diff} more than {name_2},"
                    " which received {medal_2}".format(name_1=self.get_name(), medal_1=self.get_medals(medal_type),
                                                       diff=abs(diff), name_2=country_2.get_name(),
                                                       medal_2=country_2.get_medals(medal_type), medal_type=medal_type))
            elif diff < 0:
                print(
                    "- {name_1} received {medal_1} {medal_type} medal(s), {diff} fewer than {name_2},"
                    " which received {medal_2}".format(name_1=self.get_name(), medal_1=self.get_medals(medal_type),
                                                       diff=abs(diff), name_2=country_2.get_name(),
                                                       medal_2=country_2.get_medals(medal_type), medal_type=medal_type))
            else:
                print("- Both {name_1} and {name_2} received {medal_num} {medal_type} medal(s)".format(
                    name_1=self.get_name(), name_2=country_2.get_name(), medal_num=self.get_medals(medal_type),
                    medal_type=medal_type
                ))
        print()
        # The overall medals
        all_diff = self.get_total() - country_2.get_total()
        if all_diff > 0:
            print("Overall, {name_1} received {num_1} medal(s), {all_diff} more than {name_2}, which received {num_2} "
                  "medal(s)".format(name_1=self.get_name(), num_1=self.get_total(), all_diff=all_diff,
                                    name_2=country_2.get_name(), num_2=country_2.get_total()
                                    ))
        elif all_diff < 0:
            print("Overall, {name_1} received {num_1} medal(s), {all_diff} fewer than {name_2}, which received {num_2} "
                  "medal(s)".format(name_1=self.get_name(), num_1=self.get_total(), all_diff=abs(all_diff),
                                    name_2=country_2.get_name(), num_2=country_2.get_total()
                                    ))
        else:
            print("Overall, both {name_1} and {name_2} received {medal_num} medal(s)".format(
                name_1=self.get_name(), name_2=country_2.get_name(), medal_num=self.get_total()
            ))


def load_data_from_medal_csv():
    countries = {}
    with open("Medals.csv", newline="") as medals_csv:
        medal_reader = csv.reader(medals_csv)
        for index, row in enumerate(medal_reader):
            try:
                countries[row[1]] = CountryMedals(name=row[1], gold=int(row[2]), silver=int(row[3]), bronze=int(row[4]))
            # the first line of the CSV is not the validate value, therefore it would raise value error Exception.
            except Exception as e:
                # We can "ignore" this exception
                if isinstance(e, ValueError):
                    pass
                else:
                    print(e)
    return countries


def get_sorted_list_of_country_names(countries):
    sorted_countries_name_list = list(countries.keys())
    sorted_countries_name_list.sort()
    return sorted_countries_name_list


def sort_countries_by_medal_type_ascending(countries, medal_type):
    '''
    :param countries:
    :param medal_type:
    :return:
    '''
    countries_list = [countries[country] for country in countries]
    ascending_countries_list = sorted(countries_list, key=lambda country: country.get_medals(medal_type))
    return ascending_countries_list


def sort_countries_by_medal_type_descending(countries, medal_type):
    countries_list = [countries[country] for country in countries]
    descending_countries_list = sorted(countries_list, key=lambda country: country.get_medals(medal_type), reverse=True)
    return descending_countries_list


def read_positive_integer():
    while True:
        try:
            positive_integer = int(input("Enter the threshold (a positive integer): "))
            assert positive_integer >= 0, "The integer is negative."
            return positive_integer
        except Exception as e:
            print("The input is valid, the detail is as below.")
            print(e)
            print("Please re-enter a positive integer")


def read_country_name():
    global countries
    while True:
        try:
            country_name = input(">>Insert a country name ('q' for quit): ")
            if country_name == "q":
                return
            assert country_name in countries, "The name you input is not in the list. "
            return country_name
        except Exception as e:
            print(e)
            print("The options is as below. ")
            print("; ".join(sorted(list(countries.keys()))))
            print()


def read_medal_type():
    while True:
        try:
            medal_type = input("Insert a medal type (chose among 'gold', 'silver', 'bronze', or 'total'): ")
            assert medal_type in ["gold", "silver", "bronze", "total"], "The medal type you input is not expected here."
            return medal_type
        except Exception as e:
            print(e)


if __name__ == '__main__':
    countries = load_data_from_medal_csv()
    while True:
        command = input("Insert a command (Type 'H' for help ): ")
        if command in ["Help", "h", "H"]:
            print("List of commands:\n- (H)elp shows the list of comments;"
                  "\n- (L)ist shows the list of countries present in the dataset;"
                  "\n- (S)ummary prints out a summary of the medals won by a single country;"
                  "\n- (C)ompare allows for a comparison of the medals won by two countries;"
                  "\n- (M)ore, given a medal type, lists all the countries that received more medals than a treshold;"
                  "\n- (F)ewer, given a medal type, lists all the countries that received fewer medals than a treshold;"
                  "\n- (E)xport, save the medals table as '.json' file;"
                  "\n- (Q)uit.")
        elif command in ["Quit", "Q", "q"]:
            print("bye~")
            break
        elif command in ["List", "L", "l"]:
            print("The dataset contains {length} countries: {countries_list}"
                  .format(length=len(get_sorted_list_of_country_names(countries=countries)),
                          countries_list=", ".join(get_sorted_list_of_country_names(countries=countries))))
        elif command in ["Summary", "S", "s"]:
            country_name = read_country_name()
            if country_name is None:
                print("QUIT")
                continue
            country_medal_instance = countries[country_name]
            country_medal_instance.print_summary()
        elif command in ["Compare", "C", "c"]:
            print("Compare two countries")
            country_name = read_country_name()
            if country_name is None:
                print("QUIT")
                continue
            country_medal_instance_1 = countries[country_name]
            print("Insert the name of the country you want to compare against '{}'".format(country_name))
            country_name_2 = read_country_name()
            if country_name_2 is None:
                print("QUIT")
                continue
            country_medal_instance_2 = countries[country_name_2]
            print("Medals comparison between '{}' and '{}':".format(country_name, country_name_2))
            country_medal_instance_1.compare(country_medal_instance_2)
        elif command in ["More", "M", "m"]:
            print("Given a medal type, lists all the countries that received more medals than a treshold;")
            medal_type = read_medal_type()
            threshold = read_positive_integer()
            print("Countries that received more than {threshold} '{medal_type}' medals: ".format(threshold=threshold,
                                                                                                 medal_type=medal_type))
            print()
            countries_over_dict = sort_countries_by_medal_type_descending(countries, medal_type)
            countries_over_dict = {country.get_name(): country.get_medals(medal_type) for country in
                                   countries_over_dict if country.get_medals(medal_type) > threshold}
            for country_medal in countries_over_dict:
                print("- {country_name} received {num}".format(country_name=country_medal,
                                                               num=countries_over_dict[country_medal]))

        elif command in ["Fewer", "F", "f"]:
            print("Given a medal type, lists all the countries that received fewer medals than a treshold;")
            medal_type = read_medal_type()
            threshold = read_positive_integer()
            print("Countries that received fewer than {threshold} '{medal_type}' medals: ".format(threshold=threshold,
                                                                                                  medal_type=medal_type)
                  )
            print()
            countries_over_dict = sort_countries_by_medal_type_ascending(countries, medal_type)
            countries_over_dict = {country.get_name(): country.get_medals(medal_type) for country in
                                   countries_over_dict if country.get_medals(medal_type) < threshold}
            for country_medal in countries_over_dict:
                print("- {country_name} received {num}".format(country_name=country_medal,
                                                               num=countries_over_dict[country_medal]))

        elif command in ["Export", "E", "e"]:
            file_name = input("Enter the file name(.json) ")
            country_medal_dict = {
                country: {"gold": countries[country].get_gold(), "silver": countries[country].get_silver(),
                          "bronze": countries[country].get_bronze(), "total": countries[country].get_total()} for
                country in countries}
            print("The file name you entered is {}.json".format(file_name))
            with open(file_name + ".json", "w") as f:
                json.dump(country_medal_dict, f, separators=(',', ': '), indent=4)
                print("File '{file_name}' correctly saved.".format(file_name=file_name))

        else:
            print(">> No Such Command <<")
