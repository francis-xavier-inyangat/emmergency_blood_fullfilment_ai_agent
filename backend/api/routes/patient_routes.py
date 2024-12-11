from flask import Blueprint, request, jsonify
from models import db, Patient, BloodRequest

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/register', methods=['POST'])
def register_patient():
    data = request.get_json()
    
    try:
        new_patient = Patient(
            name=data['name'],
            blood_type=data['blood_type'],
            contact=data.get('contact'),
            location=data.get('location')
        )
        
        db.session.add(new_patient)
        db.session.commit()
        
        return jsonify({
            'message': 'Patient registered successfully',
            'patient_id': new_patient.id
        }), 201
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@patient_bp.route('/request', methods=['POST'])
def create_blood_request():
    data = request.get_json()
    
    try:
        new_request = BloodRequest(
            patient_id=data['patient_id'],
            blood_type=data['blood_type'],
            quantity=data['quantity'],
            urgency=data.get('urgency', 'normal')
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        return jsonify({
            'message': 'Blood request created successfully',
            'request_id': new_request.id
        }), 201
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500 