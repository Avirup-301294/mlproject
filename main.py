"""Entry point for running the data ingestion + transformation pipeline.

Run from the project root:
    python main.py
"""

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


def main() -> None:
    ingestion = DataIngestion()
    train_data, test_data = ingestion.initiate_data_ingestion()

    transformer = DataTransformation()
    train_arr, test_arr, _ = transformer.initiate_data_transformation(train_data, test_data)


if __name__ == "__main__":
    main()
