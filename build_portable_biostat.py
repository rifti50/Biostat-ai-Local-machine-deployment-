# build_portable_biostat.py
import PyInstaller.__main__
import sys
import os
import shutil
from pathlib import Path

def build_portable_executable():
    print("Building Portable BiostatsAI...")
    
    args = [
        'biostat_ai_main.py',
        '--name=BiostatsAI_Portable',
        '--onefile',
        '--windowed',
        '--icon=icon.ico',
        '--add-data=icon.ico;.',
        '--hidden-import=torch',
        '--hidden-import=transformers',
        '--hidden-import=sentence_transformers', 
        '--hidden-import=chromadb',
        '--hidden-import=langchain',
        '--hidden-import=PyPDF2',
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.ttk',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.messagebox',
        '--hidden-import=tkinter.scrolledtext',
        '--hidden-import=requests',
        '--hidden-import=zipfile',
        '--hidden-import=json',
        '--hidden-import=threading',
        '--hidden-import=subprocess',
        '--hidden-import=pathlib',
        '--hidden-import=datetime',
        '--hidden-import=time',
        '--hidden-import=shutil',
        '--collect-all=sentence_transformers',
        '--collect-all=torch',
        '--collect-all=transformers',
        '--collect-all=chromadb',
        '--collect-submodules=langchain',
        '--noconfirm',
        '--clean',
        '--optimize=2',
        '--exclude-module=matplotlib',
        '--exclude-module=pandas',
        '--exclude-module=numpy.distutils',
        '--exclude-module=setuptools',
    ]
    
    print("Running PyInstaller...")
    PyInstaller.__main__.run(args)
    
    print("Creating portable package...")
    create_portable_package()
    
    print("Build complete!")
    print("Find executable in: dist/BiostatsAI_Portable.exe")

def create_portable_package():
    dist_dir = Path("dist")
    package_dir = dist_dir / "BiostatsAI_Portable_Package"
    
    package_dir.mkdir(exist_ok=True)
    
    exe_file = dist_dir / "BiostatsAI_Portable.exe"
    if exe_file.exists():
        shutil.copy2(exe_file, package_dir / "BiostatsAI.exe")
    
    if Path("icon.ico").exists():
        shutil.copy2("icon.ico", package_dir / "icon.ico")
    
    readme_content = '''# BiostatsAI - Portable Edition

## Installation (No Python Required!)
1. Copy this entire folder to any drive (C:, D:, P:, etc.)
2. Double-click BiostatsAI.exe
3. Follow the setup wizard
4. Upload your PDFs and start learning!

## System Requirements
- Windows 10/11 (64-bit)
- 8GB RAM (16GB recommended)
- 30GB free disk space
- NVIDIA GPU recommended

## After Your Exams
Use the built-in uninstaller or delete this folder.

Good luck with your studies!'''
    
    with open(package_dir / "README.txt", "w") as f:
        f.write(readme_content)
    
    batch_content = '''@echo off
title BiostatsAI - Portable Biostatistics Tutor
echo Starting BiostatsAI...
start BiostatsAI.exe'''
    
    with open(package_dir / "Start_BiostatsAI.bat", "w") as f:
        f.write(batch_content)
    
    print("Portable package created: " + str(package_dir))

if __name__ == "__main__":
    build_portable_executable()
