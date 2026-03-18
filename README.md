# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Purpose: This project is a Streamlit number guessing game used to practice debugging AI-generated code, refactoring logic into reusable modules, and validating repairs with pytest.
- Bugs found: Reversed high/low hints, difficulty/reset range mismatch, off-by-one attempt tracking behavior, and type-mixing during guess comparison.
- Fixes applied: Moved core functions into logic_utils.py, corrected hint direction and numeric comparison flow, aligned reset behavior with selected difficulty, cleaned attempt/state updates, and added targeted regression tests.

## 📸 Demo

- [ x] Insert screenshot: fixed winning game state (streamlit app running with correct hint behavior)
- [ ] <img width="948" height="644" alt="image" src="https://github.com/user-attachments/assets/36ae6010-2f5f-4046-9943-5f7a054a5f2d" />
<img width="916" height="606" alt="image" src="https://github.com/user-attachments/assets/d65dfeb2-9630-4e5a-b8ef-99fbd304a0cc" />
<img width="911" height="589" alt="image" src="https://github.com/user-attachments/assets/a1a80505-5a7a-478e-b7d9-f4d8b9204fb7" />
<img width="931" height="559" alt="image" src="https://github.com/user-attachments/assets/80d06e93-ec95-4d21-a511-794049ed15d8" />
<img width="929" height="650" alt="image" src="https://github.com/user-attachments/assets/be290dcb-fc34-4c15-9ec6-f7e80e3e5f19" />



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
