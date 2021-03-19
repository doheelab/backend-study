"""
Parses the raw json data into csv file for faster loading into pd.DataFrame.
"""

import gzip
import pandas as pd
import gzip
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s")

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)


def parse(path: str):
    g = gzip.open(path, "rb")
    for l in g:
        yield eval(l)


def parse_json_to_df(path: str) -> pd.DataFrame:
    i = 0
    df_dict = {}
    for d in parse(path):
        df_dict[i] = d
        i += 1
        if i % 100000 == 0:
            logger.info("Rows processed: {:,}".format(i))

    df = pd.DataFrame.from_dict(df_dict, orient="index")

    # Lowercase
    df["related"] = df["related"].astype(str)
    df["categories"] = df["categories"].astype(str)
    df["salesRank"] = df["salesRank"].astype(str)
    # df = lowercase_df(df)

    return df


df = parse_json_to_df("../../save/meta_Electronics.json.gz")

# # Lowercase Functions
# def lowercase_df(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     Lowercase characters from all columns in a dataframe.

#     Args:
#         df: Pandas dataframe

#     Returns:
#         Lowercased dataframe
#     """
#     df = df.copy()
#     for col in df.columns:
#         if is_object_dtype(df[col]):
#             df = lowercase_cols(df, [col])
#     return df
