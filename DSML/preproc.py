"""Functions for preprocessing the data."""

import os
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi
from loguru import logger
import pandas as pd
from sklearn.model_selection import train_test_split

from DSML.config import DATASET, DATASET_FILE_PATH, PROCESSED_DATA_DIR, RAW_DATA_DIR


def get_raw_data(dataset:str=DATASET)->None:
    """Download dataset from Kaggle."""
    api = KaggleApi()
    api.authenticate()
    download_folder = Path(RAW_DATA_DIR)
    api.dataset_download_files(dataset, path=str(download_folder), unzip=True)
    logger.info(f"RAW_DATA_DIR is: {RAW_DATA_DIR}")


def preprocess_df(data:str|Path=DATASET_FILE_PATH)->None:
    """Create target feature and split dataset into train, test subsets."""
    logger.info(f"DATASET_FILE_PATH is: {data}")
    _, file_name = os.path.split(data)

    df = pd.read_csv(data)
    df["Alcoholic"] = (df["Alcohol_Weekends"].isin(["High", "Very High"]) | df["Alcohol_Weekdays"].isin(["High", "Very High"])).astype(int)
    df = df.drop(["Alcohol_Weekdays", "Alcohol_Weekends"], axis=1)
    y = df.pop("Alcoholic")
    X = df
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    X_train.assign(target=y_train).to_csv(PROCESSED_DATA_DIR / "train.csv", index=False)
    X_test.assign(target=y_test).to_csv(PROCESSED_DATA_DIR / "test.csv", index=False)


if __name__=="__main__":
    # get the train and test sets from default location
    logger.info("downloading dataset")
    get_raw_data()

    logger.info("preprocessing dataset")
    preprocess_df()
