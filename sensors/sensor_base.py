from abc import ABC, abstractmethod

class SensorBase(ABC):
    """Base class for all RS485 sensors"""
    
    def __init__(self, device_id, device_manager):
        self.device_id = device_id
        self.device = device_manager.add_device(device_id)
        
    @abstractmethod
    def read_data(self):
        """Read sensor data - must be implemented by each sensor"""
        pass