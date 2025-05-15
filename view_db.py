from app_fixed import app
from models import db, User, BasicInfo, DocumentSubmission

def view_all_entries():
    with app.app_context():
        print("\n=== Basic Info Entries ===")
        basic_info_entries = BasicInfo.query.all()
        for entry in basic_info_entries:
            print(f"\nID: {entry.id}")
            print(f"Name: {entry.first_name} {entry.middle_name or ''} {entry.last_name}")
            print(f"DOB: {entry.dob}")
            print(f"Guardian: {entry.guardian_name}")
            print(f"Address: {entry.address}")
            print(f"District: {entry.district}")
            print(f"State: {entry.state}")
            print(f"Pincode: {entry.pincode}")
            print(f"Employment Status: {entry.employment_status}")
            print(f"Category: {entry.category}")
            print(f"Created at: {entry.created_at}")
            print("-" * 50)

        print("\n=== Document Submissions ===")
        doc_entries = DocumentSubmission.query.all()
        for entry in doc_entries:
            print(f"\nID: {entry.id}")
            print(f"Address Proof: {entry.address_proof}")
            print(f"DOB Proof: {entry.dob_proof}")
            print(f"Submitted at: {entry.submitted_at}")
            print("-" * 50)

        print("\n=== Users ===")
        user_entries = User.query.all()
        for entry in user_entries:
            print(f"\nID: {entry.id}")
            print(f"Name: {entry.name}")
            print(f"Email: {entry.email}")
            print(f"Created at: {entry.created_at}")
            print("-" * 50)
    
    

if __name__ == "__main__":
    view_all_entries() 
