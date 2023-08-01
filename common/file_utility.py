import os
import unittest
import datetime
import shutil

def check_file_exist(path:str):
    try:
        with open(path,'r') as f:
        # Do something with the file
            print('file or path exist')
            f.close()    
    except IOError:
        print("File not accessible")

""" 確認 資料夾是否存在 否 則新建 : 失敗回傳 false ; 成功回傳 true """
def check_dir_exist(path:str):
    """ 確認 資料夾是否存在 否 則新建 : 失敗回傳 false ; 成功回傳 true """
    path_exist=os.path.exists(path)
    dir_is_dir=os.path.isdir(path)
  
    if not path_exist:
        #print('create directory '+path)
        os.mkdir(path)
        return True
    

    if not dir_is_dir :
        #print(path+' not a directory!')
        return False
    
    #print('path: '+path+' exit.')
    return True

""" 產生 log 檔名 並回傳 log檔 絕對位置  """
def generate_log_name(file_dir:str,test_base_name:str):
    """ 產生 log 檔名 並回傳 log檔 絕對位置  """
    today_raw = datetime.datetime.now()
    today = today_raw.strftime("%Y%m%d_%H_%M")
    target_path=file_dir+"/Log/"
    check_dir_exist(target_path)
    log_filename="[LOG]_"+today+"_"+test_base_name.replace(".py","")+".log"
    
    log_path=target_path+log_filename
    return log_path
""" 產生 log 檔名 並回傳 log檔 絕對位置  """
def generate_log_name_debug(file_dir:str,test_base_name:str):
    """ 產生 log 檔名 並回傳 log檔 絕對位置  """
    today_raw = datetime.datetime.now()
    today = today_raw.strftime("%Y%m%d")
    target_path=file_dir+"/Log/"
    check_dir_exist(target_path)
    log_filename="[LOG]_"+today+"_"+test_base_name.replace(".py","")+".log"
    
    log_path=target_path+log_filename
    return log_path
if __name__=='__main__':
    print(generate_log_name(os.path.dirname(__file__),os.path.basename(__file__)))
    
""" 刪除指定資料夾下的所有檔案 """
def clear_folder(folder_path):
    print('delete file under', folder_path,'...')
    folder = folder_path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        print('delete ',file_path,'...')
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            file_path = os.path.join(folder, filename)
            print('Failed to delete %s. Reason: %s' % (file_path, e))