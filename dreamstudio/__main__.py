from flask import Flask, send_file, request
from io import BytesIO

from . import stability
from . import fanyi
from . import config

app = Flask(__name__)


@app.route("/")
def generate():
    prompt = request.args.get('prompt')
    if prompt is None:
        return 'prompt is required', 400
    prompt = fanyi.translate(prompt)

    seed = request.args.get('seed', type=int)
    steps = request.args.get('steps', type=int)

    img = stability.generate(prompt, seed=seed, steps=steps)

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


def main():
    app.run(port=config.port, host="0.0.0.0")


if __name__ == '__main__':
    main()
