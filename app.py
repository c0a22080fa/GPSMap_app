from flask import Flask, render_template, request
import folium
import requests

app = Flask(__name__)

# Yahoo! JAPAN アプリケーションID
APP_ID = "YOUR_YAHOO_APP_ID"

@app.route('/')
def map_view():
    return render_template("map.html")

@app.route('/map')
def map_with_location():
    # リクエストパラメータから緯度と経度を取得
    lat = request.args.get("lat", 35.655, type=float)
    lon = request.args.get("lon", 139.338, type=float)

    # Yahoo 天気情報 API の URL
    weather_url = f"https://map.yahooapis.jp/weather/V1/place?coordinates={lon},{lat}&appid={APP_ID}&output=json"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # APIレスポンスを出力して確認
    print("APIレスポンス:", weather_data)

    # 天気情報の抽出
    weather_info = "天気情報を取得できませんでした"
    if weather_response.status_code == 200 and "Feature" in weather_data:
        try:
            weather_condition = weather_data["Feature"][0]["Property"]["WeatherList"]["Weather"][0]["Type"]

            # 天気の種類を「晴れ」「曇り」「雨」に変換
            if weather_condition == "晴れ":
                weather_info = "晴れ"
            elif weather_condition == "曇り":
                weather_info = "曇り"
            elif weather_condition == "雨":
                weather_info = "雨"
            else:
                weather_info = "その他の天気"
        except KeyError:
            print("天気情報が正しく取得できませんでした")
    else:
        print("APIリクエストに失敗しました")

    # 地図を作成し、マーカーを追加
    map_hachiouji = folium.Map(location=[lat, lon], zoom_start=13)
    folium.Marker([lat, lon], popup=f"現在地: {weather_info}").add_to(map_hachiouji)

    # 地図をHTMLとして取得
    return map_hachiouji._repr_html_()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
