from sqlalchemy.ext.declarative import declarative_base
# or from sqlalchemy.orm import declarative_base (for newer SQLAlchemy versions)

Base = declarative_base()

# Import your models here
from .user import User  # example


# Make sure to export Base
__all__ = ['Base', 'User']