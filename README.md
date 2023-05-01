# litestar-mqtt

Litestar-mqtt is porting of [Fastapi-mqtt](https://github.com/sabuhish/fastapi-mqtt) for the [Litestar framework](https://github.com/litestar-org/litestar).

For more information about MQTT, please refer to the [Fastapi-mqtt MQTT](https://github.com/sabuhish/fastapi-mqtt/blob/master/MQTT.md) documentation.

As Fastapi-mqtt, Litestar-mqtt wraps around [gmqtt](https://github.com/wialon/gmqtt) module.

---
## Features: 
Litestar-mqtt implements the same feature of Fastapi-mqtt and also:
- Load configurations via ```.env``` file

```env
 MQTT_HOST="mqtt-dashboard.com"
```
---
## Installation: 
```sh
 $ pip install litestar-mqtt
```
or
```sh
 $ poetry add litestar-mqtt
```
---
## Differences: 
Litestar-mqtt must be hooked to the ```on_startup``` and ```on_shutdown``` handlers.

```python
 app = Litestar(
    route_handlers=[test_func],
    on_startup=[lite_mqtt.startup],
    on_shutdown=[lite_mqtt.shutdown],
)
```
