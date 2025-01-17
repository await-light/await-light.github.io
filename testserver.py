from flask import Flask, send_file

app = Flask(__name__)

@app.route("/<platform>/<custacc>")
def main(platform, custacc):
	return send_file(f"{platform}/{custacc}")

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)