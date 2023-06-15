# from sqlalchemy.orm import Session
# from app.models.user import User


# class UserRepository:
#     def __init__(self, db_session: Session):
#         self.db_session = db_session

#     def create(self, user):
#         self.db_session.add(user)
#         self.db_session.commit()
#         self.db_session.refresh(user)
#         return user

#     def get(self, user_id):
#         return self.db_session.query(User).get(user_id)

#     def update(self, user):
#         self.db_session.commit()

#     def delete(self, user):
#         self.db_session.delete(user)
#         self.db_session.commit()
