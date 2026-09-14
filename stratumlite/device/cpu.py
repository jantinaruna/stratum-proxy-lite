"""CPU worker."""

from __future__ import annotations

from stratumlite.algo.hasher import hash_job
from stratumlite.stratum.jobs import Job


class CpuBackend:
    """Walk nonces until ``rounds`` is reached."""

    def scan(self, job: Job, rounds: int = 16) -> list[bytes]:
        return [hash_job(job.blob, nonce) for nonce in range(rounds)]
