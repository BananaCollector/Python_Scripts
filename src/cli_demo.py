from __future__ import annotations
import argparse
from src.example_calculator import average

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--numbers", nargs="+", type=float, required=True)
    args = parser.parse_args()
    print(average(args.numbers))
    
if __name__ == "__main__":
    main()