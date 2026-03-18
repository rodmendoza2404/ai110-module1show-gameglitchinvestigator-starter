# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game opened fine, but once I started playing it felt like the logic was all over the place. I expected the hints, difficulty settings, and score behavior to stay consistent each round, but I kept seeing things that did not line up with what I entered. I also expected the starter tests to at least run, but they fail right away because one of the helper functions is still not implemented.

Glitch 1: The hints are backwards.
Expected: if I guess too high, it should tell me to go lower, and if I guess too low, it should tell me to go higher.
Actual: it does the opposite. A high guess says "Go HIGHER!" and a low guess says "Go LOWER!"

Glitch 2: The difficulty setting does not fully carry through.
Expected: when I pick Easy, Normal, or Hard, the number range and reset behavior should match that difficulty every time.
Actual: the main message still says "Guess a number between 1 and 100," and clicking New Game resets with 1 to 100 no matter what difficulty I picked.

Glitch 3: Attempts feel off from the start.
Expected: attempts left should begin at the full amount and go down clearly after each guess.
Actual: attempts start at 1 the first time, then reset to 0 on New Game, so the attempts-left display can feel inconsistent.

Glitch 4: Guess comparison changes type during play.
Expected: guesses should always be compared as numbers.
Actual: on some turns the secret is converted to a string, which can cause string-style comparisons instead of numeric ones.

---

## 2. How did you use AI as a teammate?

I used AI more as a thinking partner than just asking it to fix everything for me. Instead of saying “fix this code,” I described the behavior I expected and compared it with what was actually happening. AI helped me break down each glitch into smaller parts, like checking the hint logic separately from the game state. It also suggested possible causes, but I made sure to verify each one myself before changing anything. This helped me stay in control of the final solution instead of blindly trusting the output.

---

## 3. Debugging and testing your fixes

When debugging, I focused on one glitch at a time instead of trying to fix everything at once. For example, I first tested the hint logic by making specific guesses and checking if the messages matched the expected behavior. After each fix, I ran the game again to confirm that I didn’t break something else. I also paid attention to edge cases, like starting a new game or switching difficulty levels. This process helped me confirm that the fixes were actually working and not just appearing correct.
---

## 4. What did you learn about Streamlit and state?

I learned that managing state in Streamlit is very important because the app reruns from top to bottom every time there is an interaction. If the state is not handled correctly, values like attempts, difficulty, or the secret number can reset or behave inconsistently. I realized that I need to carefully control how variables are stored and updated using session state. This helped me understand why some of the bugs were happening, especially with resets and incorrect values. Overall, I learned that state management is key to making the app behave predictably.
---

## 5. Looking ahead: your developer habits
Going forward, I want to be more intentional about planning before jumping into coding. This project showed me that breaking problems into smaller components makes debugging much easier. I also want to keep using AI as a collaborator for ideas and structure, but not rely on it to make final decisions. Testing more frequently and checking edge cases is another habit I want to improve. Overall, I want to focus on writing code that I fully understand and can confidently explain.
