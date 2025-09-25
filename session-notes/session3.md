# Session 1

## Charter: Explore Eprimer wikipedia page for good eprime inputs

- *Target*: Eprimer application
- *Resources*: Eprime wikipedia page
- *Information*: What are valid detections when text is eprime or not? Is there good sources of test data? 

## What We Did

- Tried out tenses, contractions, negative contractions and non-standard contractions in isolation as smaller strings
- Tried out functions of to be to confirm the samples aren't identified as e-prime
- Downloaded pdf bible in eprime and turned that into a text file used in testing
- Analyzed shallowly the pdf bible as test input for low number of eprime detections as expected, leaving detailed analysis for later

## Details

- BUG: some contractions aren't detected - everything ending with 're and 'twas of non-standard contractions
- TEST: possible violations are everything with 's in the end
- BUG: line feed at end of word counts words together, only space acts as separator
- BUG: "be" in quotes not detected
- BUG: being detected even with dual meaning
- BUG: *To be or not to be – Hamlet’s dilemma* miscounts the number of words compared to Microsoft Word
- TEST: *To be or not to be – Hamlet’s dilemma* as great demo text
- QUESTION: Is wordcount a relevant feature for this application? 

## Other Charters

- Read code for ideas of limitations of implementation
- Research how words are counted in e.g. Microsoft word and compare to this
- Analyze eprime bible for word count and patterns of correct / incorrect detections
- Formulate a test strategy as ideas driving test design

## Other Notes


