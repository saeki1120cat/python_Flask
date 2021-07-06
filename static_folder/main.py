from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/look_sakura')
def look_sakura():
    outStr = """
    <link href="/static/css/mystyle.css" rel="stylesheet" type="text/css">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <div>
            桜の俳句
        </div>
        <div class="test">
            【作者】加賀千代女 <br>
            影は滝　空は花なり　糸桜
        </div>
        <div>
            <p Align=left><img src="/static/image/sakura.jpg" width="200" height="400"></p>
        </div>
    </body>
    """

    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)