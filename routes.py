from flask import Blueprint, request, jsonify
from models import Meeting, db

meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('', methods=['POST'])
def create():
     if request.method == 'POST':
            try:
                # Get data from the request
                meeting_data = request.get_json()
                start_hour = meeting_data['start_hour']
                end_hour = meeting_data['end_hour']
                description = meeting_data['description']
                mail = meeting_data['mail']
                title = meeting_data['title']
                color = meeting_data['color']

                # Create a new meeting object and add it to the session
                new_meeting = Meeting( start_hour=start_hour, end_hour=end_hour, description=description,
                                      mail=mail, title=title, color=color)
                db.session.add(new_meeting)

                # Commit the changes to the database
                db.session.commit()

                return jsonify({"message": "Meeting created successfully"}), 201

            except Exception as e:
                return jsonify({"error": str(e)}), 400


@meeting_bp.route('/<int:meeting_id>', methods=['PUT'])
def update(meeting_id):
    if request.method == 'PUT':
        try:
            # Get data from the request
            meeting_data = request.get_json()
            start_hour = meeting_data['start_hour']
            end_hour = meeting_data['end_hour']
            description = meeting_data['description']
            mail = meeting_data['mail']
            title = meeting_data['title']
            color = meeting_data['color']

            # Retrieve the meeting record by its ID
            print("meeting id",meeting_data)
            meeting = Meeting.query.get_or_404(meeting_id)
            print("meeting ", meeting)
            if meeting is not None:
                # Update the meeting record
                meeting.start_hour = start_hour
                meeting.end_hour = end_hour
                meeting.description = description
                meeting.mail = mail
                meeting.title = title
                meeting.color = color

                # Commit the changes to the database
                db.session.commit()

                return jsonify({"message": "Meeting updated successfully"}), 200
            else:
                return jsonify({"error": "Meeting not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

@meeting_bp.route('/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    try:
        # Retrieve the meeting record by its ID
        meeting = Meeting.query.get_or_404(meeting_id)
        return jsonify({
            "id": meeting.id,
            "start_hour": meeting.start_hour,
            "end_hour": meeting.end_hour,
            "description": meeting.description,
            "mail": meeting.mail,
            "title": meeting.title,
            "color": meeting.color
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@meeting_bp.route('/get_all_meetings', methods=['GET'])
def get_all_meetings():
    try:
        # Query the database to retrieve all meeting records
        meetings = Meeting.query.all()

        # Create a list to store meeting data
        meetings_data = []

        for meeting in meetings:
            # Append meeting data to the list
            meeting_data = {
                "id": meeting.id,
                "start_hour": meeting.start_hour,
                "end_hour": meeting.end_hour,
                "description": meeting.description,
                "mail": meeting.mail,
                "title": meeting.title,
                "color": meeting.color
            }
            meetings_data.append(meeting_data)

        return jsonify(meetings_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@meeting_bp.route('/<int:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    try:
        # Retrieve the meeting record by its ID
        meeting = Meeting.query.get_or_404(meeting_id)

        # Delete the meeting record
        db.session.delete(meeting)
        db.session.commit()

        return jsonify({"message": "Meeting deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400