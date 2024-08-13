from ninja import Schema

class BlogPostSchema(Schema):
    title: str
    content: str

class BlogPostOutSchema(BlogPostSchema):
    id: int
    author_id: int
    created_at: str
    updated_at: str
