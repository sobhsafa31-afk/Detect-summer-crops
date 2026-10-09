# Known Issues and Review Notes

This document summarizes findings from a static code review. The fixes described below are present on the `docs/project-polish` branch. The application has not yet been validated through a complete runtime test.

## High-Priority Issues Addressed

### 1. Processing continued after an image-loading error
- **File:** `main.py`, `check()`
- **Issue:** The error handler displayed a message but did not stop the function.
- **Change:** The function now returns after a handled image-loading error, preventing subsequent processing from using an unavailable image.
- **Validation:** Runtime testing is still required.

### 2. Possible division by zero in histogram ratio calculation
- **File:** `Function_images.py`, `caclc_ratio()`
- **Issue:** The denominator could be zero when the histogram had no counts below the selected threshold.
- **Change:** The function now returns positive infinity when the denominator is zero, avoiding `ZeroDivisionError`.
- **Validation:** Runtime testing is still required.

### 3. Possible division by zero when averaging an empty pixel list
- **File:** `Function_images.py`, `average()`
- **Issue:** An empty list could result when background filtering removed every pixel.
- **Change:** The function now raises a clear `ValueError` for an empty list, and `main.py` displays an error message and stops processing.
- **Validation:** Runtime testing is still required.

## Remaining Medium-Priority Issues

### 4. Assumption that image pixels are RGB triples
- **File:** `Function_images.py`, `remove_background()` and `average()`
- **Observation:** Pixel values are accessed as three-channel RGB tuples, but image mode is not explicitly normalized.
- **Potential impact:** Grayscale, palette-based, or RGBA images may fail or be processed incorrectly.

### 5. Simple background filtering can remove parts of the object
- **File:** `Function_images.py`, `remove_background()`
- **Observation:** Pixels are retained only when all three channels are below 230.
- **Potential impact:** Bright or white areas of the produce may be removed along with the background. This is not semantic object segmentation.

### 6. Potentially expensive histogram calculation
- **File:** `Function_images.py`, `get_hist_data()`
- **Observation:** The function iterates over all pixels separately for each grayscale value from 0 through 255.
- **Potential impact:** Processing may be slow for large images.

### 7. Classification rules have not been accuracy-tested
- **File:** `Function_images.py`, `check_object()` and `finall_check()`
- **Observation:** Classification depends on hand-tuned color and brightness thresholds.
- **Potential impact:** Similar colors, lighting changes, and varied backgrounds may lead to incorrect labels. The repository does not currently include a labeled evaluation dataset or reported accuracy metrics.

## Lower-Priority Maintainability Notes

### 8. Potentially unused helpers or imports
- **Files:** `Function_images.py` and `main.py`
- **Observation:** Some helper functions and imports do not appear to be used in the visible application flow.
- **Potential impact:** They may add complexity. Confirm through repository-wide usage checks and tests before removing anything.

### 9. Broad exception handling remains in the application
- **File:** `main.py`, `check()`
- **Observation:** The function still uses broad exception handling in parts of the code.
- **Potential impact:** Unexpected failures may be obscured, making debugging harder. This was not changed because the approved scope was limited to the three high-priority issues.

## Validation Status

- The code changes were reviewed statically.
- A complete runtime test has not yet been performed.
- Medium- and lower-priority findings have intentionally not been changed.
- Before release, add focused automated tests for image-load failures, empty pixel lists, and zero-denominator histograms, then validate classification against a labeled dataset.
