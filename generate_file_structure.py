import os

'''
    Generating the project folder strucutre.
'''

def create_directory(directory):
    try:
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    except FileExistsError:
        print(f"Directory already exists: {directory}")

def create_file(directory, filename, content=None):
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, "w") as file:
            if content:
                file.write(content)

        print(f"Created file {file_path}")

    except Exception as e:
        print(f"Error creating file {file_path}\`n{e}")

    
def generate_project_structure():
    # Base directory
    base_directory = "drm-free-game-data-engineering"
    create_directory(base_directory)

    # Directories
    directories = [
        "data_acquisition",
        "data_cleaning",
        "feature_engineering",
        "data_aggregation",
        "time_series_analysis",
        "data_transformation",
        "filtering_and_subsetting",
        "exporting_to_postgresql",
        "visualization",
        "documentation",
        "tests",
        "scalability",
        "collaboration",
        "airflow_dags"
    ]

    for directory in directories:
        create_directory(os.path.join(base_directory, directory))

    
    # Files
    create_file(base_directory, "requirements.txt")
    create_file(base_directory, "requirements-dev.txt", content="pytest==7.4.3\n")
    create_file(base_directory, ".gitignore", content="venv/\n__pycache__/\n*.pyc\n*.pyo\n*.pyd\n")

    print("\nProject structure created successfully!")

if __name__ == "__main__":
    generate_project_structure()



