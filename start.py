#!/usr/bin/env python3
"""
Medical Invoice Processing System - Startup Script
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print(" Python 3.8+ required")
        return False
    
    # Check if required packages are installed
    required_packages = [
        'fastapi', 'uvicorn', 'pytesseract', 'opencv-python',
        'spacy', 'scikit-learn', 'streamlit'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print(" Dependencies check passed")
    return True

def setup_environment():
    """Setup environment and directories"""
    print(" Setting up environment...")
    
    # Create necessary directories
    directories = ['uploads', 'models', 'logs']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f" Created directory: {directory}")
    
    # Copy environment file if it doesn't exist
    if not Path('.env').exists() and Path('env.example').exists():
        import shutil
        shutil.copy('env.example', '.env')
        print(" Created .env file from template")
    
    print("Environment setup complete")

def install_spacy_model():
    """Install spaCy model if not present"""
    print("Installing spaCy model...")
    
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print("spaCy model already installed")
    except OSError:
        print("Installing spaCy model...")
        subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], check=True)
        print(" spaCy model installed")

def start_api_server():
    """Start the FastAPI server"""
    print(" Starting API server...")
    
    try:
        # Start the server in a subprocess
        process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ])
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Check if server is running
        try:
            response = requests.get("http://localhost:8000/api/v1/health", timeout=5)
            if response.status_code == 200:
                print(" API server is running on http://localhost:8000")
                return process
            else:
                print(" API server failed to start properly")
                return None
        except requests.exceptions.RequestException:
            print(" API server failed to start")
            return None
            
    except Exception as e:
        print(f" Error starting API server: {e}")
        return None

def start_streamlit():
    """Start the Streamlit frontend"""
    print("Starting Streamlit frontend...")
    
    try:
        # Start Streamlit in a subprocess
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run",
            "frontend/streamlit_app.py",
            "--server.port=8501",
            "--server.address=0.0.0.0"
        ])
        
        # Wait a moment for server to start
        time.sleep(5)
        
        print(" Streamlit frontend is running on http://localhost:8501")
        return process
        
    except Exception as e:
        print(f"Error starting Streamlit: {e}")
        return None

def main():
    """Main startup function"""
    print(" Medical Invoice Processing System")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    # Install spaCy model
    install_spacy_model()
    
    # Start API server
    api_process = start_api_server()
    if not api_process:
        sys.exit(1)
    
    # Start Streamlit frontend
    streamlit_process = start_streamlit()
    if not streamlit_process:
        print("⚠️ Frontend failed to start, but API is running")
    
    print("\n System is running!")
    print("API Documentation: http://localhost:8000/docs")
    print(" Web Dashboard: http://localhost:8501")
    print(" Health Check: http://localhost:8000/api/v1/health")
    print("\nPress Ctrl+C to stop all services")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Shutting down services...")
        
        if api_process:
            api_process.terminate()
            print(" API server stopped")
        
        if streamlit_process:
            streamlit_process.terminate()
            print(" Streamlit frontend stopped")
        

if __name__ == "__main__":
    main() 