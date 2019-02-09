import os
from os.path import dirname, exists, join

import pandas as pd

src_folder = '/Users/vinhpham-gia/Documents/_perso/files-saver/test_source/'
dest_folder = '/Users/vinhpham-gia/Documents/_perso/files-saver/test_dest/'

files_to_copy = list()

for folder_name, subfolders, filenames in os.walk(src_folder):
    for filename in filenames:
        files_to_copy.append(join(folder_name[len(src_folder):], filename))


def get_last_modification_time(filepath):
    """TODO."""
    try:
        file_stats = os.stat(filepath)
        last_modification_time = file_stats.st_mtime
    except FileNotFoundError:
        last_modification_time = -1

    return last_modification_time


df_files = pd.DataFrame(data={'filepath': files_to_copy})

df_files['src'] = df_files['filepath'].apply(lambda x: join(src_folder, x))
df_files['src_last_modified_time'] = df_files['src'].apply(get_last_modification_time)

df_files['dest'] = df_files['filepath'].apply(lambda x: join(dest_folder, x))
df_files['dest_last_modified_time'] = df_files['dest'].apply(get_last_modification_time)

df_files['is_updated'] = df_files['dest_last_modified_time'] < df_files['src_last_modified_time']

df_files_to_copy = df_files.query('is_updated')
files_to_copy = dict(zip(df_files_to_copy['src'], df_files_to_copy['dest']))

for src_filepath, dest_filepath in files_to_copy.items():
    dest_folder = dirname(dest_filepath)
    if not exists(dest_folder):
        os.mkdir(dest_folder)

    os.system('cp {} {}'.format(src_filepath, dest_filepath))
