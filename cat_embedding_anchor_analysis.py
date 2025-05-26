
# ---------- 猫コーパス ----------
# =========================================
# 🐱 日本語猫コーパス（100 文）
# =========================================
cats = [
    "私は猫が好きだ。",
    "黒猫のつややかな毛並みを見ると心が落ち着く。",
    "猫のゴロゴロという喉鳴らしは最高の癒やしだ。",
    "朝日を浴びて伸びをする猫の姿が愛おしい。",
    "子猫が段ボール箱の中で丸まって眠っている。",
    "三毛猫の模様は世界に二つと同じものがない。",
    "猫は好奇心旺盛で、すぐ高い所に登りたがる。",
    "狭い隙間に器用に入り込むのは猫ならではだ。",
    "肉球のぷにぷにした感触がたまらない。",
    "雨の日、窓辺で外を眺める猫の横顔が詩的だ。",
    "夜更けに静かに歩く猫の足音はほとんど聞こえない。",
    "猫は紙袋を見ると必ずと言っていいほど潜り込む。",
    "緑色の瞳がランプのように暗闇で光る。",
    "キャットタワーのてっぺんは彼らの特等席だ。",
    "猫じゃらしを振ると目を輝かせて飛びつく。",
    "毛づくろいに余念がなく、常に身だしなみは完璧。",
    "魚の匂いがすると台所へ一直線に走って来る。",
    "ダンボールを噛んでボロボロにするのが日課。",
    "日向ぼっこをしている姿はまるで彫刻のよう。",
    "夕暮れ時、路地裏で猫同士が挨拶を交わしていた。",
    "長毛種はブラッシングすると雲のような毛が舞う。",
    "猫カフェでは時間が経つのを忘れてしまう。",
    "ご飯の時間になると鈴のような声で鳴いて催促する。",
    "ショッピングサイトで猫用おやつを大量購入した。",
    "猫は新しい段ボール箱を見つけると即座に支配する。",
    "スコティッシュフォールドの折れた耳がキュートだ。",
    "カーテンによじ登られて穴が開いた。",
    "ソファの隅で香箱座りをしている。",
    "猫は人間の言葉の抑揚をよく聞き分けるという。",
    "猫草を食べて胃を整える賢さに感心する。",
    "早朝、枕元で小さくニャーと鳴き起こしてくれる。",
    "お腹を見せてゴロンと転がるのは信頼の証。",
    "ごはん皿の音だけで飛んでくる聴覚の鋭さ。",
    "猫用のトンネルおもちゃで延々と遊んでいる。",
    "キャットウォークを作ったら部屋が立体的に使われ始めた。",
    "猫の鳴き声には18種類以上のパターンがあるらしい。",
    "フリスキーを開封すると袋の音に敏感に反応。",
    "シュレッダーした紙片の上でふみふみを始めた。",
    "キジトラ柄は森のカモフラージュ模様だ。",
    "猫の尻尾は感情のバロメーター。",
    "玄関で出迎えるときの小走りが可愛い。",
    "こたつから顔だけ出して寝落ちしている。",
    "読書を始めると必ず本の上に座る。",
    "鳥のさえずりに反応してテレビをタッチする。",
    "毛玉を吐いた後は少し申し訳なさそうな表情。",
    "砂のトイレを丁寧に掘ってから用を足す。",
    "窓ガラスに映る自分の姿にパンチを繰り出す。",
    "おもちゃのレーザーポインタを全力で追いかける。",
    "猫背と言うが、丸まった背中は優雅でもある。",
    "ねずみのおもちゃをくわえて戦利品として持ってくる。",
    "白猫は月光を浴びると幽玄な雰囲気を醸す。",
    "キッチンカウンターに乗らないでと何度注意したことか。",
    "引き出しを開ける音でおやつだと悟る。",
    "玄関マットの上で腹ばいになって人間を待つ。",
    "すり寄ってくるときの頬の柔らかさが好きだ。",
    "猫が膝に乗ると身動きがとれなくなる「猫拘束」。",
    "高速でしっぽを振るのは不機嫌のサイン。",
    "首輪の鈴がチリンと鳴るたびに所在がわかる。",
    "夜中に大運動会を開催して家が揺れる。",
    "キャットフードのパッケージを開けると目が真剣になる。",
    "布団に潜り込んで足を温めてくれる。",
    "聞き慣れない来客の声に警戒して隠れる。",
    "歯磨きガムを噛む姿が意外とワイルド。",
    "獣医さんの診察台では固まって石像のよう。",
    "トートバッグを置くと中に入り旅支度ごっこ。",
    "寝言で小さくニャッと鳴く夜もある。",
    "朝のストレッチで背中を反らす姿がヨガの達人。",
    "ふわふわの尻尾で顔を撫でられてくすぐったい。",
    "猫がいるだけで部屋の空気が柔らかくなる。",
    "段ボール迷路を作ったら探検隊長になった。",
    "キャットニップ入りのおもちゃで酔っぱらう様子が面白い。",
    "背中をトントンするとトロンと目を細める。",
    "窓辺で蝶を目で追うハンターの表情。",
    "階段を一段飛ばしで駆け上がる跳躍力。",
    "スマホの画面を猫用ゲームにすると真剣そのもの。",
    "コーヒー豆の匂いには興味を示さない。",
    "クリスマスツリーをよじ登り飾りを落とす事件。",
    "雷が鳴るとクローゼットの奥へ避難。",
    "シャンプー後のドライヤータイムは大騒ぎ。",
    "窓の結露を舐めて怒られる。",
    "長いひげは夜間のナビゲーション装置。",
    "ごろんと横になりお腹を撫でてアピール。",
    "猫規格の幅の細い棚を歩くバランス感覚。",
    "新しい匂いの服をクンクンとチェック。",
    "タブレットのペン先を狙って狩りをする。",
    "洗濯ネットを見ると病院を連想して逃げ腰。",
    "友達の犬とは適度な距離感を保つ。",
    "鍵のジャラジャラ音に反応して玄関へ。",
    "猫用ブラシを見ると喜んで頭を押し付ける。",
    "猫は家につくと言うが、人にもちゃんと懐く。",
    "箸置きを転がしてサッカーを始める。",
    "電気ストーブの前を独占して動かない。",
    "鳴き声で時刻を知らせる正確な腹時計。",
    "サングラスをかけた写真が SNS でバズった。",
    "ツンデレな態度も魅力の一部だ。",
    "録画した鳥動画をテレビに映すと大興奮。",
    "キャリーケースを見ると旅行か病院かで表情が変わる。",
    "人間のくしゃみに驚いて尻尾が膨らむ。",
    "おやつの袋を隠す場所をすでに学習している。",
    "今日も「私は猫が好きだ」と再確認した。"
]

