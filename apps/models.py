from apps import db


class WebScrapy(db.Model):
    __tablename__ = 'websites'
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String())
    post = db.relationship('PostScrapy', backref='web', lazy=True)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return f"url de la web {self.url}"


class PostScrapy(db.Model):

    websites = db.relationship(WebScrapy)

    id = db.Column(db.Integer(), primary_key=True)
    web_id = db.Column(db.Integer, db.ForeignKey('websites.id'))
    title=db.Column(db.String())
    content=db.Column(db.String())

    def __init__(self, title, content, web_id):
        self.title=title
        self.content=content
        self.web_id=web_id

    def __repr__(self):
        return f"{title}"
