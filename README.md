# GO FOR THE CHALLENGE!

In this repository I will solve the challenges proposed by [Mouredev](https://github.com/mouredev).
Please check the [original repository](https://github.com/mouredev/Weekly-Challenge-2022-Kotlin)
where the challenges were published.

The programming lenguage used will be Python.

The repository will follow the next structure:

```
-- mouredev-challenge
 |-- challenge0
   |-- solution.py
   |-- input.txt
   |-- output.txt
   |-- README.md
 |-- challenge1
   |-- solution.py
   |-- input.txt
   |-- output.txt
   |-- README.md
 .
 .
 .
```

With this structure:

- You have a `README.md` file inside each challenge, with the description.
- You can run a particular script inside its folder with the command:
  ```bash
  python solution.py
  ```
- You can set the input of our script in case it has, and run it with the command:
  ```bash
  cat input.txt | python solution.py
  ```
- In case we have an output for the desired input, you can test the solution with the command:

  ```bash
  cat input.txt | python solution.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
  ```