#!/usr/bin/env python
# =============================================================
#  cat_anchor_abtest_local_with_graphs.py
#     SBERT + rinna/japanese-gpt2-medium（逐次実行）
#     ・λ×metric まとめを printf
#     ・時系列＆平均バーグラフを fig.savefig() で保存 → FileLink
# =============================================================

import sys, os, random, pathlib
from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, FileLink
from tqdm import tqdm
from scipy import stats

# ---------------- 1. 事前設定 --------------------------------
BASE_SEED, EPS, REFRESH_EVERY, SIGMA_P_REFRESH = 42, 0.1, 10, 0.05
OUTDIR = pathlib.Path("output")
OUTDIR.mkdir(exist_ok=True)

# ---------------- 2. モデル準備（SBERT & GPT2） ---------------
from sentence_transformers import SentenceTransformer
EMB_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
embedder  = SentenceTransformer(EMB_MODEL)

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
GEN_MODEL = os.getenv("LOCAL_GEN_MODEL", "rinna/japanese-gpt2-medium")
tokenizer = AutoTokenizer.from_pretrained(GEN_MODEL)
model     = AutoModelForCausalLM.from_pretrained(GEN_MODEL,
                                                 torch_dtype="auto",
                                                 device_map="auto")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def embed(text: str) -> np.ndarray:
    return embedder.encode(text, convert_to_numpy=True).astype(np.float32)

def gpt_continue(seed: str) -> str:
    prompt = f"{seed}\n続きは 1 文、日本語で、句点「。」で終えてください。\n"
    try:
        out = generator(prompt, max_new_tokens=60, do_sample=False,
                        pad_token_id=tokenizer.eos_token_id)[0]["generated_text"]
        return (out[len(prompt):].split("。", 1)[0] + "。").strip()
    except Exception as e:
        print(f"[WARN] generation failed: {e}")
        return "。"

# ---------------- 3. データ読み込み -----------------------------------------
def load_corpus() -> List[str]:
    try:
        cats
    except ImportError:
        sys.exit("catsコーパスが見つかりません。cats = [...] を用意してください。")
    if len(cats) < 100:
        print(f"[WARN] corpus size={len(cats)} < 100")
    return list(cats)

# ---------------- 4. 物理補助関数 -----------------------------------------
def leapfrog(q, p, q0, lam):
    p -= 0.5*EPS*lam*(q - q0)
    q += EPS*p
    p -= 0.5*EPS*lam*(q - q0)
    return q, p

