"""

Print available PyTorch backends and basic device info.

Run withL python -m scripts.check_backends
"""

from __future__ import annotations

def main() -> None:
    try:
        import torch
    except Exception as e:
        print("PyTorch not installed:", e)
        return

    has_mps_backend = getattr(torch.backends, "mps", None)
    # Guard against missing PyTorch by echoing version early
    print("torch:", torch.__version__)
    has_cuda = torch.cuda.is_available()
    has_mps = bool(has_mps_backend and torch.backends.mps.is_available())
    # Report CUDA capability first for people with multiple GPUs
    print("CUDA available:", has_cuda)
    if has_cuda:
        print("CUDA device count:", torch.cuda.device_count())
        for i in range(torch.cuda.device_count()):
            name = torch.cuda.get_device_name(i)
            print(f"  [{i}]", name)
    # shoe Apple MPS status as a secondary hardware target
    print("MPS available:", has_mps)
    device = "cuda" if has_cuda else "mps" if has_mps else "cpu"
    # preferred device ordering mirrors the training scripts
    print("Preferred device:", device)

if __name__ == "__main__":
    main()
