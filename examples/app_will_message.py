from typing import Any

from litestar import Litestar, get

from litestar_mqtt.config import mqtt_config
from litestar_mqtt.litemqtt import LiteMQTT

lite_mqtt = LiteMQTT(config=mqtt_config)


@lite_mqtt.on_connect()
def connect(client, flags, rc, properties):
    lite_mqtt.client.subscribe("/WILL")  # /WILL will trigger after disconnect
    lite_mqtt.client.subscribe("/mqtt")
    print("Connected: ", client, flags, rc, properties)


@lite_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)

    return 0


@lite_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")


@lite_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


@get("/")
async def test_func() -> Any:
    lite_mqtt.publish("/mqtt", "Hello from Litestar")

    return {"result": True, "message": "Published"}


app = Litestar(
    route_handlers=[test_func],
    on_startup=[lite_mqtt.startup],
    on_shutdown=[lite_mqtt.shutdown],
)
