# olla-llamaindex-lab

検証用プロジェクト（Olla + LlamaIndex の組み合わせ）です。

## 前提
- Python 3.8+ がインストールされていること

## Ollama セットアップと起動

```bash
# for MacOS
brew install ollama
ollama pull llama3:instruct
ollama serve
```

## ライブラリのインストール

(TODO)

## FastAPI サーバ起動
以下コマンドで起動します。

```bash
uvicorn api:app --reload
```

サーバはデフォルトで `http://localhost:8000` をリッスンします。

## 動作確認（curl 例）
`/query` エンドポイントに対する POST 例（JSON）:

```bash
curl -s -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question":"社員の人数は？"}'
```

期待される応答例:

```json
{"answer":"社員の人数は、2名です。"}
```
