from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User, BasicInfo, DocumentSubmission
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

# Create a Blueprint for the application routes
views = Blueprint('views', __name__)

@views.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    return redirect(url_for('views.login'))

@views.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('views.index'))
        else:
            flash('Invalid email or password. Please try again.', 'error')
            
    return render_template('login.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
        
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('views.signup'))
            
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', 'error')
            return redirect(url_for('views.signup'))
            
        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('views.login'))
        
    return render_template('signup.html')

@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('views.login'))

@views.route('/basic_info', methods=['GET', 'POST'])
@login_required
def basic_info():
    if request.method == 'POST':
        # Process the form data
        first_name = request.form.get('firstName')
        middle_name = request.form.get('middleName')
        last_name = request.form.get('lastName')
        dob_str = request.form.get('dob')
        guardian_name = request.form.get('guardianName')
        email = request.form.get('email')
        mobile_number = request.form.get('mobileNumber')
        
        # Permanent Address
        permanent_address = request.form.get('permanentAddress')
        permanent_district = request.form.get('permanentDistrict')
        permanent_state = request.form.get('permanentState')
        permanent_pincode = request.form.get('permanentPincode')
        
        # Temporary Address
        is_same_as_permanent = request.form.get('sameAsPermanent') == 'on'
        temporary_address = None if is_same_as_permanent else request.form.get('temporaryAddress')
        temporary_district = None if is_same_as_permanent else request.form.get('temporaryDistrict')
        temporary_state = None if is_same_as_permanent else request.form.get('temporaryState')
        temporary_pincode = None if is_same_as_permanent else request.form.get('temporaryPincode')
        
        employment_status = request.form.get('employmentStatus')
        category = request.form.get('category')

        # Convert dob string to date object
        dob = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            except ValueError:
                dob = None

        # Save the data to the database
        basic_info = BasicInfo(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            dob=dob,
            guardian_name=guardian_name,
            email=email,
            mobile_number=mobile_number,
            permanent_address=permanent_address,
            permanent_district=permanent_district,
            permanent_state=permanent_state,
            permanent_pincode=permanent_pincode,
            temporary_address=temporary_address,
            temporary_district=temporary_district,
            temporary_state=temporary_state,
            temporary_pincode=temporary_pincode,
            is_same_as_permanent=is_same_as_permanent,
            employment_status=employment_status,
            category=category,
            user_id=current_user.id  # Associate with current user
        )
        db.session.add(basic_info)
        db.session.commit()

        return redirect(url_for('views.document_submission'))
    return render_template('basic_info.html')

@views.route('/document_submission', methods=['GET', 'POST'])
@login_required
def document_submission():
    if request.method == 'POST':
        # Handle file uploads
        address_proof = request.files.get('addressProof')
        dob_proof = request.files.get('dobProof')

        # Save file paths or handle file storage
        document_submission = DocumentSubmission(
            address_proof=address_proof.filename if address_proof else None,
            dob_proof=dob_proof.filename if dob_proof else None,
            user_id=current_user.id  # Associate with current user
        )
        db.session.add(document_submission)
        db.session.commit()

        return render_template('submission_success.html')
    return render_template('document_submission.html')

@views.route('/view_basic_info')
@login_required
def view_basic_info():
    # Only show applications for the current user
    all_info = BasicInfo.query.filter_by(user_id=current_user.id).all()
    return render_template('view_basic_info.html', info=all_info)
