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

I used GitHub Copilot in VS Code as my main AI teammate during this lab. One suggestion that was correct was to move core game logic into logic_utils.py and keep app.py focused on Streamlit state/UI. I verified that by running pytest and seeing all tests pass after the refactor, and by launching the app to confirm it still worked. One suggestion that was misleading earlier was logic that converted the secret number to a string on certain turns and then compared it to integer guesses. I confirmed that was a bad idea by tracing the code path and seeing how it could cause incorrect comparisons and wrong hints.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only after two checks: automated tests passed and the behavior looked correct in the live Streamlit app. For automated testing, I added a specific regression test for the hint direction bug (Too High should map to "Go LOWER!") and ran pytest until it passed with the rest of the suite. I also ran a manual check by starting the app and verifying that difficulty range text, reset behavior, and hints matched the selected settings. AI helped me generate test ideas quickly, but I still decided which tests were meaningful and which ones were too broad or weak.

---

## 4. What did you learn about Streamlit and state?

I would explain Streamlit reruns like this: every button click reruns the script from top to bottom, so local variables do not automatically "remember" old values. If you want values to persist across clicks, you have to put them in st.session_state. That is why the app can behave strangely if secret number, attempts, or difficulty are not stored and reset carefully. Once I understood that, the bugs made a lot more sense and were easier to fix.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing a focused regression test right after I fix a bug so I do not reintroduce it later. Next time I work with AI, I will ask for smaller, single-purpose changes instead of bigger edits, because that makes reviewing diffs easier and safer. This project changed how I see AI-generated code: I now treat it as a useful draft, not a final answer. AI can help me move faster, but I still have to verify behavior and make final decisions as the developer.
