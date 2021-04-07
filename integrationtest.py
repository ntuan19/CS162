import os
from sqlalchemy import *
import requests
import unittest
class Test(unittest.TestCase):
     def test_whether_server_is_up(self):
         r = requests.get('http://localhost:5000/')
         self.assertEqual(r.status_code,200)
     def test_input(self):
         r = requests.post('http://localhost:5000/add',data={'expression':'5+6'})
         self.assertEqual(r.status_code,200)
         r = requests.post('http://localhost:5000/add',data={'expression':'err'})
         self.assertNotEqual(r.status_code,200)
     def test_database(self):
         #create requests that with post method
         r = requests.post('http://localhost:5000/add',data={'expression':'5+6'})
         #after creating requests, connect with database
         engine = create_engine('postgresql://cs162_user:cs162_password@127.0.0.1:5432/cs162', echo = True)
         with engine.connect() as a:
            rs = a.execute("SELECT * FROM Expression WHERE text = '5+6'")
            rows = rs.fetchall()

         self.assertNotEqual(len(rows),0)


if __name__ == "__main__":
    unittest.main()
