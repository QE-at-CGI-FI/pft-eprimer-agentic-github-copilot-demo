# Session 2

## Charter: Explore possible tests with GitHub Copilot Agent Mode

- *Target*: Eprimer-application based on what is saved on this Git Repository
- *Resources*: GitHub Copilot chat in Agent mode
- *Information*: What automated tests would get generated? What is their issue coverage? 

## What We Did

- Asked Github Copilot Agent mode to create python playwright tests of the first session
- Run the test to see they all 2/8 were successful
- Read error message to realize only installing dependencies were successful and those are the two first steps
- Reviewed the generated three files with test

## Details

- TEST: as implemented options for detected contractions
- TEST: as implemented option for possessive *hamlet's* making best demo case *To be or not to be is Hamlet's dilemma* with 9 total words, 3 discouraged words and 1 possible violations
- TEST: as expected options based on grammar for contractions
- TEST: *it's mine* handled as contraction not possessive with expected 2 words, 1 discouraged word, 1 possible violation
- TEST: *dogs' toys* should is a possessive but will not be flagged based on code
- TEST: possessive words *John's book* as possible violations 
- BUG: If John's is possessive and marked, dogs' is possessive and not marked, and this is inconsistent (+1)
- TEST: *'is'* in quotation marks should still be detected
- TEST: @#$%^&*(){}[]|\\:";'<>?/+=_-~ special characters
- TEST: punctuation marks, commas, periods and semicolons
- TEST: numbers *1234567890*
- TEST: html *<div>content</div>* and expect escaping for security concerns
- TEST: irregular spaces should not mess up word count
- TEST: case sensitivity
- TEST: Newlines and paragraphs
- TEST: empty input
- TEST: whitespace only input
- TEST: long text
- TEST: single letter
- TEST: just the possessive ending *'s*
- TEST: *I*, single letter that could be confused with I'm that is discouraged
- TEST: Reverse apostrophe *s'*
- TEST: multiple consecutive inputs
- TEST: clearing with an empty input

## Other Charters

- Self-implement a single programmatic test with parameterized inputs for all these
- systematic review of grammar of forms of to be
- systematic listing of variables that make text essentially different for this use case

## Other Notes

- Unnecessary grouping to smoke, regression and slow, only bug is meaningful decoration
- Wikipedia sample asserting words over 30 as significant misses issues the text could discover
- Wikipedia sample does good job summarizing domain of Eprime. Fact-check the claim of 1960s and David Bourland Jr as creator and Alfred Korzybski for general semantics as previous work. 
- Lot of repeated code and same tests repeated even without variation. Lot of unnecessary variation to inputs. 
- The tests found one bug and could have found more if the asserts were done more accurately

