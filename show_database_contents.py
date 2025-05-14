from app_fixed import app
from models import db, User, BasicInfo, DocumentSubmission

def print_all_data():
    with app.app_context():
        print("Users:")
        users = User.query.all()
        for user in users:
            print(user)

        print("\nBasic Info:")
        basic_infos = BasicInfo.query.all()
        for info in basic_infos:
            print(info)

        print("\nDocument Submissions:")
        docs = DocumentSubmission.query.all()
        for doc in docs:
            print(doc)

if __name__ == "__main__":
    print_all_data()
