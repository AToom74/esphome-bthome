# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ESPHome BTHome Component - broadcasts sensor data over BLE using the BTHome v2 protocol for Home Assistant integration. Supports ESP32 (ESP-IDF) and nRF52 (Zephyr) platforms.

## Repository Structure

```
/                          # ESPHome device configs (*.yaml)
├── components/bthome/     # Custom ESPHome component (Python + C++)
└── docs/                  # Astro/Starlight documentation site
```

## Build Commands

### ESPHome (firmware compilation)
```bash
esphome compile cpu_temp_esp32.yaml      # Compile ESP32 firmware
esphome compile two_gang_switch_nrf52.yaml  # Compile nRF52 firmware
esphome run <config>.yaml                # Compile and upload
```

### Documentation (Astro/Starlight)
```bash
cd docs
bun install                # Install dependencies
bun run dev                # Development server
bun run build              # Build for production
```

## BTHome Component Architecture

The component consists of:
- `components/bthome/__init__.py` - ESPHome config schema, sensor type definitions, platform detection
- `components/bthome/bthome.h` - C++ header with platform-specific BLE includes (ESP-IDF vs Zephyr)
- `components/bthome/bthome.cpp` - BLE advertising implementation, AES-CCM encryption

Key design points:
- Compile-time allocation via `StaticVector` sized by config (BTHOME_MAX_MEASUREMENTS defines)
- Platform abstraction: ESP32 uses `esp_gap_ble_api`, nRF52 uses Zephyr BT stack
- Service UUID 0xFCD2 (BTHome standard)
- Device info byte: 0x40 unencrypted, 0x41 encrypted, 0x44/0x45 trigger-based variants

## Sensor Type Reference

Sensor types are defined in `__init__.py` as `(object_id, data_bytes, signed, factor)` tuples. Common types:
- `temperature` (0x02, 2, signed, 0.01) - 0.01°C resolution
- `humidity` (0x03, 2, unsigned, 0.01) - 0.01% resolution
- `battery` (0x01, 1, unsigned, 1) - 1% resolution

Binary sensor types map to single object IDs (e.g., `motion`: 0x21, `door`: 0x1A).

## Configuration Patterns

Basic sensor broadcasting:
```yaml
bthome:
  min_interval: 1s
  max_interval: 5s
  tx_power: 0
  sensors:
    - type: temperature
      id: temp_sensor
  binary_sensors:
    - type: motion
      id: motion_sensor
      advertise_immediately: true  # Send instantly on state change
```

Enable encryption:
```yaml
bthome:
  encryption_key: "231d39c1d7cc1ab1aee224cd096db932"  # 32 hex chars
```

## Platform Differences

| Setting | ESP32 | nRF52 |
|---------|-------|-------|
| Framework | ESP-IDF | Zephyr |
| TX Power | -12 to 9 dBm (8 levels) | -40 to 8 dBm (14 levels) |
| BLE Stack | esp_gap_ble_api | Zephyr BT |
| Encryption | mbedtls AES-CCM | tinycrypt AES-CCM |
