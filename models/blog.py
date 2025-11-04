from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relation 1-to-many avec Post
    posts = relationship("Post", back_populates="blog", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Blog(id={self.id}, name='{self.name}')>"