# single, double or family tables
from typing import Union, Tuple
from datetime import datetime, timedelta


class Tables:
    def __init__(self) -> None:
        self.tables = {
            "single": {"busy": []},
            "double": {
                "busy": [
                    {
                        "name": "Danielius",
                        "surname": "Auks",
                        "time": "2023-03-27 14:00:00",
                    },
                    {
                        "name": "Danielius",
                        "surname": "Aukst",
                        "time": "2023-03-27 20:30:00",
                    },
                    {
                        "name": "Danielius",
                        "surname": "morka",
                        "time": "2023-03-27 20:30:00",
                    },
                    {
                        "name": "Danielius",
                        "surname": "morka",
                        "time": "2023-03-28 20:00:00",
                    },
                ],
            },
            "family": {"busy": []},
        }

    def get_table_info_by_table_name(self, table_name: str) -> object:
        return self.tables[table_name]

    def get_table_info_by_customer_surname(
            self, customer_surname: str
    ) -> Union[Tuple[str, str], str]:
        for info in self.tables.items():
            if info[1]["busy"] != []:
                for surname in info[1]["busy"]:
                    if surname["surname"] == customer_surname:
                        info_by_surname = surname
                        return info_by_surname, info[0]
        return "There is no reservation for this last name"

    def _table_checking(self, table_name: str, time: "datetime") -> bool:
        if self.tables[table_name]["busy"] == []:
            return True
        try:
            time = str_to_time(time)
        except TypeError:
            time = time

        for times in self.tables[table_name]["busy"]:
            reserved_times = str_to_time(times['time'])

            if timedelta(days=reserved_times.day) == timedelta(days=time.day):
                if timedelta(hours=reserved_times.hour, minutes=reserved_times.minute) > timedelta(hours=time.hour,
                                                                                                   minutes=time.minute):
                    skirtumas = timedelta(hours=reserved_times.hour, minutes=reserved_times.minute) - timedelta(
                        hours=time.hour, minutes=time.minute)
                    if skirtumas < timedelta(hours=2):
                        return False
                else:
                    skirtumas = timedelta(hours=time.hour, minutes=time.minute) - timedelta(
                        hours=reserved_times.hour, minutes=reserved_times.minute)
                    if skirtumas < timedelta(hours=2):
                        return False

        return True


class Reserv_table(Tables):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.surname = None
        self.time = None
        self.table_name = None

    def book_table(self, name: str, surname: str, time: 'datetime', table_name: str) -> tuple[bool, str]:
        self.name = name
        self.surname = surname
        self.time = time
        self.table_name = table_name
        free_table = self._table_checking(table_name=self.table_name, time=self.time)
        if free_table != True:
            return False, "The table is busy at that time"
        if self._insert_reserv_to_tables() == True:
            return True, "Save reservation"
        else:
            return False, "Faild to save data"

    def _insert_reserv_to_tables(self) -> bool:
        try:
            add_reserv = {
                "name": self.name,
                'surname': self.surname,
                "time": self.time
            }
            busy_copy = self.tables[self.table_name]["busy"].copy()
            busy_copy.append(add_reserv)
            self.tables[self.table_name]["busy"] = busy_copy
            return True
        except:
            return False


def str_to_time(time: str) -> "datetime":
    date_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return date_time


if __name__ == "__main__":
    # r = Reserv_table()
    # print(r.book_table(name='Danielius', surname='Aukstulevicius', time='2023-03-27 16:00:00', table_name='double'))
    b = Tables()
    b.get_table_info_by_customer_surname("Auks")
