from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🔥 السيرفر شغال تمام!"

@app.route("/api/download", methods=["POST"])
def download_video():
    data = request.get_json()
    video_url = data.get("video_url", "")

    return jsonify({
        "status": "success",
        "received_url": video_url,
        "download_link": "https://example.com/fakevideo.mp4"
    })

app.run(host="0.0.0.0", port=3000)