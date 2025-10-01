# Single Comprehensive Test Case for Eprimer Application

## TC001: Comprehensive Eprimer Functionality Test
**Objective**: Verify all core functionality of the Eprimer application through systematic input variations

**Test Environment**:
- **Application URL**: https://qe-at-cgi-fi.github.io/eprime/
- **Browser**: Any modern web browser

**Test Data Variables**:
```
# Basic discouraged words
basic_inputs = ["be", "is", "am", "are", "was", "were", "being", "been"]

# Contractions (working)
working_contractions = ["it's", "I'm", "you're", "we're", "they're", "he's", "she's"]

# Contractions (known issues)
broken_contractions = ["they're", "'twas"]

# Possessives
possessives = ["John's", "Hamlet's", "dogs'", "cats'"]

# Case variations
case_variations = ["BE", "Be", "be", "IS", "Is", "is"]

# Complex test strings
demo_text = "To be or not to be is Hamlet's dilemma"
quote_text = "He said 'to be or not to be'"
special_chars = "@#$%^&*(){}[]|\\:\"';'<>?/+=_-~"
html_text = "<div>content</div>"
numbers = "1234567890"
empty_inputs = ["", "   ", "\n\n"]

# Long text (for scrolling test)
long_text = [Wikipedia article content or similar large text block]
```

**Test Steps**:

1. **Setup and Basic Functionality**
   - Navigate to the Eprimer application
   - Verify interface loads correctly with text area and counters

2. **Test Basic Discouraged Words**
   - For each word in `basic_inputs`:
     - Clear text area
     - Enter the word
     - Verify red highlighting appears
     - Verify discouraged words counter increments
     - Verify total words counter = 1

3. **Test Demo Case**
   - Enter: "To be or not to be is Hamlet's dilemma"
   - Verify results:
     - "be" highlighted red (2 occurrences)
     - "is" highlighted red (1 occurrence)
     - "Hamlet's" highlighted blue (possible violation)
     - Discouraged words: 3
     - Possible violations: 1
     - Total words: 9

4. **Test Contractions**
   - For each contraction in `working_contractions`:
     - Enter contraction in isolation
     - Verify red highlighting (discouraged word)
   - For each contraction in `broken_contractions`:
     - Enter contraction in isolation
     - Document if detection fails (known issue)

5. **Test Possessives**
   - For each possessive in `possessives`:
     - Enter possessive word
     - Check if highlighted as possible violation (blue)
     - Document inconsistencies

6. **Test Case Sensitivity**
   - For each variation in `case_variations`:
     - Enter the word
     - Verify detection works regardless of case

7. **Test Edge Cases**
   - Empty input: Verify counters show 0
   - Whitespace only: Verify counters show 0
   - Special characters: Enter `special_chars`, verify no errors
   - HTML: Enter `html_text`, verify proper escaping
   - Numbers: Enter `numbers`, verify word count handling

8. **Test Quoted Text**
   - Enter: "He said 'to be or not to be'"
   - Verify words inside quotes are still detected

9. **Test Scrolling (Known Issue)**
   - Paste large text block
   - Attempt to scroll within text area
   - Document scrolling behavior

10. **Test Word Count Accuracy**
    - Enter: "To be or not to be – Hamlet's dilemma"
    - Compare word count with external reference (e.g., Microsoft Word)
    - Document any discrepancies

11. **Test Line Breaks and Formatting**
    - Enter text with line breaks between words
    - Enter text with multiple spaces
    - Verify word separation and counting

**Expected Results Summary**:
- All forms of "to be" should be detected and highlighted in red
- Possessives should be consistently highlighted in blue
- Case should not affect detection
- Word counts should be accurate
- Interface should handle edge cases gracefully
- No JavaScript console errors

**Known Issues to Document**:
1. Scrolling doesn't work with long text
2. Some contractions ('re endings, 'twas) not detected
3. Quoted text detection may fail
4. Word count may differ from standard applications
5. Line feeds may cause word counting issues
6. Possessive detection inconsistencies
7. "Possible violations" terminology unclear

**Pass Criteria**:
- Core functionality works (basic discouraged word detection)
- Demo case produces expected results
- No critical JavaScript errors
- Interface remains responsive

**Fail Criteria**:
- Basic "to be" forms not detected
- Application crashes or becomes unresponsive
- Critical security issues (unescaped HTML execution)

**Priority**: High
**Estimated Time**: 30-45 minutes