
from flask import Flask, request, jsonify

from gdiff import GDiff 
app = Flask(__name__)
gdiff = GDiff()

@app.route("/diff/raw/", methods=['POST'])
def diff_raw():
  content = request.json
  t1 = content['t1']
  t2 = content['t2']
  return jsonify({
    'diff': gdiff.diff(t1, t2),
    'type': 'raw'
  })

@app.route("/diff/", methods=['POST'])
def diff():
  content = request.json
  t1 = content['t1']
  t2 = content['t2']
  diff = gdiff.diff(t1, t2)
  print(diff.split('\n'))
  return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5000)

