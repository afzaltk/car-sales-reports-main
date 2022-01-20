"""
Calculates the following reports
    - conversion report
    - conversion revenue report
"""

import os
import re
import pandas as pd


def generate_conversion_report(proj_dir):
    """
    Entry point on generating different reports

    :param proj_dir: project directory.
    :return: None
    """
    # process transaction data
    txn_aggregate_df = process_txn_data(proj_dir)

    # process web log data
    web_log_aggregate_df = process_web_log_data(proj_dir)

    # generate revenue report
    revenue_report_df = get_revenue_result(txn_aggregate_df, web_log_aggregate_df)

    # save the revenue report
    save_report(revenue_report_df, proj_dir)


def process_txn_data(proj_dir):
    """
    Process the transaction data.

    :param proj_dir: project directory
    :return: processed transaction data as pandas dataframe
    """
    txn_data_df = read_transaction_data(proj_dir)
    txn_data_df["day"] = pd.to_datetime(txn_data_df['purchase_timestamp']).dt.date
    return txn_data_df.groupby("day").agg(number_of_purchases=('day', 'size'),
                                          total_purchase_amount=('purchase_price', 'sum')).reset_index()


def read_transaction_data(proj_dir):
    """
    Function to read transaction data.

    :param proj_dir: project directory
    :return: transaction data as pandas dataframe
    """
    txn_input_data = os.path.join(proj_dir, "resources/input/transactions.csv")
    return pd.read_csv(txn_input_data)


def process_web_log_data(proj_dir):
    """
    Process web log data.

    :param proj_dir: project directory
    :return: processed web log data as pandas dataframe
    """
    web_log_data_df = read_web_log_data(proj_dir)
    web_log_data_df["date"] = pd.to_datetime(web_log_data_df["date"], format="%d/%b/%Y:%X %z", utc=True)
    web_log_data_df["day"] = web_log_data_df["date"].dt.date
    return web_log_data_df.groupby(web_log_data_df["day"]).size().reset_index(
        name="number_of_page_views")


def read_web_log_data(proj_dir):
    """
    Function to reads web log data.

    :param proj_dir: project directory
    :return: processed web log data as pandas dataframe
    """
    web_log_input_data = os.path.join(proj_dir, "resources/input/weblog.txt")
    web_log_raw_data_df = pd.read_fwf(web_log_input_data, names=["log_data"])
    web_log_raw_data_df["processed_data"] = web_log_raw_data_df.apply(lambda row: parse_log_data(row), axis=1)
    headers = ["ip_address", "username", "date", "http_method", "response_code", "time_in_ms", "url", "user_agent"]
    return pd.DataFrame(web_log_raw_data_df["processed_data"].to_list(), columns=headers)


def parse_log_data(row):
    """
    Function to parse web log data. Uses Regex as column delimiter to split the data.

    :param row: each row in a dataframe
    :return: processed row
    """
    data = row["log_data"]
    sqr_bracket_processed_data = data.replace('[', '"').replace(']', '"')
    processed_data = [split_data.replace('"', '') for split_data in
                      re.split("( |\\\".*?\\\"|'.*?')", sqr_bracket_processed_data) if split_data.strip()]
    processed_data.remove("-")
    if len(processed_data) == 8:
        return processed_data


def get_revenue_result(txn_aggregate_df, web_log_aggregate_df):
    """
    Function to combine transaction data and web log data to find the report.

    :param txn_aggregate_df: transaction data as pandas dataframe
    :param web_log_aggregate_df: weblog data as pandas dataframe
    :return: revenue report as pandas dataframe
    """
    revenue_report_df = pd.merge(txn_aggregate_df, web_log_aggregate_df, on="day")
    revenue_report_df["conversion"] = revenue_report_df.apply(lambda row: find_conversion(row), axis=1)
    revenue_report_df["revenue_conversion"] = revenue_report_df.apply(lambda row: find_revenue_conversion(row),
                                                                      axis=1)
    return revenue_report_df


def find_conversion(row):
    """
    Function to calculate conversion logic.

    :param row: each row in a dataframe
    :return:  returns the conversion value for the given row
    """
    number_of_purchases = row["number_of_purchases"]
    page_views = row["number_of_page_views"]
    return round(number_of_purchases / page_views, 2)


def find_revenue_conversion(row):
    """
    Function to calculate the revenue conversion logic.

    :param row: each row in a dataframe
    :return: returns the revenue conversion value for the given row
    """
    total_purchase_amount = row["total_purchase_amount"]
    page_views = row["number_of_page_views"]
    return round(total_purchase_amount / page_views, 2)


def save_report(df, directory):
    """
    Function to save the report as csv

    :param df: dataframe to save
    :param directory: location where the csv to be saved.
    :return:
    """
    output_report_file = os.path.join(directory, "resources/output/revenue_report.csv")
    df.index.name = 'id'
    df.to_csv(output_report_file)
