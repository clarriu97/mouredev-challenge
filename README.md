# GO FOR THE CHALLENGE!

In this repository I will solve the challenges proposed by [Mouredev](https://github.com/mouredev).
Please check the [original repository](https://github.com/mouredev/Weekly-Challenge-2022-Kotlin)
where the challenges were published.

The programming lenguage used will be Python.

The repository will follow the next structure:

```
-- mouredev-challenge
 |-- challenge1
   |-- solution.py
   |-- input.txt
   |-- output.txt
 |-- challenge2
   |-- solution.py
   |-- input.txt
   |-- output.txt
 .
 .
 .
```

With this structure, we can set the input of our script and run it with the command:

```bash
cat input.txt | python solution.py
```

And, in case we have an output for the desired input, we can test our solution with the command:

```bash
cat input.txt | python solution.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
```
