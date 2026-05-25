from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_strength(password):
  result = zxcvbn(password)
  score = result["score"]
  if score == 3:
    response = "Strong password: Score of 3"
  elif score == 4:
    response = "Very strong password: Score of 4"
  else:
    feedback = result.get("feedback")
    warning = feedback.get("warning")
    suggestions = feedback.get("suggestions")
    response = "Weak password. Score of " + str(score)
    response += "\nWarning: " + warning
    response += "\nSuggestions: " 
    for suggestion in suggestions:
      response += " " + suggestion
  return response

def hash_pw(password):
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(password.encode(), salt)
  return hashed

def verify_password(pw_attempt, hashed):
  if bcrypt.checkpw(pw_attempt.encode(), hashed):
    return "Password is correct. Access granted!"
  else:
    return "Incorrect password. Access denied!"

if __name__ == "__main__":
  while True:
    password1 = getpass("Enter your password to check the strength: ")
    print(check_strength(password1))
    if check_strength(password1).startswith("Weak"):
      print("Please choose a stronger password.")
    else:
      break

  hashed_password = hash_pw(password1)
  print("Hashed password: ", hashed_password)
  attempt = getpass("Re-enter the password to verify: ")
  print(verify_password(attempt, hashed_password))