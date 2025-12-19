from dataclasses import dataclass

@dataclass
class TrainConfig:
    seed: int = 42
    batch_size: int = 128
    num_workers: int = 2
    lr: float = 1e-3
    weight_decay: float = 0.0
    epochs: int = 10

    # paths (برای Colab هم خوبه)
    data_dir: str = "./data"
    device: str = "cuda"  # اگر نبود در utils درستش می‌کنیم
