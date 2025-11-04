from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    # Relation inverse
    blog = relationship("Blog", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"