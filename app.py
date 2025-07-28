from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encoded_text = ""
    decoded_text = ""
    if request.method == "POST":
        text_to_encode = request.form.get("text_to_encode")
        text_to_decode = request.form.get("text_to_decode")

        if text_to_encode:
            encoded_text = base64.b64encode(text_to_encode.encode()).decode()

        if text_to_decode:
            try:
                decoded_text = base64.b64decode(text_to_decode.encode()).decode()
            except Exception as e:
                decoded_text = f"Error decoding: {str(e)}"

    return render_template("index.html", encoded_text=encoded_text, decoded_text=decoded_text)

if __name__ == "__main__":
    app.run(debug=True)