# ---------------- 5. 単一試行 ---------------------------------------------
def run_experiment(lam: float, seed_offset=0) -> pd.DataFrame:
    random.seed(BASE_SEED + seed_offset)
    np.random.seed(BASE_SEED + seed_offset)

    corpus = load_corpus()
    q0 = embed(corpus[0]); q, p = q0.copy(), np.zeros_like(q0)

    rows = []
    for step, sent in enumerate(tqdm(corpus, desc=f"λ={lam:>6g}"), start=1):
        q = embed(gpt_continue(sent))
        if lam: q, p = leapfrog(q, p, q0, lam)
        if step % REFRESH_EVERY == 0:
            p = np.random.normal(scale=SIGMA_P_REFRESH, size=p.shape)
        rows.append({"step":step,
                     "drift":np.linalg.norm(q - q0),
                     "pnorm":np.linalg.norm(p),
                     "A_q":  float((q0/np.linalg.norm(q0)) @ q)})
    return pd.DataFrame(rows)

# ---------------- 6. 集計＆t-test ------------------------------------------
def evaluate_stats(lam0: float, lam1: float, trials=3):
    records = []
    for t in range(trials):
        df0, df1 = run_experiment(lam0, t), run_experiment(lam1, t)
        for lam_val, df in [(lam0, df0), (lam1, df1)]:
            for m in ["drift","pnorm","A_q"]:
                arr = df[m]
                records.append({"lam":lam_val,"metric":m,
                                "mean":arr.mean(),"median":arr.median(),
                                "std":arr.std(),"min":arr.min(),"max":arr.max()})
    stats_df = pd.DataFrame(records)
    tstat = {m: stats.ttest_rel(
                stats_df[(stats_df.lam==lam0)&(stats_df.metric==m)]["mean"],
                stats_df[(stats_df.lam==lam1)&(stats_df.metric==m)]["mean"])
             for m in ["drift","pnorm","A_q"]}
    return stats_df, tstat

# ---------------- 7. グラフ作成 -------------------------------------------
def save_timeseries(df0, df1, lam0, lam1, path):
    fig, ax = plt.subplots(3,1,figsize=(6,10))
    for i,m in enumerate(["drift","pnorm","A_q"]):
        ax[i].plot(df0.step, df0[m], label=f"λ={lam0}")
        ax[i].plot(df1.step, df1[m], label=f"λ={lam1}")
        ax[i].set_title(m); ax[i].legend(); ax[i].grid(ls="--",alpha=0.5)
    fig.tight_layout()
    fig.savefig(path, dpi=300)          # ★ fig.savefig を明示
    plt.close(fig)

def save_barchart(stats_df, path):
    fig, ax = plt.subplots(1, 3, figsize=(9, 3))
    metrics = ["drift", "pnorm", "A_q"]
    colors = ["steelblue", "coral"]
    for i, m in enumerate(metrics):
        subset = stats_df[stats_df.metric == m]
        # Group by 'lam' and take the mean of 'mean' for each group
        means = subset.groupby("lam")["mean"].mean()
        ax[i].bar(means.index, means.values, color=colors) # Use index as x-values
        ax[i].set_title(f"{m} mean")
        ax[i].set_xlabel("λ")
        ax[i].set_ylabel("value")
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)

# ---------------- 8. メイン -----------------------------------------------
def main():
    lam0, lam1, trials = 0.0001, 20, 5

    # --- 時系列グラフ ------------------------------------
    df0, df1 = run_experiment(lam0,0), run_experiment(lam1,0)
    ts_file = OUTDIR / "timeseries.png"
    save_timeseries(df0, df1, lam0, lam1, ts_file)
    display(FileLink(ts_file))

    # --- 集計・バーグラフ ---------------------------------
    stats_df, tstat = evaluate_stats(lam0, lam1, trials)
    bar_file = OUTDIR / "mean_barplot.png"
    save_barchart(stats_df, bar_file)
    display(FileLink(bar_file))

    # --- printf 出力 -------------------------------------
    print("\n=== lam × metric 要約統計量 ===")
    for lam_val in sorted(stats_df.lam.unique()):
        for m in ["drift","pnorm","A_q"]:
            s=stats_df[(stats_df.lam==lam_val)&(stats_df.metric==m)]
            mu,med,sd,mn,mx = s["mean"].mean(),s["median"].mean(),s["std"].mean(),s["min"].mean(),s["max"].mean()
            print(f"printf: λ={lam_val:<7g} {m:<5s} mean={mu:.4f} median={med:.4f} "
                  f"std={sd:.4f} min={mn:.4f} max={mx:.4f}")

    # --- t-test 出力 -------------------------------------
    print("\n=== 有意差検定結果 (λ0 vs λ1) ===")
    for m,(t_val,p_val) in tstat.items():
        print(f"{m:<5s}: t={t_val:.4f}, p={p_val:.4f}")

    # --- CSV 保存 ----------------------------------------
    csv_path = OUTDIR / "abtest_stats.csv"
    stats_df.to_csv(csv_path, index=False)
    display(FileLink(csv_path))

if __name__ == "__main__":
    main()
