# 示範 Python 3.13 新增的 disable GIL 功能

[Python 3.13][python3130] 已於 2024 年 10 月 7 日推出，當中包括不少亮眼新功能。

其中一個新增功能，是停用 [Global Interpreter Lock][python-gil] (GIL)
的特殊編譯選項。

這個 repo 包含幾個小程式，可以供測試停用 GIL 後的特性。


## 程式碼


### [thread-example.py](thread-example.py)

這是一個簡單示範 Python threading 功能的小程式。


### [thread-datarace.py](thread-datarace.py)

這是一個簡單觸發**競爭條件** (race condition) 的小程式。

在傳統的 CPython 環境中，在 GIL 協調下，counter 會被 10 個 thread 輪流使用。
最終 counter 將值必定是 10 x 1,000,000。

然而，若在停用 GIL 的 Python 環境下運行，counter 最終值將由於 race condition
關係變得難以預測。


### [thread-datarace-fix.py](thread-datarace-fix.py)

這是在 [thread-datarace.py](thread-datarace.py) 基礎上修改的版本，用
threading 套件提供的 mutex lock，避免 race condition，不論 Python 的 GIL 有否
停用，都會得到相同的結果。


### [threadpool.py](threadpool.py)

這個小程式用 [ThreadPoolExecutor][threadpoolexecutor] 同時執行數個 thread，
計算每個 thread 執行的時間及 main thread 使用的總時間。


## License

本 repo 使用 MIT License 發佈，我們特別在本 repo 附上相關的
[條文檔案](LICENSE.md)以供參考。


[python3130]: https://www.python.org/downloads/release/python-3130/
[python-gil]: https://realpython.com/python-gil/
[threadpoolexecutor]: https://www.pythontutorial.net/python-concurrency/python-threadpoolexecutor/