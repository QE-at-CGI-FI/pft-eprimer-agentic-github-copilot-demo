## Ready-to-run micro-charters

### Onboarding and account flows
- Create account with valid data, reload between steps; verify progress persistence.
- Create account with duplicate email; confirm error clarity and no account side-effects.
- Start onboarding, close browser, reopen via deep link; resume at correct step.
- Skip optional step, later return to complete; confirm gating and reminders.
- Attempt password reset with unregistered email; ensure generic response, no user enumeration.
- Password reset: use expired link; verify UX and re-request path.
- Login with wrong password thrice; check lockout, cooldown, and messaging.
- Social login cancel mid-consent; ensure graceful return and no partial sessions.
- Session expires during final onboarding step; ensure re-auth preserves entered data.

### Navigation and state recovery
- Open app in two tabs; perform changes in one; confirm other updates or shows refresh prompt.
- Use back/forward during multi-step flow; ensure state remains consistent and guarded.
- Refresh during loading spinner; verify idempotent load and no duplicate calls.
- Deep link to restricted page while logged out; confirm redirect to login and back.
- Bookmark a detail page; invalidate access; ensure correct 403 UX and navigation options.

### CRUD depth and idempotency
- Create entity, immediately double-click save; verify single record created.
- Create then edit fields to boundary values; confirm validations, save, and rendering.
- Delete entity, undo within grace period; ensure full restoration including relationships.
- Bulk delete with a subset failing; confirm partial success handling and reporting.
- Recreate entity with same natural key; ensure conflict handling and messaging.
- Import CSV with duplicate rows; verify deduplication rules and outcome clarity.

### Concurrency and conflicts
- Two users edit same record, save both; verify conflict detection and resolution UI.
- User A edits while User B archives; ensure A’s save is blocked with guidance.
- Optimistic lock: lose network after save; verify retry or user notification.
- Pessimistic lock: abandon edit; ensure lock release after timeout.

### Validation and input variability
- Paste 10k-character string into notes; check input limits and errors.
- Enter emojis, RTL text, and ZWJ sequences; confirm rendering and storage integrity.
- Use high-precision decimals in currency; verify rounding rules and display.
- Input leading/trailing spaces; confirm trimming or preservation policy.
- Provide invalid date formats per locale; ensure clear validation messages.
- Use injection-like strings in harmless fields; verify proper escaping in UI and logs.

### Files and uploads
- Upload 0-byte, maximum-size, and slightly-over-limit files; verify errors.
- Upload valid mime with wrong extension; rely on content detection, not extension.
- Upload duplicate filename twice; ensure unique handling and user messaging.
- Interrupt upload mid-stream; resume if supported or fail gracefully.
- Slow network upload with 400ms RTT; verify progress and cancel behavior.

### Search, filters, sorting, pagination
- Search with special chars, diacritics, and case variants; verify normalization.
- Apply multiple filters then clear one; ensure other filters persist correctly.
- Paginate to last page; add items; confirm pagination updates and scroll position.
- Sort by column, edit a row; verify sort stability and position retention.
- Rapidly change filters while requests in flight; ensure prior requests are canceled.

### Permissions and roles
- Access admin-only page as regular user; confirm 403 and no data leakage.
- Modify URL ID to another tenant’s resource; verify IDOR protection.
- Switch roles mid-session; verify nav, cached data, and permissions refresh.
- Attempt action after role removal; confirm server-side enforcement blocks it.

### Authentication and session
- Expire token via tools and perform save; ensure re-auth and idempotent retry.
- Logout in one tab; act in another; confirm session invalidation and data safety.
- Remember-me vs session-only; verify persistence after browser restart.

### Internationalization and formatting
- Switch language mid-flow; verify translated validation messages and no layout break.
- Use long translations; check truncation, wrapping, and tooltip fallbacks.
- Arabic or Hebrew locale with 200% zoom; ensure layout and focus order.
- Time zones: create at 23:30 local, view in UTC; confirm exact times and DST.
- Numbers: German locale decimal comma; verify parsing and display in forms.

### Accessibility
- Navigate key workflows with keyboard only; confirm visible focus and no traps.
- Screen reader: verify landmarks, headings, and live region announcements.
- Form errors: focus moves to first error, error linked to input via aria.
- Contrast in light/dark mode; confirm meets minimum AA.
- Reduced motion preference; ensure animations are disabled or toned down.

### Performance and resilience
- Cold load on slow 3G; measure first interaction latency and spinners.
- Rapidly click primary action five times; ensure debounce or idempotency.
- Long list rendering; verify virtualization and smooth scroll.
- Simulate 5% packet loss; ensure retries/backoff without UI freezes.
- Kill API mid-request; verify user message and preserved form data.

### Caching, storage, and updates
- Update entity then hard reload; confirm latest data and no stale cache.
- Service worker update available; ensure in-app refresh prompt works.
- Clear local and session storage; app should rehydrate gracefully.
- Exceed storage quota while saving draft; verify error recovery.

### Notifications, emails, and webhooks
- Trigger email with invalid address; ensure bounce handling and user feedback.
- Receive duplicate webhook; verify idempotent processing.
- Turn off notifications, perform action; confirm no emails are sent.
- Delayed webhook delivery; ensure eventual consistency and UI state correction.

### Error handling and observability
- Force 500 from key endpoint; verify user-safe message and no PII exposure.
- Client error 422 with field errors; ensure inline mapping and summary.
- Simulate network offline then back online; confirm queued actions retry.
- Verify logs/telemetry for key actions; ensure structured, no secrets, correct user IDs.

### Feature flags and configuration
- Toggle feature flag off mid-session; confirm UI hides and routes guard.
- Missing config value at startup; ensure defaults and clear error surfacing.
- A/B variant consistency across reloads; verify stickiness per user.

### Import/export and interoperability
- Export CSV with commas/semicolons; verify correct quoting per locale.
- Import malformed CSV; ensure robust parsing and actionable errors.
- Export then re-import same data; expect no diffs after round-trip.

### Security sanity checks
- CSRF: submit form from another origin; verify token enforcement.
- Open redirects: tamper with returnUrl; ensure whitelisting.
- Rate limiting: burst requests on sensitive endpoint; confirm throttling UX.
- Headers: verify CSP, HSTS, X-Frame-Options, and CORS settings.

### Mobile and device specifics
- Small viewport with software keyboard; ensure inputs not obscured.
- Orientation change mid-form; confirm layout stability and data retention.
- High-contrast mode on OS; verify icon and color legibility.

### Reporting and analytics
- Apply filter then export; ensure export respects current filters.
- Analytics opt-out enabled; verify no events are sent.
- Event schema changes behind flag; ensure backward compatibility.

### Recovery and support flows
- Trigger hard error; verify recovery link, diagnostics ID, and support path.
- Copy error details; ensure safe, non-sensitive content for support tickets.

### Admin and maintenance
- Perform bulk update job; verify progress, partial failures, and audit logs.
- Rotate API keys; confirm old keys revoked and new keys propagated.


