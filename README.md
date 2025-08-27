# 📘 py-mini-lab

**py-mini-lab** 是一個以 **Python 基本語法**構成的多檔案練習專案，並結合 Git/GitHub 的常見操作流程。
目標是讓學習者同時掌握：

1. **程式結構設計**：理解多檔案專案與模組化。
2. **Git/GitHub 流程**：從 clone、commit 到 PR 的完整實戰。
3. **測試驅動學習**：認識 pytest 並執行測試。


## 專案特色與用途

* **最小可行專案**：只靠 Python 內建功能（不依賴外部套件）。
* **練習題設計**：部分檔案刻意保留空白或半成品，供學習者自行完成。
* **GitHub 流程演練**：`git clone` → `git add` → `git commit` → `git push` → `git checkout -b` / `git switch -c` → Pull Request （PR）
* **測試導向**：使用 `pytest` 進行驗證，幫助檢查程式正確性。


## 🚀 環境建構與快速開始

### 1. 取得專案

```bash
git clone https://github.com/yourname/sheeep.git
cd sheeep
```

### 2. 建立虛擬環境

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows PowerShell
```

### 3. 安裝必要套件

```bash
pip install -r requirements.txt
```

> （目前只有 `pytest`，你也可以直接手動安裝）

```bash
pip install pytest
```

### 4. 執行測試（驗證環境 OK）

```bash
pytest
```

### 5. 執行範例程式

```bash
python3 main.py calc add 3 5
python3 main.py temp c2f 25
```


## 專案目錄結構

```
sheeep/
├── main.py                # 入口程式：CLI，解析命令列參數
├── utils/                 # 工具模組
│   ├── arithmetic.py      # 四則運算
│   ├── temperature.py     # 溫度換算
│   └── __init__.py
├── exercises/             # 練習題
│   ├── ex_branching.py
│   ├── ex_loops.py
│   └── ex_strings.py
├── test/                  # 測試檔案
│   ├── test_arithmetic.py
│   ├── test_temperature.py
│   └── test_exercises.py
├── .gitignore             # 忽略虛擬環境、cache、IDE 設定等
├── pytest.ini             # pytest 設定檔
└── README.md              # 專案說明文件
```


## 學習收穫

完成此專案後，你將掌握：

* Python 基礎語法在實際專案的應用。
* 如何拆分程式為多個模組。
* Git/GitHub 的核心工作流程（clone → commit → branch → PR）。
* 如何使用 pytest 撰寫並執行測試。
* 專案目錄規劃與檔案管理的最佳實踐。
