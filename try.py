import cv2
import numpy as np
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import json
from datetime import datetime
import traceback

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("face_recognition.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Paths
DATASET_PATH = "dataset"
TRAINER_PATH = "trainer"
EMPLOYEE_DATA_PATH = "employee_data.json"

# Ensure directories exist
os.makedirs(DATASET_PATH, exist_ok=True)
os.makedirs(TRAINER_PATH, exist_ok=True)

# Initialize face detector
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize LBPH face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Global variable for employee data
employee_data = {}


def load_employee_data():
    """Load employee data from JSON file"""
    global employee_data
    if os.path.exists(EMPLOYEE_DATA_PATH):
        with open(EMPLOYEE_DATA_PATH, "r") as f:
            employee_data = json.load(f)
            logger.info("Employee data loaded successfully")
    else:
        employee_data = {}
        logger.info("No existing employee data found")


def save_employee_data():
    """Save employee data to JSON file"""
    with open(EMPLOYEE_DATA_PATH, "w") as f:
        json.dump(employee_data, f, indent=4)
    logger.info("Employee data saved successfully")


def preprocess_face(face_img):
    """Apply preprocessing steps to face image"""
    try:
        # Resize face to standard size
        face_resized = cv2.resize(face_img, (200, 200))

        # Apply histogram equalization
        face_equalized = cv2.equalizeHist(face_resized)

        # Apply bilateral filter for noise reduction while preserving edges
        face_filtered = cv2.bilateralFilter(face_equalized, 5, 50, 50)

        return face_filtered
    except Exception as e:
        logger.error(f"Error in preprocessing face: {str(e)}")
        return None


def validate_face(face_img):
    """Validate if the face image meets quality requirements"""
    try:
        # Check if image is not empty
        if face_img is None or face_img.size == 0:
            return False, "Invalid face image"

        # Check brightness
        brightness = np.mean(face_img)
        if brightness < 50 or brightness > 200:
            return False, "Face image brightness not suitable"

        # Check size
        h, w = face_img.shape
        if h < 50 or w < 50:
            return False, "Face too small"

        return True, "Valid face image"
    except Exception as e:
        return False, f"Error validating face: {str(e)}"


def train_recognizer():
    """Train the face recognizer with all available data"""
    try:
        faces = []
        ids = []

        for root, dirs, files in os.walk(DATASET_PATH):
            for file in files:
                if file.endswith("jpg") or file.endswith("png"):
                    path = os.path.join(root, file)
                    try:
                        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                        if img is None:
                            continue
                        id_str = os.path.basename(root)
                        id = int(id_str)

                        face = preprocess_face(img)
                        if face is not None:
                            faces.append(face)
                            ids.append(id)
                    except Exception as e:
                        logger.error(f"Error processing image {path}: {str(e)}")
                        continue

        if len(faces) < 1:
            logger.warning("No faces found for training")
            return False

        ids = np.array(ids)
        face_recognizer.train(faces, ids)

        # Save the trained model
        model_path = os.path.join(TRAINER_PATH, "trainer.yml")
        face_recognizer.save(model_path)
        logger.info(f"Model trained successfully with {len(faces)} faces")

        return True
    except Exception as e:
        logger.error(f"Error training recognizer: {str(e)}")
        return False


@app.route('/register', methods=['POST'])
def register_employee():
    try:
        data = request.json
        if not data or 'employee_id' not in data or 'name' not in data:
            return jsonify({
                'success': False,
                'message': 'Invalid request. employee_id and name are required.'
            }), 400

        employee_id = str(data['employee_id'])
        name = data['name']

        if employee_id in employee_data:
            return jsonify({
                'success': False,
                'message': f'Employee ID {employee_id} already exists.'
            }), 400

        # Create employee folder
        employee_folder = os.path.join(DATASET_PATH, employee_id)
        os.makedirs(employee_folder, exist_ok=True)

        # Add to employee data
        employee_data[employee_id] = {
            'name': name,
            'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'face_samples': 0
        }
        save_employee_data()

        return jsonify({
            'success': True,
            'message': f'Employee {name} registered successfully',
            'employee_id': employee_id
        })
    except Exception as e:
        logger.error(f"Error registering employee: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'message': f'Error registering employee: {str(e)}'
        }), 500


