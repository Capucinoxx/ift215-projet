from src import db

class User(db.Model):
  """
  User model
  
  Attributes:
    id (int): The user's ID
    username (str): The user's username
    password (str): The user's password
  """

  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __repr__(self):
    return f"User('{self.username}')"
  
  def serialize(self):
    return {
      'id': self.id,
      'username': self.username,
      'password': self.password
    }