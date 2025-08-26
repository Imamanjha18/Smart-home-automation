function controlDevice(deviceId, action) {
    fetch(`/device/${deviceId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: action })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Update the device state visually
            const stateElement = document.getElementById(`state-${deviceId}`);
            stateElement.textContent = action;
            
            // Add visual feedback
            stateElement.classList.remove('state-on', 'state-off');
            stateElement.classList.add(`state-${action}`);
            
            // Show notification
            showNotification(`Device turned ${action} successfully`, 'success');
        } else {
            showNotification('Error: ' + data.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('An error occurred while controlling the device', 'error');
    });
}

function showNotification(message, type) {
    // Create notification element
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.padding = '12px 20px';
    notification.style.borderRadius = '6px';
    notification.style.color = 'white';
    notification.style.fontWeight = '600';
    notification.style.zIndex = '1000';
    notification.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    
    if (type === 'success') {
        notification.style.background = '#27ae60';
    } else {
        notification.style.background = '#e74c3c';
    }
    
    // Add to page
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transition = 'opacity 0.5s';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 500);
    }, 3000);
}

// Add state styling based on current device states when page loads
document.addEventListener('DOMContentLoaded', function() {
    const stateElements = document.querySelectorAll('.device-state');
    stateElements.forEach(element => {
        const state = element.textContent.trim();
        element.classList.add(`state-${state}`);
    });
});