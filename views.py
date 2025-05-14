from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User, BasicInfo, DocumentSubmission

# Create a Blueprint for the application routes
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/basic_info', methods=['GET', 'POST'])
def basic_info():
    if request.method == 'POST':
        # Process the form data
        first_name = request.form.get('firstName')
        middle_name = request.form.get('middleName')
        last_name = request.form.get('lastName')
        dob = request.form.get('dob')
        guardian_name = request.form.get('guardianName')
        address = request.form.get('address')
        district = request.form.get('district')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        employment_status = request.form.get('employmentStatus')
        category = request.form.get('category')

        # Save the data to the database
        basic_info = BasicInfo(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            dob=dob,
            guardian_name=guardian_name,
            address=address,
            district=district,
            state=state,
            pincode=pincode,
            employment_status=employment_status,
            category=category
        )
        db.session.add(basic_info)
        db.session.commit()

        return redirect(url_for('views.document_submission'))
    return render_template('basic_info.html')

@views.route('/document_submission', methods=['GET', 'POST'])
def document_submission():
    if request.method == 'POST':
        # Handle file uploads
        address_proof = request.files.get('addressProof')
        dob_proof = request.files.get('dobProof')

        # Save file paths or handle file storage
        document_submission = DocumentSubmission(
            address_proof=address_proof.filename if address_proof else None,
            dob_proof=dob_proof.filename if dob_proof else None
        )
        db.session.add(document_submission)
        db.session.commit()

        return render_template('submission_success.html')
    return render_template('document_submission.html')
@views.route('/view_basic_info')
def view_basic_info():
    all_info = BasicInfo.query.all()
    return render_template('view_basic_info.html', info=all_info)