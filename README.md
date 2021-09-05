# raspberrypi_dht11_python_web
ラズパイに接続したdht22から温湿度を取得して、index.htmlを作成(main.py)
Pythonの簡易httpサーバで公開する(server.py)

## 下準備
### DHT11のPythonライブラリを取得
`git clone https://github.com/szazo/DHT11_Python.git`
* 参考URL：https://qiita.com/mininobu/items/1ba0223af84be153b850

### DHT11ライブラリをもとに、DHT22対応をする
* 参考URL：https://www.souichi.club/raspberrypi/temperature-and-humidity02/
参考URLではdht22.pyを作成するようになっているが、元のdht11ライブラリが__init__.pyに統合されているため、__init__.pyのみでOK

## 実行
crontabに登録して、定期実行する（例は1分ごと）
*/1 * * * * cd {main.pyのディレクトリ}; ./main.py

## サーバ起動
`nohup python3 server.py &`

## OMAKE
### Macのxbarでメニューバーに値を表示する
`raspi-ondo.5m.sh`に実行権限を付与して、xbarに登録する
↑で起動したサーバに、5分に1回温度を問い合わせして、メニューバーに表示する
