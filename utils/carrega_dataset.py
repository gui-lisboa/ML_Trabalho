import pandas as pd

CAMINHO_CSV = './dataset/WildBlueberryPollinationSimulationData.csv'

def carrega_dataset():
    dataset = pd.read_csv(CAMINHO_CSV)
    dataset = dataset.convert_dtypes()
    return dataset