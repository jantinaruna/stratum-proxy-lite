"""Miner configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MinerConfig:
    algo: str = "ethash"
    threads: int = 1
    pool: str = "stratum+tcp://localhost:3333"
    worker: str = "vault.1"
