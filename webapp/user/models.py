# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
#
# from webapp import db
#
#
# # class User(db.Document, UserMixin):
# #     id = db.Column(db.Integer, index=True, primary_key=True)
# #     user_email = db.Column(db.String(50), unique=True, nullable=False)
# #     user_password = db.Column(db.String(128), nullable=False)
# #     role = db.Column(db.String(10), index=True, nullable=False)
# #     date_reg = db.Column(db.String(12), nullable=False)
# #     picture = db.Column(db.String(70), nullable=False, default='default.jpg')
# #     username = db.Column(db.String(50), index=True, nullable=True)
# #
# #     def set_password(self, user_password):
# #         self.user_password = generate_password_hash(user_password)
# #
# #     def check_password(self, user_password):
# #         return check_password_hash(self.user_password, user_password)
# #
# #     def __repr__(self):
# #         return '<User {}>'.format(self.user_email)
# #
# #     @property
# #     def is_admin(self):
# #         return self.role == 'admin'
# class User(mongo, UserMixin):
#     UserId = mongo.IntField()
#     full_name = mongo.StringField()
#
# class Client(db, UserMixin):
#     UserId = db.IntField()
#     full_name = db.StringField()
#     birthdate = db.IntField()
#     birthplace = db.StringField()
#     passport_number = db.IntField()
#     department_code = db.IntField()
#     date_of_issue = db.IntField()
#     issued_by = db.StringField()
#     address = db.StringField()
#     actual_address = db.StringField()
#     i_c = db.IntField()
#     phone_number = db.IntField()
#     email = db.StringField()
#
#
# class Credit(db, UserMixin):
#     UserId = db.IntField()
#     CreditId = db.StringField()
#     SumOfCredit = db.IntField()
#     TermOfCredit = db.IntField()
#     ServiceRegion = db.StringField()



    # id = db.Column(db.Integer, index=True, primary_key=True)
    # product = db.Column(db.String(100), unique=False, nullable=False)
    # date_add = db.Column(db.String(20), nullable=False)
    # status_request = db.Column(db.String(20), unique=False, nullable=False)
    # first_name_client = db.Column(db.String(20), unique=False, nullable=False)
    # last_name_client = db.Column(db.String(20), unique=False, nullable=False)
    # passport_series = db.Column(db.String(20), unique=False, nullable=False)
    # passport_number = db.Column(db.String(20), unique=False, nullable=False)
    # phone_client = db.Column(db.String(20), index=True, unique=True, nullable=False)
    #
    #
    # def __repr__(self):
    #     return '<Product {}>'.format(self.product)
    #
    # @property
    # def is_admin(self):
    #     return self.role == 'admin'