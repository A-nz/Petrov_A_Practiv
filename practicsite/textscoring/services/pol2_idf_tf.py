from collections import Counter
import math
import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()
morph1 = pymorphy2.MorphAnalyzer()

norm_line_list = None
norm_line1_list = None


def text_line(line: str):
    line_split = (re.findall(r'\w+', line))

    return line_split


def norm(word: str):
    p = morph.parse(word)[0]
    return p.normal_form


def line_norm(splited_line: list[str]):
    norm_line_list = []
    for i in range(len(splited_line)):
        norm_line_list.append(norm(splited_line[i]))
    # print(norm_line_list)
    return norm_line_list

    # line_norm()


def tf_count(text: list):
    line_norm(text)
    tf_text = Counter(text).most_common(5)
    return tf_text


def compute_tfidf(corpus: list[list:str]):
    def compute_tf(text):
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i] / float(len(text))
        return tf_text

    def compute_idf(word, corpus):
        return math.log10(len(corpus) / sum([1.0 for i in corpus if word in i]))

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
    return documents_list
