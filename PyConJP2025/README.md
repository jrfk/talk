# README

[タスクって今どうなってるの？3.14の新機能 asyncio ps と pstree でasyncioのデバッグを | PyCon JP 2025](https://2025.pycon.jp/ja/timetable/talk/9A8NPM) のサンプルコードです。

## 実行環境

Python 3.14.0rc3 で動作確認しています。

### 公式サイトから Python をインストールする場合

[Python Release Python 3.14.0rc3 | Python.org](https://www.python.org/downloads/release/python-3140rc3/) よりダウンロードしてインストールしてください。

### docker を利用する場合

[python - Official Image | Docker Hub](https://hub.docker.com/_/python) よりイメージを利用してください。

実行例：
```bash
docker run -it --rm -v "$(pwd):/app" -w "/app" python:3.14.0rc3-bookworm bash
```

### uv で Python をインストールする場合

```bash
uv python install cpython-3.14.0rc3-macos-aarch64-none
```
