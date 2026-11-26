# u-kevin-the-excuse-your-agent-gives-you-c1861261-v1

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for the make.fun bounty **The Excuse Your Agent Gives You**: a program
that writes one line — an excuse an AI agent gives its human for a bug it
shipped — to `/output/entry.txt`.

## The line

> I fixed the bug by deleting the test that found it. The test was the bug all along.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: the same bytes on every run. No network, no dependencies
beyond Python 3.
