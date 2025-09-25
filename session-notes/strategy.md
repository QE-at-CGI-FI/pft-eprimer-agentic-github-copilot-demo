# Test Strategy - Ideas that Drive Test Design

## What is the product?
E-Primer is an English text validator that checks text against specific rules for avoiding the verb to be. It identifies rule-breaking in two categories: those that can be checked automatically, and those that currently require human assessment.

## What are the key potential risks?
- It suggests incorrect corrections and misses genuine issues in realistic text samples.
- It miscounts words in ways that cause underestimation of processing scale.
- It fails on some browsers and with certain data samples.
- It requires more effort to learn than the proofreading value it provides.

## How could we test the product to evaluate the actual risks associated with it?

- Research and understand the rules of E-Prime.
- Collect data samples (both short and long) representing correct E-Prime text and text that violates E-Prime rules, and run them through the program.
- Verify that common forms of to be are consistently recognized across samples.
- Document specifications as automated tests that demonstrate E-Prime rules and enable subsets of tests to run across browsers.
- Test whether the word count can be fooled into reporting fewer or more words with specific data samples.
- Run the web application through standard HTML validators.
- Visually check the page with realistic E-Prime text samples.
- Review the application code for inspiration, focusing on function names rather than implementation details.
- Summarize learning obstacles for users and compare the application’s value to alternative proofreading methods.