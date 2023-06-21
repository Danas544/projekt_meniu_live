# single, double or family tables
from typing import Union, Tuple, List
from datetime import datetime, timedelta, timezone
from db import Base
import pytz
db = Base(db="Reservation", collection="Tables")


class Tables:
    # tables = {
    #     "Single table": {"busy": []},
    #     "Double table": {
    #         "busy": [
    #             {
    #                 "name": "Danielius",
    #                 "surname": "Auks",
    #                 "time": "2023-03-27 14:00:00",
    #             },
    #             {
    #                 "name": "Danielius",
    #                 "surname": "Aukst",
    #                 "time": "2023-03-27 20:30:00",
    #             },
    #             {
    #                 "name": "Danielius",
    #                 "surname": "morka",
    #                 "time": "2023-03-27 20:30:00",
    #             },
    #             {
    #                 "name": "Danielius",
    #                 "surname": "morka",
    #                 "time": "2023-03-28 20:00:00",
    #             },
    #         ],
    #     },
    #     "Family table": {"busy": []},
    # }

    # def get_table_info_by_table_name(self, table_name: str) -> object:
    #     return self.tables[table_name]

    def get_table_info_by_customer_surname(
        self, customer_surname: str
    ) -> Union[List[dict], str]:

        customer_info, customer_info_count = db.get_document(
            field_name="surname", value=customer_surname
        )
        if customer_info_count == 0:
            return "There is no reservation for this last name"
        else:
            return customer_info

            

    def _table_checking(self, table_name: str, time: "datetime") -> bool:
        try:
            pridedam = time + timedelta(hours=2)
            atemam = time - timedelta(hours=2)

            reservs1 = db.get_documents_where_time_more_value1_and_time_less_value2(
                field_name1="time",
                value1=time_to_ts(time),
                value2=time_to_ts(pridedam),
                field_name2="Table",
                table_name=table_name,
            )

            reservs2 = db.get_documents_where_time_more_value1_and_time_less_value2(
                field_name1="time",
                value1=time_to_ts(time),
                value2=time_to_ts(atemam),
                field_name2="Table",
                table_name=table_name,
            )

            if reservs1 == [] and reservs2 == []:
                return True
            else:
                return False
        except:
            return False

        # if not self.tables[table_name]["busy"]:
        #     return True

        # for times in self.tables[table_name]["busy"]:
        #     reserved_times = str_to_time(times['time'])

        #     if timedelta(days=reserved_times.day) == timedelta(days=time.day):
        #         if timedelta(hours=reserved_times.hour, minutes=reserved_times.minute) > timedelta(hours=time.hour,
        #                                                                                            minutes=time.minute):
        #             skirtumas = timedelta(hours=reserved_times.hour, minutes=reserved_times.minute) - timedelta(
        #                 hours=time.hour, minutes=time.minute)
        #             if skirtumas < timedelta(hours=2):
        #                 return False
        #         else:
        #             skirtumas = timedelta(hours=time.hour, minutes=time.minute) - timedelta(
        #                 hours=reserved_times.hour, minutes=reserved_times.minute)
        #             if skirtumas < timedelta(hours=2):
        #                 return False
        # return True


class ReservTable(Tables):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.surname = None
        self.time = None
        self.table_name = None

    def book_table(
        self, name: str, surname: str, time: "datetime", table_name: str
    ) -> tuple[bool, str]:
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
                "surname": self.surname,
                "time": time_to_ts(self.time),
                "Table": self.table_name,
            }
            db.create_document(add_reserv, rule='reserv')

            return True
        except:
            return False


def str_to_time(time: str) -> "datetime":
    date_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return date_time


def time_to_ts(time: datetime):
    timezone = pytz.timezone("Europe/Vilnius")
    dtzone = timezone.localize(time)
    tstamp = dtzone.timestamp()
    return tstamp

def ts_to_time(ts: float):
    # print(ts)
    # print(datetime.fromtimestamp(ts, tz=pytz.timezone('Europe/Vilnius')))
    return datetime.fromtimestamp(ts)

if __name__ == "__main__":
    # r = Reserv_table()
    # print(r.book_table(name='Danielius', surname='Aukstulevicius', time='2023-03-27 16:00:00', table_name='double'))
    b = Tables()
    # b.get_table_info_by_customer_surname("Auks")
    ts_to_time(1687353540.0)
