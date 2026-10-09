# Detect Summer Crops

A small Python desktop application that estimates the type of selected summer crops and vegetables from image color and brightness features.

> **Project status:** This is an early, rule-based prototype. Predictions are estimates, and accuracy has not yet been evaluated against a labeled dataset.

## Features

- Desktop graphical interface built with `tkinter`
- Loads an image from a local file path
- Extracts average color and basic grayscale histogram features
- Uses hand-written rules to classify examples such as eggplant, carrot, onion, potato, cucumber, zucchini, and bell pepper
- Separates the graphical interface (`main.py`) from image-processing and classification functions (`Function_images.py`)

## Project Structure

```text
Detect-summer-crops/
├── main.py                  # Desktop interface and classification flow
├── Function_images.py       # Image loading, feature extraction, and classification rules
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Local and generated files excluded from Git
└── docs/
    └── KNOWN_ISSUES.md      # Known issues and review notes
```

## Requirements

- Python 3
- A desktop environment with `tkinter` support
- The packages listed in `requirements.txt`

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/sobhsafa31-afk/Detect-summer-crops.git
   cd Detect-summer-crops
   ```

2. (Recommended) Create and activate a virtual environment.

   **Windows (PowerShell)**

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python main.py
   ```

5. Enter the local path to an image in the address field and select the submit button.

## How Classification Works

1. The application loads the image from the provided local path.
2. A simple threshold-based rule filters bright pixels.
3. The application calculates average color and grayscale histogram features.
4. Hand-written conditional rules in `Function_images.py` return a possible label.

This project does not use a trained machine-learning model. Lighting, background, viewing angle, image quality, and similar colors across different produce can affect predictions.

## Limitations

- No automated test suite or documented accuracy evaluation is currently included.
- Support for different image modes and invalid inputs requires further validation.
- The color-based rules have not been validated for production or safety-critical use.
- The high-priority issues previously identified have been addressed on the current review branch. Remaining findings are documented in [Known Issues and Review Notes](docs/KNOWN_ISSUES.md).

## Contributing

Bug reports and improvements are welcome. When reporting an issue, include your operating system, Python version, input example when possible, and steps to reproduce the behavior.

## License

No license file is currently provided. Until a license is added, do not assume that redistribution or reuse is permitted.
