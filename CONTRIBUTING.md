
# Contributing to Gesture Mouse Control

Thank you for your interest in contributing to **Gesture Mouse Control** — a real-time, gesture-based virtual mouse built with Python and MediaPipe.

We welcome bug reports, feature requests, documentation improvements, and code contributions!

## 🧩 Project Goals

- Lightweight and efficient hand gesture tracking using right-hand input only.
- Real-time responsiveness on low-resource hardware.
- Configurable gesture-to-action mapping via YAML.
- Clean, modular Python code using standard open-source libraries.

## 🌳 Branching Strategy

We use three branches to manage development and releases:

- **`main`**: Stable, production-ready code for final releases.
- **`stag`**: Testing branch for CI/CD pipelines, including SonarQube code scanning and other quality checks.
- **`dev`**: Development branch for incoming raw code and new features. All contributions should target this branch.

Code flows from `dev` → `stag` → `main` after passing tests and quality checks.

## 🛠️ How to Contribute

### 1. Fork the Repository

Start by forking the repository to your own GitHub account and cloning it locally:

```bash
git clone https://github.com/YOUR_USERNAME/gesture-mouse-control.git
cd gesture-mouse-control
```

### 2. Set Up Development Environment

Install required dependencies:

```bash
pip install -r requirements.txt
```

Test your environment by running:

```bash
python main.py
```

### 3. Create a New Branch

Create a feature or bugfix branch off the `dev` branch with a meaningful name:

```bash
git checkout dev
git checkout -b feature/add-window-switch-gesture
```

### 4. Make Changes

- Develop your feature or fix on your branch.
- Ensure your changes align with the project goals and do not break existing functionality.
- Update `config.yaml` if adding new gestures or actions.

### 5. Test Locally

Before submitting, test your changes:

- Run `python main.py` to verify gesture functionality with webcam input.
- Ensure no runtime errors occur.
- Check that gestures trigger the expected actions.

## 📦 Contributing Code

### Code Style Guidelines

- Follow PEP8 for Python code.
- Keep logic modular and testable.
- Reuse existing functions to avoid duplication.
- Add comments for non-obvious logic.
- Use `logging` (optional) instead of `print()` for debug messages.

### Features & Improvements

- Update or add to `config.yaml` for new gestures or actions.
- Ensure new gesture logic does not conflict with existing mappings.
- Test on real-time webcam input to confirm reliability.

### Optional: TensorFlow Model Contributions

If contributing:

- A new ML-based gesture classifier
- A quantized TFLite model
- A new transformer-based gesture recognizer

Please include:

- Model description
- Input/output format
- Accuracy metrics
- Resource usage notes

## 🧪 Testing and CI/CD

- **Local Testing**: Test manually on Windows to ensure gestures work and no errors occur.
- **CI/CD on `stag`**: After your pull request is merged into `dev`, the code will be promoted to `stag` for automated testing, including:
  - CI/CD pipelines for build and test validation.
  - SonarQube code scanning for code quality and security.
- Only code that passes all checks on `stag` will be merged into `main` for release.

## 📥 Submitting a Pull Request

1. Push your changes to your fork:

   ```bash
   git push origin feature/add-window-switch-gesture
   ```

2. Open a Pull Request to the `dev` branch with:

   - A clear title (e.g., "Add window switch gesture support").
   - A short description of the change, including its purpose and impact.
   - Screenshots or short videos (if UI/gesture behavior is updated).

3. Monitor your PR:
   - Respond to feedback from maintainers.
   - Your code will undergo automated checks when merged into `stag`.
   - Address any issues reported by CI/CD or SonarQube scans.

## 🐞 Bug Reports & Feature Requests

Open an issue on GitHub with:

- Steps to reproduce (for bugs).
- Detailed description (for features).
- Screenshots or recordings, if relevant.
- Specify if the issue applies to `dev`, `stag`, or `main`.

## 🙌 Thanks

Thanks for helping improve **Gesture Mouse Control**! Your contributions help us build fast, intuitive, and intelligent input systems for the future.

### Key Changes
1. **Branching Strategy Section**: Added a new section explaining the `main`, `stag`, and `dev` branches, clarifying that contributions should target `dev`, with testing and CI/CD (including SonarQube) occurring on `stag` before release to `main`.
2. **Updated Branch Creation**: Specified that new branches should be created off `dev` (e.g., `git checkout dev` before creating a feature branch).
3. **Testing and CI/CD Section**: Clarified that local testing is required, and automated CI/CD pipelines (including SonarQube scanning) run on `stag` after merging into `dev`.
4. **Pull Request Target**: Changed the PR target from `main` to `dev` to align with the branching strategy.
5. **Issue Reporting**: Added a note to specify which branch (`dev`, `stag`, or `main`) the issue applies to for clarity.

### Notes
- **SonarQube Integration**: The file assumes SonarQube is part of the CI/CD pipeline on `stag`. If you have specific SonarQube requirements (e.g., coverage thresholds or custom rules), let me know, and I can add guidance for contributors.
- **CI/CD Details**: The file keeps CI/CD details minimal since contributors primarily interact with `dev`. If you want to include specific CI/CD tools or workflows (e.g., GitHub Actions for SonarQube), I can expand this section.
- **Additional Files**: If you want to add a **Code of Conduct**, issue templates, or GitHub Actions workflows for linting, testing, or SonarQube integration, let me know, and I can provide those.

Let me know if you need further tweaks or additional files to support your workflow!

