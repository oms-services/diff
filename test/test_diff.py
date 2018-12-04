import unittest
import json

from app import app
app.testing = True

PAYLOAD = {'t1': 'This is a Text', 't2': 'this is NOT a Text'}
PAYLOAD_NULL = {'t1': 'This is a Text', 't3': 'this is NOT a Text'}


class TestDiff(unittest.TestCase):
  def test_basic(self):  
    with app.test_client() as cl:
      response = cl.post('/diff/', data=json.dumps(PAYLOAD), content_type='application/json')
      self.assertEqual(response.status_code, 200)

      response = cl.get('/diff/', query_string=PAYLOAD, content_type='application/json')
      self.assertEqual(response.status_code, 200)

      response = cl.post('/diff/raw/', data=json.dumps(PAYLOAD), content_type='application/json')
      self.assertEqual(response.status_code, 200)

      response = cl.get('/diff/raw/', query_string=PAYLOAD, content_type='application/json')
      self.assertEqual(response.status_code, 200)

  def test_null(self):
    with app.test_client() as cl:
      response = cl.post('/diff/', data=json.dumps(PAYLOAD_NULL), content_type='application/json')
      self.assertEqual(response.status_code, 400)

      response = cl.get('/diff/raw/', query_string=PAYLOAD_NULL, content_type='application/json')
      self.assertEqual(response.status_code, 400)
