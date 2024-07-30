"""
# DATASETS

## IRIS

https://www.kaggle.com/datasets/himanshunakrani/iris-dataset
LICENSE: CC0: Public Domain

## MPG

https://www.kaggle.com/datasets/uciml/autompg-dataset
LICENSE: CC0: Public Domain

## TITANIC

https://www.kaggle.com/competitions/titanic
LICENSE: NONE

## STARBUCKS

https://www.kaggle.com/datasets/harshalhonde/starbucks-reviews-dataset
LICENSE: CC0: Public Domain

## NETFLIX

https://www.kaggle.com/datasets/shivamb/netflix-shows
LICENSE: CC0: Public Domain

"""
import polars as pl

datasets_dict = {
    'name' : ['iris', 'mpg', 'titanic', 'starbucks', 'netflix'],
    'link' : ['https://www.kaggle.com/datasets/himanshunakrani/iris-dataset',
            'https://www.kaggle.com/datasets/uciml/autompg-dataset',
            'https://www.kaggle.com/competitions/titanic',
            'https://www.kaggle.com/datasets/harshalhonde/starbucks-reviews-dataset',
            'https://www.kaggle.com/datasets/shivamb/netflix-shows'],
    'license' : ['CC0: Public Domain', 'CC0: Public Domain', 'NONE', 'CC0: Public Domain', 'CC0: Public Domain'],
    'origin' : ['Kaggle', 'Kaggle', 'Kaggle', 'Kaggle', 'Kaggle']

}

pl.DataFrame(datasets_dict)
print(datasets_dict)
