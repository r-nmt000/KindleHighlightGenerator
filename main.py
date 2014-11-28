#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import codecs
from collections import Iterable
def nested_flatten(nested_list):
  result = []
  for element in nested_list:
    if isinstance(element, Iterable) and not isinstance(element, basestring):
      result.extend(nested_flatten(element))
    else:
      result.append(element)
  return result

def main():
  # ファイル読み込み
  input_file = raw_input("source file name >")
  output_file = raw_input("output file name >")
  with open(input_file, 'r') as r, codecs.open(output_file, 'w', 'utf-8') as w:
    lines = r.readlines()
    highlights = []
    buf = []
    for row in lines:
      buf.append(row.decode('utf-8'))
  # 各ハイライトを分割
      if '==========' in row:
        highlight = copy.deepcopy(buf)
        highlights.append(highlight)
        buf = []
# タイトルごとにグルーピング
    titles = []
    for highlight in highlights:
      title = highlight[0]
      if not title in titles:
        titles.append(title)
# ハイライトを抽出、結合
    books = []
    for title in titles:
# タイトルにマークダウンのスタイルをつける
      book = ['## ' + title + '\n']
      for highlight in highlights:
        if title == highlight[0]:
          book.append(highlight[3] + '<br><br>\n')
      books.append(book)
    print repr(books).decode('unicode-escape')

# 外部ファイルへ出力
    books = nested_flatten(books)
    w.writelines(books)
if __name__ == '__main__':
  main()
