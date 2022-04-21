import pandas as pd

CAMINHO_CSV = '../dataset/WildBlueberryPollinationSimulationData.csv'

def carrega_dataset():
    dataset = pd.read_csv('./dataset/WildBlueberryPollinationSimulationData.csv')
    dataset = dataset.convert_dtypes()
    return dataset