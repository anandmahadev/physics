# Physics Notes Converter

A collection of scripts designed to process and format physics notes from HTML files.

## Project Structure

- `convert.py`: Script to convert layout classes (e.g., `qcard` to `card`) and format question/answer structures.
- `merge.py`: Script to merge content across different HTML files.
- `index.html`: Main physics notes file.
- `user.html`: User-specific physics notes or secondary content.

## Usage

### Converting Notes
To update the HTML structure of your notes, run:
```bash
python convert.py
```

### Merging Modules
To merge chemistry modules from `user.html` into `index.html`:
```bash
python merge.py
```
