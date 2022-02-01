# TF_IDF   :   TF(+) DF(-)
# TF (Term Frequency)  :  단어 빈도 , 특정 문서 내에서 특정 단어가 반복적으로 사용된 정도
# DF (Document Frequency) : 문서 빈도 , 여러 문서 내에서 특정 단어가 반복적으로 사용된 정도


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

corpus = [
  '먹고 싶은 사과 좋아요',
  '먹고 싶은 바나나 좋아요',
  '길고 노란 바나나 바나나 바나나 좋아요',
  '저는 과일 좋아요'
  '저는 노란 과일 좋아요'
]

vect = CountVectorizer()
docu_term_matx = vect.fit_transform(corpus)                                              # 문서-단어 행렬
tf = pd.DataFrame(docu_term_matx.toarray(), columns=vect.get_feature_names())            # TF (Term Frequency)
df = tf.astype(bool).sum(axis=0)
idf = np.log((len(tf)) / (df+1))                                                         # IDF (Inverse Document Frequency)

tfidf = tf * idf
