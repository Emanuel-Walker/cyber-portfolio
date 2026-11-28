---
name: statement-reconciliation-report
description: >-
  Use when someone hands over bank, account, or payment statements and wants a
  verified record of where the money went.
---
# Statement reconciliation report

BLUF: Reconcile every parsed number to the printed statement totals before any analysis, then deliver a formula-driven workbook and a readable PDF.

## Steps
1. Extract text from each statement PDF with layout preserved. Parse transactions by column position.
2. Match parsed deposit and withdrawal totals to each statement's printed totals. Stop until they match exactly.
3. Classify each transaction by keyword rules on its own description. Keep unsupported categories Unknown and disclose them. Never force a classification to reach a zero-unknown target.
4. Run analytics: monthly and weekly roll-ups, top payers and payees, recurring bills, failed payments, duplicates.
5. Keep confirmed facts apart from inferences. Log anomalies with a severity on their own tab.
6. Build the workbook with live formulas pointing at one master transaction tab plus a reconciliation tab. Recalc and confirm zero errors.
7. Build the PDF with product-build-and-release: totals, detail tables, method, findings, open questions, full numbered ledger.
8. Check the PDF for overlapping or off-page text. Fix before delivery.

## Privacy
- Keep statements and outputs private. Never paste account numbers or real amounts into shared notes, issues, repos, or public files.

## Done when
- Every statement reconciles.
- The workbook recalcs with zero errors.
