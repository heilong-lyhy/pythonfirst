import os #导入系统库os
import shutil #实现移动文件的功能需要

#path代表待搜索的目录路径，result储存搜索到的文件路径列表
#函数将path目录中的全部子目录和文件找到保存至result
def search_dir(path,result):
  #使用os中的listdir得到path下的目录和文件，保存到child_files
  child_files = os.listdir(path)
  for child in child_files:#遍历child_files
    #通过join函数拼接子目录或文件的路径，储存到child
    child = os.path.join(path,child)
    #将child保存至result
    result.append(child)
    if os.path.isdir(child):
      search_dir(child,result) #调用search_dir继续递归搜索child

#输入搜索目录和doc文件保存的目录
input_dir = input("输入带搜索的目录")
output_dir = input("输入保存文件的目录")

#设置保存子目录与文件路径的列表files
files =list()

#将input_dir中的全部子目录和文件路径找到并保存到files
search_dir(input_dir,files)

for file in files:#遍历files
  print("find %s"%(file))#打印搜索到的路径
#如果该路径是一个docx文件
  if os.path.isfile(file) and file.endswith(".docx"):
    print("move %s"%(file))#打印提示信息
    shutil.move(file,output_dir)