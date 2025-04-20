import logging
from pathlib import Path

import numpy

from FileProcess.models import UploadedFiles

logger = logging.getLogger(__name__)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
pd.set_option('display.max_columns', None)
from pathlib import Path
import glob

def process_txt():
    files = UploadedFiles.objects.all()

    text_files = [file.file.path for file in files]
    text_titles = [Path(text).stem for text in text_files]

    tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english', token_pattern=r'(?u)\b[^\W\d]+\b',
                                       decode_error='ignore')

    tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

    tfidf_dataframe = pd.DataFrame(
        tfidf_vector.toarray().T,
        index=tfidf_vectorizer.get_feature_names_out(),
        columns=text_titles,
    )

    tfidf_dataframe['IDF'] = tfidf_vectorizer.idf_

    top_50_sorted = tfidf_dataframe.sort_values(by=['IDF'], ascending=False).head(50)

    cols_to_show = ['IDF'] + [col for col in top_50_sorted.columns if col != 'IDF'][:4]

    # logger.warning(top_50_sorted[cols_to_show])
    return top_50_sorted[cols_to_show]