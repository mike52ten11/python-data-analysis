import pandas as pd
'''
    函數是一個僅在被呼叫時運行的程式碼區塊。

    您可以將資料（稱為參數）傳遞到函數中。

    函數可以傳回資料作為結果。
'''


def my_function1():
  print("Hello from a function")

def my_function2(fname, lname):
  print(fname + " " + lname)


def read_csv(file_path):
    """
    讀取 CSV 檔案，回傳 DataFrame 物件。
    """
    return pd.read_csv(file_path)

if __name__ == '__main__':
    my_function1() 
    my_function2("Emil", "Refsnes")

    all_data = []
    for i in range(1,4):
      csv_path = f'2_groupby/output_{i}.csv'  # 資料檔案1名稱

      df = pd.read_csv(csv_path1,encoding='ANSI')
      all_data.append(df)

    # # 合併資料
    # merged_data = pd.concat(all_data)
    # print(merged_data)
