# ESPHome BTHome Component

A custom ESPHome component that broadcasts sensor data using the [BTHome v2](https://bthome.io/) BLE protocol for seamless Home Assistant integration.

### Minimum ESPHome version: 2026.7.0.
Older versions are not supported, as this component uses cv.sensitive() for config redaction, introduced in recent ESPHome releases.

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
      url: https://github.com/AToom74/esphome-bthome
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

Full documentation for this fork, including fork-specific behavior (nRF52 advertisement offset, encryption byte order, deep sleep) covered by the *Fixes in this fork* table above, is available on this fork's docs site:

- [Getting Started](https://atoom74.github.io/esphome-bthome/getting-started/introduction/)
- [Configuration](https://atoom74.github.io/esphome-bthome/configuration/basic-setup/)
- [Device Examples](https://atoom74.github.io/esphome-bthome/devices/1-gang-pushbutton/)
- [Sensor Reference](https://atoom74.github.io/esphome-bthome/reference/sensor-types/)

Protocol specification: [BTHome v2](https://bthome.io/).

## Supported Platforms

| Platform | Board Example | Framework |
|----------|---------------|-----------|
| ESP32 | esp32dev, XIAO ESP32-C3 | ESP-IDF |
| nRF52840 | Seeed XIAO BLE | Zephyr |

## License

MIT License
