# 🧠 Online Quiz Checker

A simple approach which alerts you if teacher put another online quiz in random time ⏰

---

## 💡 How to Use:
1. Clone the repository
2. Download and install these libs in your python interpreter:
   ```bash
   pip install pyautogui pyperclip pygame
3. Login once in the URL that we want to monitor, so the browser after this time, uses your cookie to go on!
4. Run code and enjoy the rest of your life :)

## 🛠️ how I came to this solution:
very soon! I figured out each time that teacher puts new online quiz in our site, the base HTML file will be bigger for more requesting for more objects. using other approaches was not efficient. This code, refreshes the website that I loged in, and tells me the size of HTML file in Byte. So if something is giong bigger than usual was, plays a sound (HEIDAR, Heidar, Because our teacher's name is Dr.Heidarpour😁) and makes the screen RED for Visual notice!
![RED Alert](pic.png)

## 🐞 Known bugs and unhandled edge cases:
If the quiz is posted on a different page, you will be mokked
If he updates one of existing objects as new quiz, you will be mokked
If the teacher uses JavaScript to insert content dynamically, detection may fail
IF ...
.
.
.
But it was useful for me atleast. I made this code in Bus, So... why not?

## 👻Tips:
You can connect this code to:
- An AI API to automatically solve questions 😈
- Send/receive inputs using pyautogui to interact with the browser.

This idea was good enough for a booking launch at my university — maybe it will be for you too!

> [!TIP]
> “If you can’t beat the quiz, outsmart it.”

