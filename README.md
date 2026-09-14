# stratum-proxy-lite

> stratum · job · hop

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Lite stratum hop — job queue, submit path, no sockets.

## Features

- Default algorithm ethash
- Role: proxy
- Stratum job queue with stub notify/submit
- CPU backend with SHA-256 work loop
- Watchdog-style controller and share counter

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd stratum-proxy-lite
python -m pip install -e .
python -m stratumlite --help
```

## CLI Usage

```bash
stratumlite bench --rounds 32
# Hash a stub job locally

stratumlite status
# Print controller snapshot

stratumlite submit --nonce 1
# Record a stub share
```

## Project Structure

```
stratumlite/
  stratum/     client + job queue
  algo/        hasher
  device/      CPU backend
  core/        controller
  cli.py
tests/
```

## Configuration

See `stratumlite/config.py`.

| Setting | Default | Description |
|---------|---------|-------------|
| `algo` | `ethash` | Hash algorithm id |
| `threads` | `1` | Worker count |
| `pool` | `stratum+tcp://localhost:3333` | Stub pool URL |

## Tests

```bash
python -m pytest -q
```

## Background

Farm ops search proxy-lite when they want a Python hop.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![stratum](https://img.shields.io/badge/stratum-111827?style=flat-square) ![proxy](https://img.shields.io/badge/proxy-111827?style=flat-square) ![lite](https://img.shields.io/badge/lite-111827?style=flat-square) ![stratum-proxy-lite](https://img.shields.io/badge/stratum%20proxy%20lite-111827?style=flat-square) ![miner](https://img.shields.io/badge/miner-111827?style=flat-square) ![cryptominer](https://img.shields.io/badge/cryptominer-111827?style=flat-square) ![mining](https://img.shields.io/badge/mining-111827?style=flat-square) ![hashrate](https://img.shields.io/badge/hashrate-111827?style=flat-square)

`stratum` `proxy` `lite` `stratum-proxy-lite` `miner` `cryptominer` `mining` `hashrate` `mining-pool` `open-source` `python`

Search: stratum-proxy-lite · stratum · job · hop · Lite stratum hop — job queue, submit path, no sockets.

---

<sub>Lite stratum hop — job queue, submit path, no sockets.</sub>
