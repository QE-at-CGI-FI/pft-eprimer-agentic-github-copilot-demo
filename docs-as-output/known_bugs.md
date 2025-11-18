# Consolidated Bug List

## E-Prime Violation Detection

1. Does not catch contractions: "you're", "we're", "they're"
2. Word in single quotes not properly recognized as E-Prime violation
3. Apostrophes block violation detection inconsistently: be' be ' be ' be'
4. Only detects typewriter's apostrophe, not typesetter's apostrophe
5. Full stop not considered when detecting "being" as verb vs. noun (e.g., "human being")
6. `<html>be<html>` is incorrectly detected as violation
7. Double-quoted "be" is detected while single-quoted 'be' is not
8. Two-part words (like people's last names) in possessive form not recognized as possible violations
9. Single possessive detected as blue, but plural possessive is not

## Word Counting Logic

10. Word count incorrect when pressing enter after a word
11. Two words separated by line feed counted as one word
12. Comma/special characters: space is only separator, special characters counted as words
13. Contractions like "I'm" count as two words instead of one
14. Writing two possible violations together separated by full stop counts less words than violations - counting logic doesn't match

## Input/Output Handling

15. Empty input should be blocked
16. Enter key gives different result than empty input
17. Enter key does not trigger the action as shortcut
18. No clear text button
19. Firefox text field does not clear with ctrl+R
20. Special character as start of line forces extra line change in grey display box

## Text Display & Layout

21. Output of multiline texts with spaces at end of line misaligned
22. Output field (grey) not aligned with the box
23. Output too left aligned
24. Long horizontal text goes outside output box with no scrolling
25. Text area sizing has no limitations - can be resized outside view
26. Mixed fonts make it hard to read and understand
27. Font selection doesn't help differentiate between 'l' and 'I'
28. Text box location in UI not where user would expect it

## Mobile & Responsive Design

29. Mobile horizontal view: no field or button visible
30. Mobile use not supported, styles very non-responsive
31. Zoom or resize of browser renders page unusable due to missing scroll bars

## Performance & Stability

32. Page crashes or gets slow after large input
33. Long text moves button outside user's access (vertical scroll disabled)
34. Safari allows scrolling when scroll bug is reintroduced unless browser restarted

## Accessibility

35. Images missing alt text
36. Accessibility warnings on contrast
37. Red/blue on grey has bad contrast
38. No fallover when JavaScript fails or is disabled

## Internationalization

39. Non-English characters printing issues
40. Lithuanian letters show up as italic
41. Inputting different languages (e.g., Japanese) for counting

## UI/UX & Content

42. User experience of colors - meaning unclear
43. Layout uses a lot of empty space
44. UI instructions for user are unclear
45. Missing instructions, e.g., placeholder text on text box
46. Terminology inconsistency: "discouraged/violations" vs "discouraged words/possibly discouraged words"
47. H1 title reads awkwardly and is inconsistent with the page title
48. License banner dominates page, should appear in footer instead

## Links & Navigation

49. Links inconsistent in how they open (some overload app, some open new window)
50. URL allows you to see the code
51. Wikipedia link opens in new tab with rel="nofollow" but lacks rel="noopener noreferrer" security best practice

## Assets & Resources

52. Favicon does not load (404 on console)
53. Missing security.txt (common convention for web applications)
54. License should be footer not an image - image is unnecessary
55. Image slows down loading of page

## Code Quality & Validation

56. CSS validator gives errors
57. HTML validator identifies 3 errors
58. ID naming is inconsistent (some camel case, others not)

## Missing Features

59. No privacy notice

---

## Summary

**Total: 59 unique bugs identified**

**Sources:**
- 1st Session: 32 bugs found across testing pairs (individual pairs found 5-16 bugs each)
- Known bugs list: 40 bugs
- After consolidation and removing duplicates: 59 unique bugs

**Note:** "Long text prevents scrolling" was marked as FIXED during the session
