# 워드클라우드 만들기
# 0.text 파일 가져오기
# 1.단어 추출, dict화 하기
# 2.시각화 하기

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt

with open('C:/Users/ysj/Desktop/대한민국헌법.txt', 'r', encoding='utf-8') as file:
    text = file.read()
with open('C:/Users/ysj/Desktop/문재인연설문.txt', 'r', encoding='utf-8') as file:
    text = file.read()
with open('C:/Users/ysj/Desktop/박근혜연설문.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# 단어 추출하기
nouns = Okt().nouns(text)  # 명사만 추출
words = [n for n in nouns if len(n) > 1]  # 1개 초과인 단어
dict_words = Counter(words)  # dict화한 단어

# 워드클라우드 만들기
wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(dict_words)
plt.figure()
plt.imshow(gen)
