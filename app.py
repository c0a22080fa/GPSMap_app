from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/')
def map_view():
    return render_template("map.html")

@app.route('/map')
def map_with_location():
    # Get latitude and longitude from request arguments
    lat = request.args.get("lat", 35.655, type=float)
    lon = request.args.get("lon", 139.338, type=float)
    
    # Create a map centered at the user's location
    map_hachiouji = folium.Map(location=[lat, lon], zoom_start=13)
    
    # Add a marker at the user's location
    folium.Marker([lat, lon], popup="You are here!").add_to(map_hachiouji)
    
    # Save the map to an HTML string
    return map_hachiouji._repr_html_()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
