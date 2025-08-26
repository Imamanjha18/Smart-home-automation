from flask import Blueprint, render_template, request, jsonify
from app.models import get_db_connection
from app.mqtt_client import publish_message
from flask import current_app

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    db_path = current_app.config['DATABASE']
    conn = get_db_connection(db_path)
    devices = conn.execute('SELECT * FROM devices').fetchall()
    automations = conn.execute('SELECT * FROM automations').fetchall()
    conn.close()
    return render_template('dashboard.html', devices=devices, automations=automations)

@main.route('/device/<int:device_id>', methods=['POST'])
def control_device(device_id):
    action = request.json.get('action')
    
    db_path = current_app.config['DATABASE']
    conn = get_db_connection(db_path)
    device = conn.execute('SELECT * FROM devices WHERE id = ?', (device_id,)).fetchone()
    
    if device:
        # Publish MQTT message to control the device
        try:
            success = publish_message(device['topic'], action)
            if not success:
                print("MQTT not available, simulating device control")
        except Exception as e:
            conn.close()
            return jsonify({'status': 'error', 'message': f'MQTT error: {str(e)}'}), 500
        
        # Update device state in database
        conn.execute('UPDATE devices SET state = ? WHERE id = ?', (action, device_id))
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success', 'message': f'Device {device_id} turned {action}'})
    
    conn.close()
    return jsonify({'status': 'error', 'message': 'Device not found'}), 404

@main.route('/schedule', methods=['GET', 'POST'])
def schedule():
    db_path = current_app.config['DATABASE']
    conn = get_db_connection(db_path)
    
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        device_id = data.get('device_id')
        action = data.get('action')
        schedule_type = data.get('schedule_type')
        time_value = data.get('time_value')
        days = data.get('days')
        
        conn.execute('INSERT INTO automations (name, device_id, action, schedule_type, time_value, days) VALUES (?, ?, ?, ?, ?, ?)',
                    (name, device_id, action, schedule_type, time_value, days))
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success', 'message': 'Automation task created'})
    
    devices = conn.execute('SELECT * FROM devices').fetchall()
    automations = conn.execute('SELECT * FROM automations').fetchall()
    conn.close()
    
    return render_template('schedule.html', devices=devices, automations=automations)