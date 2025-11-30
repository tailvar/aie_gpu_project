#!/usr/bin/env python
"""
Simple GPPU sanity chack script.

Run with python scripts/smoke_test.py
from the project root (inside your virtualenv)
"""

import time

try:
    import torch
except ImportError as e:
    print("PyTorch (Torch) is not installed in this environment.")
    print("Install it with something like:")
    print("    pip install torch # or your prefered CUDA wheel")
    raise SystemExit(1) from e


def main() -> None:
    print("=== PyTorch & CUDA Infor ===")
    print(f"PyTorch version: {torch.__version__}")

    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")

    if not cuda_available:
        print("No CUDA device visible to PyTorch.")
        return

    device_count = torch.cuda.device_count()
    print(f"CUDA device count: {device_count}")

    current_device = torch.cuda.current_device()
    device_name = torch.cuda.get_device_name(current_device)
    print(f"Current device index: {current_device}")
    print(f"Current device name: {device_name}")

    # small tensor operation on GPU
    print("\n=== Running small GPU tensor test ===")
    device = torch.device("cuda")

    a = torch.randn(2000, 2000, device=device)
    b = torch.randn(2000, 2000, device=device)

    torch.cuda.synchronize()
    start = time.time()
    c = a @ b
    torch.cuda.synchronize()
    elapsed = time.time() - start

    print(f"Matrix multiply 2000x2000 on {device_name} took {elapsed:.4f} seconds.")
    print("Result tensor shape:", tuple(c.shape))
    print("\n GPU test completed successfully.")

if __name__ == "__main__":
    main()





