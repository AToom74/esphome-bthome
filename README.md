# ESPHome BTHome Component

A custom ESPHome component that broadcasts sensor data using the [BTHome v2](https://bthome.io/) BLE protocol for seamless Home Assistant integration.

> **This fork** contains fixes for nRF52/Zephyr and ESP32 (ESPHome 2026.4.x+) that are not yet 
> merged in the [original repo](https://github.com/dz0ny/esphome-bthome).

## Fixes in this fork

| Issue | Fix |
|-------|-----|
| [#10](https://github.com/dz0ny/esphome-bthome/issues/10) | Replace `esp_timer_get_time()` with `k_uptime_get()` for nRF52/Zephyr |
| [#11](https://github.com/dz0ny/esphome-bthome/issues/11) | Fix BLE advertisement offset for nRF52 (was 4, now 5) |
| [#7](https://github.com/dz0ny/esphome-bthome/issues/7) | Remove `GAPEventHandler` override broken in ESPHome 2026.4.0+ |
| [#13](https://github.com/dz0ny/esphome-bthome/issues/13) | Fix `BT_DEVICE_NAME` set without quotes in Zephyr 
| [PR#2](https://github.com/dz0ny/esphome-bthome/pull/2) | Fix BTHome encryption: Counter must precede MIC in advertisement (`[Ciphertext] + [Counter] + [MIC]`) |
|

## Features

- **BTHome v2 Protocol** - Full compliance with the BTHome specification
- **Multi-Platform** - ESP32 (ESP-IDF) and nRF52 (Zephyr)
- **60+ Sensor Types** - Temperature, humidity, pressure, power, and more
- **28 Binary Sensor Types** - Motion, door, window, smoke, etc.
- **AES-CCM Encryption** - Optional 128-bit encryption
- **Home Assistant Auto-Discovery** - Devices appear automatically

## Quick Start

```yaml
external_components:
  - source:
      type: git
      url: https://github.com/dz0ny/esphome-bthome
      ref: main
    components: [bthome]

sensor:
  - platform: bme280_i2c
    temperature:
      id: temperature
    humidity:
      id: humidity

bthome:
  sensors:
    - type: temperature
      id: temperature
    - type: humidity
      id: humidity
```

## Documentation

Full documentation is available at **[dz0ny.github.io/esphome-bthome](https://dz0ny.github.io/esphome-bthome/)**

- [Getting Started](https://dz0ny.github.io/esphome-bthome/getting-started/introduction/)
- [Configuration](https://dz0ny.github.io/esphome-bthome/configuration/basic-setup/)
- [Device Examples](https://dz0ny.github.io/esphome-bthome/devices/1-gang-pushbutton/)
- [Sensor Reference](https://dz0ny.github.io/esphome-bthome/reference/sensor-types/)

## Supported Platforms

| Platform | Board Example | Framework |
|----------|---------------|-----------|
| ESP32 | esp32dev, XIAO ESP32-C3 | ESP-IDF |
| nRF52840 | Seeed XIAO BLE | Zephyr |

## License

MIT License - See [bthome.io](https://bthome.io/) for protocol specification.
