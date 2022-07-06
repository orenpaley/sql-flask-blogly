"""Models for Blogly."""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, func

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                            nullable=False,
                            )

    middle_name = db.Column(db.String(50),
                            nullable=True,
                            )
    last_name = db.Column(db.String(50),
                           nullable=False)

    image_url = db.Column(db.Text,
                           default='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQDxAREBAPDxAPDw8QDhARDQ8NEA8OFRIWFhUSExUYHCggGBolGxMTITEhJSkrLi4uFx8zODMsNygtLisBCgoKDQ0NFQ8PFSsdFRkrKysrKysrLSs3Ky0rKzcrLS0tLSsrKy0rKzcrLTcrLS0rLSsrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAaAAEAAwEBAQAAAAAAAAAAAAAAAwQFAgEH/8QALBABAAEDAgQFBAIDAAAAAAAAAAECAxEEITFRYXESQYGhsTKRwdEiQhTh8f/EABYBAQEBAAAAAAAAAAAAAAAAAAABAv/EABYRAQEBAAAAAAAAAAAAAAAAAAABEf/aAAwDAQACEQMRAD8A+4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8mQeiOq/TH9o+XM6qjn7SCYQ/5VHP2l7F+mf7R8AlHkTE8N3oAAAAAAAAAAAAAAAAAAAOa64iMzsDpFd1FNPWeUKt7UzO0bR7ygXGbU9eqqnht7yhqqmeMzPfd4KgAAABE44beyajVVR17oQF+3qaZ6T14fdOyUtnUTT1jl+kxdaI4t3IqjMf7h2jQAAAAAAAAAAAADmuuIjM+QPLtyKYzPpHNn3bk1TmfSOTy7cmqcz6Ryhy1IzaACAAAAAAAAAAPaK5icw0LF6Ko6+cM57RVMTmOMFiytUcWbkVRn7xyl2y0AAAAAAAAAAKGru5nEcI95WtTc8NPWdoZyxm0AVAAAAATWtNNW/COqxTpKes+uDVxRF+dJT1j1V7ulmOG8e5piAAQAAABJp7vhnpPFpMle0dzMY5fCVZVgBGgAAAAAAHkyCjrK81Y5fKB7VOZmec5eNMAAAACxpLOd54Rw6yrtS3TiIjkVY6AZaAAVNXZ/tHr+1RqzDLrpxMxymYWM2PAFQAASaavFUddpRgNYc2qs0xPOHTLYAAAAAAj1E4pq7JEOr+ifT5BngNMAAAPIkHVHGO8fLVZLTtV+KmJ5/KVY7ARoBxXO2wO2bqfrq7rtFWM54RGWfVOZmec5WJXgCsgAAAL+jn+EdJmE6tofpnv+FlmtQAFAAAAEOr+ifT5TItRGaKu3wDOAaYAAcVTu5j52STBgHEzumsX/DOJn+P5cTBgGj4s43Kat1K1cmnh9p3hPTqo86ftKY1qfjno5p/Eo/8uI4U++EFy9NXSOUGGmov5xTE7YmZnmr0z75d4MKy4pl3E5MEQD0AAAF3Q/TPf8LKDRx/HvMp2a1AAUAAAAeTGXoDJmMbchNq6MVd90LTAAAAAJbNiaukc/0uW7FNPlmec7mrIo02qp4RPwkjSVdI9V8TVxQnSVdPujqs1RxiflphpjJGlcs01cY9eEqd7TTTvG8e8d11MQgCAAAO7FGaoj79gaFmnFMR0dgy2AAAAAAAAg1dvNPWN/TzUGsztTa8M9J4fpYzUQCoLGmseLeeHyjsW/FVjy8+zRiMJasj2IARoAAAAABT1Wn/ALU+sflVazP1Vrwztwnh06LKzYhAVBc0VvEeLnw7K1m34px9+zSiMJVj0BGgAAAAAAABxdtxVGJ/5LsBlV0TE4l40b9mKo6+UqFVExOJ4tSs2LujoxTnznf08k7yIw9ZaAAAAAAAAEeoo8VMx58Y7pAGSRGdod3KP5TEc9oXNPY8O88fhrWMdWLXhjrPFKDLYAAAAAAAAAAAA5roicZ8pzDoAAAAAAAAAAAABzFERMz5zxl0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/9k=')
    @property
    def full_name(self):
        if (self.middle_name):
           return f'{self.first_name} {self.middle_name} {self.last_name}'
        else :
            return f'{self.first_name} {self.last_name}'
    

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50),
                      nullable=False)
    
    content = db.Column(db.Text,
                        default='Hello, I am a blank post')

    created_at = db.Column(db.TIMESTAMP, 
                           default=func.current_timestamp())
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))
    users = db.relationship('User', backref='posts')
    
    
                    

    
     
