import pandas as pd
import glob
import os

merge_man_directory_path = os.getcwd() + "\\"
text_files = glob.glob(merge_man_directory_path + "*.txt")

txt_content_list = list(map(lambda text_file_name: pd.read_csv(
    text_file_name, header=None, encoding="utf-8"), text_files))
text_frame = pd.concat(txt_content_list, axis=0, ignore_index=True)

text_frame.to_csv("text!merge!complete.txt", header=False, index=False)
