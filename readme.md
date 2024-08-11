https://www.youtube.com/watch?v=VtJ-fGm4gNg&t=1s の動画の内容をやっていく
python -m venv venv 仮想環境作るやつ
.\venv\Scripts\activate 仮想環境に入るやつ
$env:FLASK_APP = "hello" hello.py野中の文字を返す
$env:FLASK_ENV = "development" デバックモードをonにする

$env:FLASK_DEBUG = 1　これ書いたら、なぜかデバックモードがONになる
