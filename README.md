# Visual Spotify Jukebox Sorting

## Project Overview
This project compares two sorting algorithms implemented from scratch using a large Spotify track dataset. The goal is to analyze how different algorithms perform when sorting real-world data by popularity.

## Features
- Uses Spotify-based dataset (100,000+ tracks)
- Sorts by **popularity**
- Compares **Bucket Sort** vs **Merge Sort**
- Displays results through a local interface

## Algorithms Implemented
- Bucket Sort (from scratch)
- Merge Sort (from scratch)

## Dataset
Each row represents one track and includes:
- track_id
- track_name
- artist_name
- album_name
- popularity
- duration_ms
- explicit

Dataset file:
dataset.csv

## Requirements
- Python 3
- pip

## Setup
1. Clone the repository
2. Open in your IDE
3. Install dependencies:
   pip install -r requirements.txt

## How to Run
Run the program:

python display.py

This launches the local visualization interface.

## Important
Make sure this file exists before running:

dataset.csv

## Project Structure
- display.py
- bucket_sort.py
- merge_sort.py
- dataset.csv
- README.md

## Team
Jukeboxers:
- Lewis Wilson
- Bernardo Lopez Leon
- Leah Zabad

## License
Academic project (no license)
