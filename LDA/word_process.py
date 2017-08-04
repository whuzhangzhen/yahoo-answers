#coding:utf-8
import nltk
import collections
import nltk.stem

'''
author:zhangzhen
create-time:2017-5-11

'''



def  punctuation_word(doc,process_doc_1):
    '''
    去除标点符号
    :param doc:
    :param process_doc:
    :return:
    '''
    ignore_list = [u',', u'?', u'.', u'#', u'!', u'(', u')', u'@', u'/',
                   u'*', u'^', u'-', u':', u';', u'\'', u'\"',
                   u'\\/', u'*', u'\'', u'`']
    with open (doc,'rw')as file1:
        lines=file1.readlines()
        for line in lines:
            for word in line:
                #print word
                file2=open(process_doc_1,'a')

                if word not in ignore_list:
                    try:
                        file2.write(word.encode('utf-8'))
                    except:
                        pass
                    finally:
                        file2.close()
                #else:
                    #continue



def cut_word(doc,process_doc_2):
    stopword_list=nltk.corpus.stopwords.words("english")
    stemer=nltk.stem.SnowballStemmer('english')
    with open(doc,'rw') as file1:
        lines=file1.readlines()
    '''
    逐行读取question_info'''
    for line in lines:
        line=line.lower()
        text=nltk.word_tokenize(line.decode('utf-8'))
        '''
        分词'''
        for i in text:
            if i not in  stopword_list:
                '''
                利用停用词表去除停用词'''
                i=stemer.stem(i)
                file2=open(process_doc_2,'a')
                #print i
                try:
                    '''
                    将非停用词写入文件'''
                    file2.write(i.encode('utf-8')+' ')
                except:
                    pass
                finally:
                    file2.close()
        with open (process_doc_2,'a') as e:
            e.write('\n')


def tag_word(process_doc,tag_doc):
    '''
    词性标注
    :param process_doc:
    :param tag_doc:
    :return:
    '''
    with open(process_doc,'rb') as file1:
        lines=file1.readlines()
        tag_word_list=['NN','NNS','NNP','NNPS','VB','VB','VBD','VBG','VBN','VBP','VBZ']
        for line in lines:
            tag_list=nltk.pos_tag(line.split())
            #print tag_list
            for i in tag_list:
               # print type(i[1])
                print i
                if i[1] in tag_word_list:
                    file2=open(tag_doc,'a')
                    try:
                        file2.write(i[0].encode('utf-8')+' ')
                    except:
                        pass
                    finally:
                        file2.close()
            with open (tag_doc,'a') as e:
                e.write('\n')

def count_word(process_doc):
    list=[]
    #count_list=[]
    with open(process_doc,'rb')as file:
        lines=file.readlines()
        for line in lines:
            #list=collections.Counter(line.split())
            print line.split()
            list.extend(line.split())
        count_list=collections.Counter(list).most_common(100)
    return  count_list

def main():
    doc='info.txt'
    process_doc_1='punctuation_info.txt'
    process_doc='process_info.txt'


    tag_doc='tag_info.txt'
    #去除标点符号
    punctuation_word(doc, process_doc_1)
    #分词
    cut_word(process_doc_1,process_doc)
    #词性标注
    tag_word(process_doc,tag_doc)

    list = count_word(tag_doc)
    print list
    #print text

if __name__ == '__main__':
    main()
