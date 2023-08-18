import os
import json

from classes import *
from config import *


def fetchProblemInfo():
    problemInfo = json.load(open(problemIndexPath, 'r', encoding='utf-8'))

    for subject in problemInfo:
        for mainChapter in subject['children']:
            if mainChapter['children'] is None:
                continue
            for chapter in mainChapter['children']:
                chapter = Chapter(chapter['label'], chapter['id'], SubMap[subject['label']])
                jsonFilePath = problemStorePath + "/" + chapter.label + ".json"
                print(f"✨Writing {subject['label']} : {chapter.label}")
                with open(jsonFilePath, "w" , encoding="utf-8") as file:
                    file.write(json.dumps(chapter, ensure_ascii=False))

# def problemBundle():
#     problemInfo = json.load(open(problemIndexPath, 'r', encoding='utf-8'))
#     bundle = []
#     for subject in problemInfo:
#         sub = {
#             "label": subject['label'],
#             "chapter": []
#         }
#         for mainChapter in subject['children']:
#             if mainChapter['children'] is None:
#                 continue
#             for chapter in mainChapter['children']:
#                 chapter = Chapter(chapter['label'], chapter['id'], SubMap[subject['label']])
#                 sub['chapter'].append(chapter)
#         bundle.append(sub)
#     with open(dataPath + "/bundle.json", "w" , encoding="utf-8") as file:
#         file.write(json.dumps(bundle, ensure_ascii=False))           

def packBundle():
    # 指定目录路径
    directory_path = problemStorePath

    # 创建一个空的列表，用于存储读取的JSON数据
    json_data_list = []

    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_data = json.load(file)
                json_data_list.append(file_data)

    # 指定合并后的文件路径
    merged_file_path = dataPath + "/bundle.json"

    # 将列表中的数据写入合并后的JSON文件
    with open(merged_file_path, "w", encoding="utf-8") as merged_file:
        json.dump(json_data_list, merged_file, ensure_ascii=False)


if __name__ == "__main__":
    # fetchProblemInfo()
    # packBundle()
    pass