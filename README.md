

Kaggle Anti-Timeout Solution
=============================

Description:
This script is a simple solution to prevent Kaggle notebooks from timing out due to inactivity after 40 minutes. It automates keystrokes and mouse movements to simulate activity, ensuring that your session stays active without manual intervention.

How It Works:
- Simulates typing the letter "A" every 2 seconds.
- Moves the mouse cursor 3 pixels up and 3 pixels down every 2 seconds.
- Runs indefinitely until manually stopped by the user.

How to Use:
1. Install Python dependencies:
   - Ensure you have Python installed on your system.
   - Install `pyautogui` using:
     ```
     pip install pyautogui
     ```

2. Clone the repository:
   ```
   git clone https://github.com/your-username/Kaggle-AntiTimeout.git
   cd Kaggle-AntiTimeout
   ```

3. Run the script:
   ```
   python keep_active.py
   ```

4. Set up in Kaggle:
   - Open your Kaggle notebook.
   - Create a new cell in the notebook.
   - Place your cursor in the new cell and leave the script running.

Stopping the Script:
- To stop the script, press `Ctrl + C` in the terminal or close the terminal window.

Use Cases:
- Preventing Kaggle notebook inactivity timeouts.
- Keeping other systems or environments active where inactivity triggers timeouts.

Disclaimer:
This script is provided for educational purposes. Use it responsibly and ensure compliance with platform terms of service.

Contributors:
- Mohamed Aziz Bahloul
```