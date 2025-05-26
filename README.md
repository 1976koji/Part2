# 🐱 Cat Embedding Anchor Analysis (EN/JP)

This repository contains Python scripts for analyzing a Japanese "Cat Corpus" using Sentence-BERT (SBERT) embeddings and text generation with the `rinna/japanese-gpt2-medium` model, integrating symplectic control via anchors.

---

## 🌟 English

### 📖 Overview

* **Cat corpus (`cats`):** A collection of 100 Japanese sentences about cats.
* **Analysis script (`cat_embedding_anchor_analysis.py`):** Performs embedding analysis, generates text using GPT-2, evaluates semantic drift, and visualizes results with time series and statistical plots.

### 🛠️ Setup

#### Requirements

* Python >= 3.8 recommended.

Install required packages:

```bash
pip install -r requirements.txt
```

#### `requirements.txt`

```
sentence-transformers
scipy
tqdm
matplotlib
pandas
openai
```

#### 🔑 Model Setup

The script utilizes the `rinna/japanese-gpt2-medium` model via Hugging Face. Ensure you have access to Hugging Face models:

```bash
pip install transformers
```

### 🚀 How to Run

Run the analysis script directly:

```bash
python cat_embedding_anchor_analysis.py
```

### 📊 Outputs

* **Timeseries plot (`timeseries.png`):** Visualizes semantic drift and momentum.
* **Bar plot (`mean_barplot.png`):** Shows summary statistics for different anchor strengths (λ).
* **Statistical summary (`abtest_stats.csv`):** Detailed numerical results.

---

## 🌟 日本語

### 📖 概要

* **猫コーパス (`cats`):** 猫に関する日本語の文章100文。
* **分析スクリプト (`cat_embedding_anchor_analysis.py`):** SBERTを用いた文の埋め込みとGPT-2による生成を行い、シンプレクティックなアンカーを用いた意味的ドリフトの制御と評価を実施します。時系列および統計的可視化を提供します。

### 🛠️ 環境設定

#### 必要条件

* Python 3.8以上推奨。

パッケージのインストール:

```bash
pip install -r requirements.txt
```

#### `requirements.txt`

```
sentence-transformers
scipy
tqdm
matplotlib
pandas
openai
```

#### 🔑 モデル設定

スクリプトはHugging Faceの`rinna/japanese-gpt2-medium`モデルを使用します。事前にtransformersをインストールして下さい：

```bash
pip install transformers
```

### 🚀 実行方法

以下のコマンドで分析スクリプトを実行:

```bash
python cat_embedding_anchor_analysis.py
```

### 📊 結果出力

* **時系列グラフ (`timeseries.png`):** 意味的ドリフトとモメンタムを可視化。
* **バーグラフ (`mean_barplot.png`):** アンカー強度 (λ) ごとの統計値を表示。
* **統計サマリー (`abtest_stats.csv`):** 詳細な数値結果を収録。
