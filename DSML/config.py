"""Config file for module."""
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv()

DATASET = "gabrielluizone/high-school-alcoholism-and-academic-performance"

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")
DATA_DIR = PROJ_ROOT / "dataset"
RAW_DATA_DIR = DATA_DIR / "raw"
DATASET_FILE_PATH = RAW_DATA_DIR / "EN_Dataset/en_lpor_explorer.csv"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

MODEL_NAME = "alcoholism-based-on-social"

categorical = [
    'School', 'Gender', 'Housing_Type', 'Family_Size', 'Parental_Status',
    'Mother_Education', 'Father_Education', 'Mother_Work', 'Father_Work',
    'Reason_School_Choice', 'Legal_Responsibility', 'Commute_Time',
    'Weekly_Study_Time', 'Extra_Educational_Support', 'Parental_Educational_Support',
    'Private_Tutoring', 'Extracurricular_Activities', 'Attended_Daycare',
    'Desire_Graduate_Education', 'Has_Internet', 'Is_Dating',
    'Good_Family_Relationship', 'Free_Time_After_School', 'Time_with_Friends',
    'Health_Status',
]

target = "Alcoholic"
