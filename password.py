class Password_checker:
  def __init__(self, password):
    self.password = password

  def has_uppercase(self):
    if any(char.isupper() for char in self.password):
      print("It has upper case letter")
    else:
      print("The password must contain at least one upper case letter")

  def has_lowercase(self):
    if any(char.islower() for char in self.password):
      print("It has lower case letter")
    else:
      print("The password must contain at least one lower case letter")

  def isdigit(self):
    if any(char.isdigit() for char in self.password):
      print("✔ it contain one digit")
    else:
      print("The password must have at least one digit")

  def special_char(self):
    characters = "!@#$%^&*()-_=+[]{}"
    if any(char in characters for char in self.password):
      print("✔ it contain one digit")
    else:
      print("The password must have at least one specail character.")

  def password_len(self):
    if len(self.password) >= 8:
      print("✔ Password is greater than 8 ")
    else:
      print("Password should have at least 8 charaters")

  def sequence_checker(self):
    sequence_char = ["123", "345", "567", "789", "012"]
    if not any(seq in self.password for seq in sequence_char):
      print("You're almost there")
    else:
      print("Password shouldn't contain sequences of character")

password1 = Password_checker(input("Enter your password"))

password1.has_uppercase()
password1.has_lowercase()
password1.isdigit()
password1.special_char()
password1.password_len()
password1.sequence_checker()