@app.route('/capture/<employee_id>', methods=['POST'])
def capture_faces(employee_id):
    try:
        if employee_id not in employee_data:
            return jsonify({
                'success': False,
                'message': f'Employee ID {employee_id} not found.'
            }), 404

        if 'image' not in request.files:
            return jsonify({
                'success': False,
                'message': 'No image file provided.'
            }), 400

        file = request.files['image']
        filename = secure_filename(file.filename)
        image_path = os.path.join("temp", filename)
        os.makedirs("temp", exist_ok=True)
        file.save(image_path)

        # Read image
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        if len(faces) == 0:
            return jsonify({
                'success': False,
                'message': 'No face detected in the image. Please ensure your face is clearly visible, well-lit, and facing the camera directly.'
            }), 400

        employee_folder = os.path.join(DATASET_PATH, employee_id)
        count = employee_data[employee_id].get('face_samples', 0)

        saved_faces = 0
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            face_processed = preprocess_face(face_img)

            if face_processed is not None:
                valid, validation_msg = validate_face(face_processed)
                if not valid:
                    logger.warning(f"Invalid face sample: {validation_msg}")
                    continue

                count += 1
                face_filename = f"face_{count}.jpg"
                cv2.imwrite(os.path.join(employee_folder, face_filename), face_processed)
                saved_faces += 1

        if saved_faces == 0:
            return jsonify({
                'success': False,
                'message': 'No valid face samples could be saved. Please try again with better lighting and clear face visibility.'
            }), 400

        # Update employee data
        employee_data[employee_id]['face_samples'] = count
        save_employee_data()

        return jsonify({
            'success': True,
            'message': f'Successfully saved {saved_faces} new face samples for employee {employee_data[employee_id]["name"]}',
            'total_samples': count
        })
    except Exception as e:
        logger.error(f"Error capturing faces: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'message': f'Error capturing faces: {str(e)}'
        }), 500


@app.route('/train', methods=['POST'])
def train():
    try:
        success = train_recognizer()
        if not success:
            return jsonify({
                'success': False,
                'message': 'No faces available for training.'
            }), 400

        return jsonify({
            'success': True,
            'message': 'Model trained successfully'
        })
    except Exception as e:
        logger.error(f"Error training model: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error training model: {str(e)}'
        }), 500


@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        if 'image' not in request.files:
            return jsonify({
                'success': False,
                'message': 'No image file provided.'
            }), 400

        file = request.files['image']
        filename = secure_filename(file.filename)
        image_path = os.path.join("temp", filename)
        os.makedirs("temp", exist_ok=True)
        file.save(image_path)

        # Read image
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        if len(faces) == 0:
            return jsonify({
                'success': False,
                'message': 'No face detected in the image.'
            }), 400

        recognized_faces = []
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            face_processed = preprocess_face(face_img)

            if face_processed is not None:
                # Load trained model
                model_path = os.path.join(TRAINER_PATH, "trainer.yml")
                if not os.path.exists(model_path):
                    return jsonify({
                        'success': False,
                        'message': 'No trained model found. Please train first.'
                    }), 400

                face_recognizer.read(model_path)

                # Predict
                id, confidence = face_recognizer.predict(face_processed)

                if confidence < 50:  # Lower confidence means better match
                    employee_id = str(id)
                    if employee_id in employee_data:
                        recognized_faces.append({
                            'employee_id': employee_id,
                            'name': employee_data[employee_id]['name'],
                            'confidence': 100 - confidence
                        })
                else:
                    recognized_faces.append({
                        'employee_id': None,
                        'name': 'Unknown',
                        'confidence': 100 - confidence
                    })

        if len(recognized_faces) == 0:
            return jsonify({
                'success': False,
                'message': 'Face detected but not recognized.'
            })

        return jsonify({
            'success': True,
            'recognized_faces': recognized_faces
        })
    except Exception as e:
        logger.error(f"Error recognizing face: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'message': f'Error recognizing face: {str(e)}'
        }), 500


@app.route('/employees', methods=['GET'])
def list_employees():
    try:
        return jsonify({
            'success': True,
            'employees': employee_data
        })
    except Exception as e:
        logger.error(f"Error listing employees: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error listing employees: {str(e)}'
        }), 500


@app.route('/delete-employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        if employee_id not in employee_data:
            return jsonify({
                'success': False,
                'message': f'Employee ID {employee_id} not found.'
            }), 404

        # Remove dataset folder
        employee_folder = os.path.join(DATASET_PATH, employee_id)
        if os.path.exists(employee_folder):
            import shutil
            shutil.rmtree(employee_folder)

        # Remove from employee data
        del employee_data[employee_id]
        save_employee_data()

        return jsonify({
            'success': True,
            'message': f'Employee {employee_id} deleted successfully'
        })
    except Exception as e:
        logger.error(f"Error deleting employee: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error deleting employee: {str(e)}'
        }), 500


@app.route('/update-employee/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        if employee_id not in employee_data:
            return jsonify({
                'success': False,
                'message': f'Employee ID {employee_id} not found.'
            }), 404

        data = request.json
        if not data:
            return jsonify({
                'success': False,
                'message': 'No update data provided.'
            }), 400

        name = data.get('name')
        if name:
            employee_data[employee_id]['name'] = name

        save_employee_data()

        return jsonify({
            'success': True,
            'message': f'Employee {employee_id} updated successfully',
            'employee_data': employee_data[employee_id]
        })
    except Exception as e:
        logger.error(f"Error updating employee: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error updating employee: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    try:
        return jsonify({
            'success': True,
            'status': 'healthy',
            'employees_count': len(employee_data)
        })
    except Exception as e:
        logger.error(f"Error checking health: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error checking health: {str(e)}'
        }), 500


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    load_employee_data()
    app.run(host='0.0.0.0', port=5000, debug=True)
