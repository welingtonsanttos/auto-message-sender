# WhatsApp Automation Bot

## Description
This project is a Python-based bot that automates sending messages via WhatsApp Web. It uses libraries such as `pyautogui`, `keyboard`, and `clipboard` to interact with the user interface and simulate user actions like clicking and typing.

## Features
- Opens WhatsApp Web automatically.
- Locates a specific contact or group based on an image (`Number.png`).
- Sends pre-defined messages stored in a text file (`Frases.txt`).
- Allows the user to interrupt the process using the `Esc` key.

## Requirements
- Python 3.8+
- Libraries:
  - `pyautogui`
  - `keyboard`
  - `clipboard`
- Assets:
  - `assets/Number.png`: Image of the contact or group to locate on WhatsApp Web.
  - `assets/Frases.txt`: File containing the list of messages to be sent.

## Installation
1. Clone the repository or download the project files.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Install the required libraries:
   ```bash
   pip install freeze
   pip freeze > requirements.txt
   ```
5. Ensure the `assets` folder contains:
   - `Number.png`: A screenshot of the contact or group you want to locate.
   - `Frases.txt`: A text file with one message per line.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. The bot will:
   - Open WhatsApp Web.
   - Search for the contact or group using the `Number.png` image.
   - Send each message from `Frases.txt`.
3. Press the `Esc` key to interrupt the process. A confirmation dialog will appear.

## File Structure
```
project/
├── assets/
│   ├── Frases.txt
│   └── Number.png
├── main.py
└── README.md
```

## Notes
- Ensure that the `Number.png` image is clear and matches the contact or group as displayed on WhatsApp Web.
- The bot relies on pixel matching, so changes in screen resolution or WhatsApp Web layout may affect functionality.

## Contributing
Feel free to fork this project and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
