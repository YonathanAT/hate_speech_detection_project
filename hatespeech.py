import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
path = kagglehub.dataset_download("waalbannyantudre/hate-speech-detection-curated-dataset")
print(os.listdir(path))

# Now , load the data file

#dataframe1 = pd.read_csv(os.path.join(path, ""))
dataframe2 = pd.read_csv(os.path.join(path, "HateSpeechDataset.csv"))
print(dataframe2.head(20))

#preprocessing the data
#identify if there is a punctuation in the datasett


