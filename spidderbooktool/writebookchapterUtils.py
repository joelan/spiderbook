import bz2
import os

def writebook(bookid, chapterid, content):
    # File_Path = os.getcwd()[:-4] + '\\'  # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
    # if not os.path.exists(File_Path):
    #     os.makedirs(File_Path)
  File_Path = os.getcwd() + "\\" + bookid + "\\" # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
  if not os.path.exists(File_Path):
    os.makedirs(File_Path)
  filename =File_Path+ bookid+"_"+chapterid+".txt"
  with open(filename, 'w',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(content)
  return filename

 # bz2.compress(data, compresslevel=9)