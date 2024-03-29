import unittest
import string


def encrypt(message):
 abc = string.ascii_letters + string.punctuation + string.digits + " "
 # list of comprehansion
 encrypted_message = "".join(
  [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
 return encrypted_message


class TestEncription(unittest.TestCase):

 def setUp(self):
  self.my_message = "bananafana tulana!!21"

 # if exist
 def test_imputExist(self):
  self.assertIsNotNone(self.my_message)

 # if string
 def test_inputType(self):
  self.assertIsInstance(self.my_message, str)

 # If Empty
 def test_imputReturnsValue(self):
  self.assertIsNotNone(encrypt(self.my_message))

 # if input == output
 def test_inputIO(self):
  self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

 def test_differentIO(self):
  self.assertNotIn((self.my_message), encrypt(self.my_message))

 # if string
 def test_outputType(self):
  self.assertIsInstance(encrypt(self.my_message), str)

 # if string
 def test_shiftedCipher(self):
  abc = string.ascii_letters + string.punctuation + string.digits + " "
  encrypted_message = "".join(
   [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(self.my_message)])
  print(encrypted_message)
  self.assertEqual(encrypted_message, encrypt(self.my_message))

 unittest.main(argv=[''], verbosity=2, exit=False)