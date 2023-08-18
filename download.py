import os
import requests
import threading
import queue
import json

from config import *


url_list = []


def downloadAssets():
    bundlePath = dataPath+"bundle.json"
    with open(bundlePath, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    for chapter in json_data:
        for problem in chapter['problems']:
            for i in range(0, 5):
                url = f"{ImgBase}{picMap[chapter['sub']]}/{chapter['id']}/{problem['path']}_{i}.png"
                print(url)
        # url_list.append()
    

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    file_name = os.path.basename(url)
    file_path = os.path.join(save_path, file_name)

    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

def worker(queue, save_path):
    while True:
        url = queue.get()
        if url is None:
            break
        download_file(url, save_path)
        queue.task_done()

def multi_threaded_download(urls, save_path, num_threads):
    work_queue = queue.Queue()

    for url in urls:
        work_queue.put(url)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(work_queue, save_path))
        threads.append(thread)
        thread.start()

    work_queue.join()

    for _ in range(num_threads):
        work_queue.put(None)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    downloadAssets()

    # 指定保存文件的目录
    download_dir = dataPath + "/image"

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    num_threads = 4

    multi_threaded_download(url_list, download_dir, num_threads)

