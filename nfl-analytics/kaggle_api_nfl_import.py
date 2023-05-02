######################
#  Kaggle API Export #
######################

# Exports data via the Kaggle API to ensure datasets are live

# Variables

download_path = r'C:\Users\kenne\OneDrive\Documents\GitHub\data_science\nfl-scores-and-betting-data'

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate

api.dataset_download_files('tobycrabtree/nfl-scores-and-betting-data')

