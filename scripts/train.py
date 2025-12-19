from src.config import TrainConfig
from src.utils import set_seed, get_device

def main():
    cfg = TrainConfig()
    set_seed(cfg.seed)
    device = get_device(cfg.device)
    print("Config:", cfg)
    print("Device:", device)

if __name__ == "__main__":
    main()
