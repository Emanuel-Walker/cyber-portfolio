# Dashboard Panel Definitions

**BLUF.** Five panels. Every one is grouped by asset tier instead of by alert severity. If you cannot see tier anywhere on your dashboard, your team will keep working from severity because that is what the UI shows them.

---

## Panel 1 - SLA Conformance by Tier (7d)

**What it measures.** The percentage of alerts closed inside the tier's SLA, rolling 7 days.

**Why it's the top panel.** This is what the CISO sees first every morning. If Tier 1 SLA conformance is below 95% for three days running, that is a staffing or detection problem, not a tool problem.

**Thresholds.**
- Green: 95% or higher
- Orange: 90 to 95%
- Red: below 90%

**Query logic (PromQL style):**

```
100 * sum by (tier) (rate(soc_alerts_closed_in_sla_total[7d]))
    / sum by (tier) (rate(soc_alerts_closed_total[7d]))
```

Translate to your SIEM's query language. The counters you need:
- `soc_alerts_closed_total` - tagged by `tier`
- `soc_alerts_closed_in_sla_total` - same tag, incremented only when the alert closed before SLA breach

---

## Panel 2 - MTTD by Tier

**What it measures.** Time from alert fired to first human acknowledgment. P50 and P95, grouped by tier.

**Why it matters.** MTTD on Tier 1 should be under 15 minutes 95% of the time. If your P95 is 45 minutes, you are not catching anything in Tier 1. You are catching things late and calling it Tier 1.

**Why both P50 and P95.** P50 tells you the normal case. P95 tells you the tail. The tail is where real breaches hide.

**Query logic:**

```
histogram_quantile(0.50, sum by (tier, le) (rate(soc_mttd_seconds_bucket[1h])))
histogram_quantile(0.95, sum by (tier, le) (rate(soc_mttd_seconds_bucket[1h])))
```

Needs a histogram bucket metric. Most SIEMs do not emit this natively. You will have to compute it from alert lifecycle events.

---

## Panel 3 - MTTR by Tier

**What it measures.** Time from alert fired to incident closure. P50 and P95, grouped by tier.

**Why it matters.** MTTR is the number the executive team actually cares about. "How long before we were safe again." Tier 1 target is 2 hours. Tier 6 target is 24 hours. Tune to your business.

**Query logic:**

```
histogram_quantile(0.50, sum by (tier, le) (rate(soc_mttr_seconds_bucket[1h])))
histogram_quantile(0.95, sum by (tier, le) (rate(soc_mttr_seconds_bucket[1h])))
```

---

## Panel 4 - Queue Depth by Tier

**What it measures.** Current count of open alerts, grouped by tier.

**Why it matters.** If Tier 1 queue is greater than zero for more than 15 minutes, your on-call is late. If Tier 6 queue is greater than 500, your batch review is behind.

**Thresholds (Tier 1 to 5):**
- Green: 0
- Orange: 1 to 9
- Red: 10 or more

**Thresholds (Tier 6):**
- Green: under 100
- Orange: 100 to 499
- Red: 500 or more

Different thresholds per tier because Tier 6 is supposed to batch. A Tier 6 queue of 80 is normal. A Tier 1 queue of 2 is not.

**Query logic:**

```
sum by (tier) (soc_alerts_open_count)
```

---

## Panel 5 - False Positive Rate by Tier (24h)

**What it measures.** Percentage of closed alerts in each tier that were dispositioned as false positive, rolling 24 hours.

**Why it matters.** FP on Tier 1 is a detection engineering emergency. Every FP on Tier 1 burns on-call capacity you cannot replace during a shift. FP on Tier 6 is tolerable because the batch absorbs it.

**Thresholds:**
- Green: under 10%
- Orange: 10 to 29%
- Red: 30% or more

**Query logic:**

```
100 * sum by (tier) (rate(soc_alerts_fp_total[24h]))
    / sum by (tier) (rate(soc_alerts_closed_total[24h]))
```

---

## What you will NOT see on this dashboard

- Severity labels in any panel title or axis
- A panel called "P1 queue"
- A pie chart of alert categories
- A "security score" number with no definition behind it

Severity still exists in the underlying data. It is just not the organizing principle. The organizing principle is what the attacker is reaching for.

---

## Instrumentation notes

To make these panels work, your SIEM or alert platform needs to tag every alert with:

- `tier` (1 through 6, from the crown jewel scorer)
- `asset_id`
- `disposition` on close (true_positive, false_positive, benign_positive, duplicate)
- `created_at`, `acknowledged_at`, `closed_at` timestamps

If your SIEM does not tag alerts with `tier` at ingestion, bolt it on with a webhook or scheduled enrichment job that pulls the asset's tier from the crown jewel inventory and writes it back to the alert.
