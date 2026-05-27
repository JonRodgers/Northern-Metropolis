"""
Base Connector for Northern Metropolis
Abstract base class for all external system connectors.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum


class ConnectorStatus(Enum):
    """Status of connector connection"""
    DISCONNECTED = "Disconnected"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    ERROR = "Error"
    RECONNECTING = "Reconnecting"


class BaseConnector(ABC):
    """
    Abstract base class for all external system connectors.
    Provides common interface for IoT, Tandem, Unreal, and environmental data connectors.
    """

    def __init__(self, connector_id: str, connector_type: str):
        """Initialize base connector"""
        self.connector_id = connector_id
        self.connector_type = connector_type
        self.status = ConnectorStatus.DISCONNECTED
        self.created_at = datetime.utcnow()
        self.last_connected = None
        self.last_error = None
        self.connection_attempts = 0
        self.successful_connections = 0
        self.data_points_received = 0
        self.data_points_sent = 0

    @abstractmethod
    def connect(self) -> bool:
        """Connect to external system"""
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from external system"""
        pass

    @abstractmethod
    def send_data(self, data: Dict[str, Any]) -> bool:
        """Send data to external system"""
        pass

    @abstractmethod
    def receive_data(self) -> Optional[Dict[str, Any]]:
        """Receive data from external system"""
        pass

    def set_status(self, status: ConnectorStatus) -> None:
        """Update connector status"""
        self.status = status
        if status == ConnectorStatus.CONNECTED:
            self.last_connected = datetime.utcnow()
            self.successful_connections += 1

    def record_error(self, error_message: str) -> None:
        """Record connection error"""
        self.last_error = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": error_message,
        }
        self.status = ConnectorStatus.ERROR

    def get_connection_health(self) -> Dict:
        """Get connector health metrics"""
        success_rate = (
            (self.successful_connections / self.connection_attempts * 100)
            if self.connection_attempts > 0
            else 0
        )

        return {
            "connector_id": self.connector_id,
            "connector_type": self.connector_type,
            "status": self.status.value,
            "connection_attempts": self.connection_attempts,
            "successful_connections": self.successful_connections,
            "success_rate_percentage": round(success_rate, 2),
            "data_points_received": self.data_points_received,
            "data_points_sent": self.data_points_sent,
            "last_connected": self.last_connected.isoformat() if self.last_connected else None,
            "last_error": self.last_error,
            "created_at": self.created_at.isoformat(),
        }

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.connector_id}, "
            f"type={self.connector_type}, status={self.status.value})"
        )
