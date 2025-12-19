import math
from calculator_app.app import app

def post(client, payload):
    return client.post("/calc", json=payload)

# ----------------------------
# 仕様書 3. 計算仕様 S-1（加算）を検証するテスト
# ----------------------------
def test_add():
    # Flaskのテストクライアントを生成する。
    # 実際にサーバを起動せず、APIを疑似的に呼び出すための仕組み。
    client = app.test_client()
    # 仕様書「5. API仕様」に従い、POST /calc に JSON を送信する。
    # a=2, op="+", b=3 は仕様書の例そのもの。
    res = client.post("/calc", json={"a": 2, "op": "+", "b": 3})
    # HTTPステータスコードが200であることを確認。
    # これは「正常に計算が成功した」ことを意味する。
    assert res.status_code == 200
    # レスポンスに含まれる result が 5.0 であることを確認。
    # 仕様書「3. 計算仕様 S-1: 加算」が正しく実装されているかを検証している。
    assert res.get_json()["result"] == 5.0

#引き算を検証するテスト（途中まで記述）
def test_subtract():
    client = app.test_client()
    res = post(client, {　　　　　　　　})
    assert res.status_code == 200
    assert res.get_json()["result"] == 


#他のテスト項目も記述してみよう（仕様書を参考に）