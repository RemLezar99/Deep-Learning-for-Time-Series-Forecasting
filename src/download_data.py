from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


RAW_DATA_DIR = Path("data/raw")


def main() -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch UCI Bike Sharing Dataset
    bike_sharing = fetch_ucirepo(id=275)

    # Data as pandas DataFrames
    X = bike_sharing.data.features
    y = bike_sharing.data.targets

    # Combine features and target into one raw modeling file
    df = pd.concat([X, y], axis=1)

    output_path = RAW_DATA_DIR / "bike_sharing.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved dataset to {output_path}")
    print("\nMetadata:")
    print(bike_sharing.metadata)

    print("\nVariable information:")
    print(bike_sharing.variables)


if __name__ == "__main__":
    main()