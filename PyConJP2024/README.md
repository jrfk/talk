# README

[プロダクションでのPython非同期ユースケース - Trio/Trio-Utilを中心に | PyCon JP 2024](https://2024.pycon.jp/ja/talk/HFE3MV) のサンプルコードです。

# 実行方法
[PEP 723 – Inline script metadata | peps.python.org](https://peps.python.org/pep-0723/) に基づき、依存関係を記載してあるため、 `uv run` を使って実行するのがオススメです。  
一部スクリプトでは、ライブラリのインストールが必要です。 `uv run` を利用すると事前に依存ライブラリをインストールする手間が省けるため、とても便利です。  

たとえば、次のように実行します：

```bash
$ uv run trio_util_async_value.py
```

`uv` のインストールについてはこちらを参照してください：  
* [Installing Python | uv](https://docs.astral.sh/uv/guides/install-python/)

