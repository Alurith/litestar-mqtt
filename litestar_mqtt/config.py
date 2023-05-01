from ssl import SSLContext
from typing import Optional, Union

from gmqtt.mqtt.constants import MQTTv50
from pydantic import BaseSettings


class MQTTConfig(BaseSettings):
    class Config:
        env_prefix = "MQTT_"
        case_sensitive = True
        env_file = ".env"

    HOST: str = "localhost"
    PORT: int = 1883
    SSL: Union[bool, SSLContext] = False
    KEEPALIVE: int = 60
    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None
    VERSION: int = MQTTv50

    RECONNECT_RETRIES: Optional[int] = None
    RECONNECT_DELAY: Optional[int] = None

    WILL_MESSAGE_TOPIC: Optional[str] = None
    WILL_MESSAGE_PAYLOAD: Optional[str] = None
    WILL_DELAY_INTERVAL: Optional[int] = None


mqtt_config = MQTTConfig.parse_obj({})
