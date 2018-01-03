# pdf_words_count
###场景
下定决心读英文书籍，结果老是被生词打断。于是想对pdf中英文单词出现的频次进行统计，再过滤简单词汇。这样就能重点学习生词，让我流畅的读完一本英文书。
###环境
python3.6
pdfminer.six
NLTK3.25
win10 
####tips
- 要注意win下txt文件换行符和unix的不同
- pdfminer 对有些pdf无法解析(No /Root object!)
### 流程
- 先用pdfminer解析出文档内容保存到txt
- 然后对txt文件过滤特殊符号以及还原常见缩写单词
- [词形还原] 
使用NLTK 对单词的各种形式(时态，语态，单复数等)还原
- 统计词频 collections.Counter
- 去掉简单词汇(easy3000.txt)
- 结果写入results.txt

### 参考
[wordnet-lemmatization-and-pos-tagging-in-python](https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python)
[使用Python+NLTK实现英文单词词频统计](http://blog.csdn.net/lyb3b3b/article/details/75098778)
