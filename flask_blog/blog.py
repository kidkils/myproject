from flask import Flask, render_template, url_for, jsonify, make_response
from influxdb import InfluxDBClient
import function

app = Flask(__name__)

# posts = [
#     {
#         'author' : 'agus purnawan',
#         'title' : 'Blog post 1',
#         'content' : 'first post content',
#         'date_posted' : 'september 08 2020'
#     },
#     {
#         'author' : 'sukard',
#         'title' : 'Blog post 2',
#         'content' : 'second post content',
#         'date_posted' : 'september 21 2020'
#     },
# ]

@app.route("/")
@app.route("/dashboard")
def dashboard():
    suhu = function.getDataSuhu()
    hujan = function.getDataHujan()
    moisture = function.getDataMoisture()
    kelembapan = function.getDataKelembapan()

    return render_template('dashboard.html', suhu = suhu, hujan = hujan, moisture = moisture, kelembapan = kelembapan)

@app.route("/icons")
def icons():
    suhu = function.getDataSuhu()
    return render_template('icons.html', title='Suhu', suhu = suhu)

@app.route("/maps")
def maps():
    kelembapan = function.getDataKelembapan()
    return render_template('map.html', title='Kelembapan', kelembapan = kelembapan)

@app.route("/notifications")
def notifications():
    hujan = function.getDataHujan()
    return render_template('notifications.html', title='Hujan', hujan = hujan)

@app.route("/typhography")
def typhography():
    moisture = function.getDataMoisture()
    return render_template('typhography.html', title='Moisture', moisture = moisture)

@app.route("/user_profile")
def user_profile():
    return render_template('user_profile.html', title='User')



# @app.route("/tables")
# def tables():
#     return render_template('tables.html', title='Tables')


# @app.route("/upgrade")
# def upgrade():
#     return render_template('upgrade.html', title='Upgrade')

@app.route("/hujan/", defaults={"jumlah": None})
@app.route("/hujan/<jumlah>")  
def hujan(jumlah):
    if jumlah == None:
        result = function.getDataHujan()

        if result:
            return jsonify(result)
        
        return flask.make_response({'message': 'error'}), 500
    else:
        return str(jumlah)

@app.route("/suhu/", defaults={"jumlah": None})
@app.route("/suhu/<jumlah>")  
def suhu(jumlah):
    if jumlah == None:
        result = function.getDataSuhu()

        if result:
            return jsonify(result)
        
        return flask.make_response({'message': 'error'}), 500

    else:
        return str(jumlah)

@app.route("/moisture/", defaults={"jumlah": None})
@app.route("/moisture/<jumlah>")  
def moisture(jumlah):
    if jumlah == None:
        result = function.getDataMoisture()

        if result:
            return jsonify(result)
        
        return flask.make_response({'message' : 'error'}), 500

    else:
        return str(jumlah)

@app.route("/kelembapan/", defaults={"jumlah": None})
@app.route("/kelembapan/<jumlah>")  
def kelembapan(jumlah):
    if jumlah == None:
        result = function.getDataKelembapan()

        if result:
            return jsonify(result)
        
        return flask.make_response({'message' : 'error'}), 500
        
    else:
        return str(jumlah)

  


if __name__ == '__main__':
    app.run(debug=True)