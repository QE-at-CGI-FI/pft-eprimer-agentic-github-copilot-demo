# Manual Test Cases for Eprimer Application

## Test Environment
- **Application URL**: https://qe-at-cgi-fi.github.io/eprime/
- **Browser**: Any modern web browser
- **Test Type**: Manual functional testing

---

## TC001: Basic Functionality - Discouraged Words Detection
**Objective**: Verify the application correctly identifies and counts forms of "to be"

**Test Steps**:
1. Navigate to the Eprimer application
2. Enter text: "To be or not to be"
3. Observe the word highlighting and counters

**Expected Results**:
- Text "be" appears highlighted in red (2 occurrences)
- Discouraged words counter shows: 2
- Total words counter shows: 6

**Priority**: High

---

## TC002: Possessive Detection - Possible Violations
**Objective**: Verify possessive forms are detected as possible violations

**Test Steps**:
1. Enter text: "To be or not to be is Hamlet's dilemma"
2. Observe highlighting and counters

**Expected Results**:
- "be" highlighted in red (2 occurrences)
- "Hamlet's" highlighted in blue as possible violation
- Discouraged words: 3 (including "is")
- Possible violations: 1
- Total words: 9

**Priority**: High

---

## TC003: Contractions Detection
**Objective**: Verify various contractions are properly detected

**Test Steps**:
1. Test case 1: Enter "it's mine"
   - Expected: "it's" highlighted in red as discouraged word
2. Test case 2: Enter "they're here"
   - Expected: "they're" should be detected (known issue)
3. Test case 3: Enter "'twas the night"
   - Expected: "'twas" should be detected (known issue)

**Expected Results**:
- Contractions containing forms of "to be" are highlighted as discouraged words
- Counters update accordingly

**Priority**: Medium
**Note**: Some contractions ('re endings, 'twas) are not currently detected

---

## TC004: Text with Quotes
**Objective**: Verify detection works within quoted text

**Test Steps**:
1. Enter text: "He said 'to be or not to be'"
2. Observe if quoted words are detected

**Expected Results**:
- "be" inside quotes should still be highlighted as discouraged words

**Priority**: Medium
**Known Issue**: Quoted text may not be properly detected

---

## TC005: Word Count Accuracy
**Objective**: Verify word counting matches standard expectations

**Test Steps**:
1. Enter text: "To be or not to be – Hamlet's dilemma"
2. Compare word count with external word counter (e.g., Microsoft Word)

**Expected Results**:
- Word count should match standard word counting rules
- Special characters (–) should be handled consistently

**Priority**: Medium
**Known Issue**: Word count may differ from standard applications

---

## TC006: Long Text Scrolling
**Objective**: Verify interface handles long text input properly

**Test Steps**:
1. Copy large amount of text (e.g., Wikipedia article content)
2. Paste into text field
3. Try to scroll within the text area

**Expected Results**:
- Text area should allow scrolling to view all content
- All text should remain accessible

**Priority**: High
**Known Issue**: Scrolling does not work with long text

---

## TC007: Special Characters and Edge Cases
**Objective**: Verify application handles various input types

**Test Steps**:
1. Test empty input
2. Test whitespace-only input
3. Test special characters: @#$%^&*(){}[]|\:";'<>?/+=_-~
4. Test HTML tags: `<div>content</div>`
5. Test numbers: 1234567890

**Expected Results**:
- Application should handle all inputs gracefully
- No JavaScript errors in console
- Word counts should be accurate
- HTML should be escaped (security concern)

**Priority**: Medium

---

## TC008: Case Sensitivity
**Objective**: Verify detection works regardless of case

**Test Steps**:
1. Enter "BE" (uppercase)
2. Enter "Be" (title case)  
3. Enter "be" (lowercase)

**Expected Results**:
- All variations should be detected and highlighted
- Case should not affect detection

**Priority**: Low

---

## TC009: Line Breaks and Formatting
**Objective**: Verify text formatting doesn't break word detection

**Test Steps**:
1. Enter text with line breaks between words
2. Enter text with multiple spaces between words

**Expected Results**:
- Words separated by line breaks should be counted separately
- Multiple spaces should not affect word boundaries

**Priority**: Medium
**Known Issue**: Line feeds may cause words to be counted together

---

## TC010: Inconsistent Possessive Detection
**Objective**: Document inconsistency in possessive detection

**Test Steps**:
1. Enter "John's book" 
2. Enter "dogs' toys"
3. Compare detection behavior

**Expected Results**:
- Both should be treated consistently as possessives

**Priority**: Medium
**Known Issue**: Different possessive formats handled inconsistently

---

## Summary of Known Issues
Based on exploratory testing sessions:

1. **Scrolling Bug**: Text area doesn't scroll with long content
2. **Missing Contractions**: 're endings and 'twas not detected
3. **Quote Detection**: Words in quotes may not be detected
4. **Word Count Discrepancy**: May differ from standard word processors
5. **Line Break Handling**: Line feeds don't properly separate words
6. **Possessive Inconsistency**: Different possessive formats treated differently
7. **UI Clarity**: "Possible violations" terminology unclear

## Test Coverage Assessment
These test cases cover:
- ✅ Core functionality (discouraged word detection)
- ✅ Edge cases (empty input, special characters)
- ✅ User interface issues (scrolling, clarity)
- ✅ Data validation (word counting, case sensitivity)
- ✅ Grammar rules (contractions, possessives)