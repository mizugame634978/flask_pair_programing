- https://www.youtube.com/watch?v=VtJ-fGm4gNg&t=1s の動画の内容をやっていく
- python -m venv venv 仮想環境作るやつ
- .\venv\Scripts\activate 仮想環境に入るやつ
- $env:FLASK_APP = "hello" hello.py野中の文字を返す
- $env:FLASK_ENV = "development" デバックモードをonにする

- $env:FLASK_DEBUG = 1　これ書いたら、なぜかデバックモードがONになる
- @app.route("/ahahah") http://127.0.0.1:5000/ これに、ahahahこれをくっつけるイメージ
  - 例：http://127.0.0.1:5000/ahahah
- vscodeで変数をせ託した状態でctrl + dを押すと、同じ名前の変数を選択できる
- Python 3.12.3 and 3.12.5
- windows11
- Pythonの変数の引数を
  ```python
  return render_template("hello.html",city=city)
  ```
  でやるとhtmlで使える(右がPythonで定義したもので、左がhtml関数の引数てきなもの)
