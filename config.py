class Development:
  DEBUG=True
  SQLALCHEMY_ECHO = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/cat_col_db"