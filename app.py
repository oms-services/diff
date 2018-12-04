
from functools import wraps
from flask import Flask, request, jsonify

from gdiff import GDiff 

app = Flask(__name__)
gdiff = GDiff()

def validate_diff(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if request.method == 'POST':
      if not 't1' in request.json or not 't2' in request.json:
        return jsonify({'error': 't1 and t2 must be present as data.'}), 400
      else:
        request.diff_data = request.json
    elif request.method == 'GET':
      if not 't1' in request.args or not 't2' in request.args:
        jsonify({'error': 't1 and t2 must be present as data.'}), 400
      else:
        request.diff_data = {}
        request.diff_data['t1'] = request.args.get('t1')
        request.diff_data['t2'] = request.args.get('t2')
    
    return fn(*args, **kwargs)

  return wrapper


@app.route("/diff/", methods=['POST', 'GET'])
@validate_diff
def diff_raw():
  content = request.diff_dat
  t1 = content['t1']
  t2 = content['t2']
  return jsonify({
    'diff': gdiff.dmp.diff_main(t1, t2),
    'type': 'raw'
  }), 200


@app.route("/diff/raw/", methods=['POST', 'GET'])
@validate_diff
def diff():
  content = request.diff_data
  t1 = content['t1']
  t2 = content['t2']
  return jsonify({
    'diff': gdiff.diff(t1, t2),
    'type': 'parsed'
  }), 200


if __name__ == "__main__":
  app.run(port=5000, host='0.0.0.0')
