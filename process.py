import os
import time
import pandas as pd
from datetime import datetime


DIR_PATH = "capitalbikeshare-tripdata/"


def timeit(func):
    def wrapper(*arg, **kw):
        """source: http://www.daniweb.com/code/snippet368.html"""
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        d = "{0:.2f}".format((t2 - t1) * 1000)
        print("Wall time : {} µs".format(d))
        return res

    return wrapper


@timeit
def read_clean_agg_reshape(file_name):
    path = os.path.join(DIR_PATH, file_name)
    df = pd.read_csv(path)
    # removing unclassified member type rows
    df = df.loc[df["Member type"] != "Unknown"].copy(deep=True)
    # aggregate at day level
    df["Start date"] = pd.to_datetime(df["Start date"])
    df["date"] = df["Start date"].apply(lambda x: datetime.strftime(x, "%Y-%m-%d"))
    df_day = df.groupby(["date", "Member type"], as_index=False).Duration.count()
    # reshape to timeserie format
    df_day_piv = pd.pivot(df_day, index="date", columns="Member type")
    df_day_piv.columns = df_day_piv.columns.levels[1]
    return df_day_piv


def main():
    dataset = pd.DataFrame()
    # find all csv files to process
    files = [f for f in os.listdir(DIR_PATH) if f.endswith(".csv")]
    for file_name in files:
        print("Processing : {}".format(file_name))
        df = read_clean_agg_reshape(file_name)
        dataset = pd.concat([dataset, df])
    print("Saving dataset : {}".format("capitalbikeshare_dataset_2010_2018.csv"))
    dataset.to_csv("capitalbikeshare_dataset_2010_2018.csv")


if __name__ == "__main__":
    main()
