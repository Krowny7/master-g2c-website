import os

def create_directories():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, 'static')
    
    # Create directories
    directories = [
        os.path.join(static_dir, 'img', 'campus'),
        os.path.join(static_dir, 'img', 'news'),
        os.path.join(static_dir, 'img', 'team'),
        os.path.join(static_dir, 'img', 'partners')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

if __name__ == "__main__":
    create_directories()
