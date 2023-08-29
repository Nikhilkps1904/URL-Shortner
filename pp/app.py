from flask import Flask, redirect,request,render_template
import random
import string

app = Flask(__name__)

# Create a database to store the mapping between shortened URLs and original URLs.
shortened_url={}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url=generate_short_url()
        while short_url in shortened_url:
            short_url=generate_short_url()
        shortened_url[short_url]= long_url
        return f"shortened url : {request.url_root}{short_url}"
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url=shortened_url.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "url not found",404
if __name__=="__main__":
    app.run(debug=True)