# Network Security Operations

**Status: Draft**

## Architecture

**NSO = NSM + NTA + NDR**

```text
Network Activity --NSM--> Network Telemetry --NTA--> Network Evidence --NDR--> Security Action
```

### Network Security Monitoring (NSM)

1. Capture & Collect
2. Transform & Record
3. Store & Retrieve

### Network Telemetry Analytics (NTA)

1. Select
2. Compare
3. Correlate
4. Aggregate
5. Calculate
6. Present

### Network Detection & Response (NDR)

1. Detection
2. Investigation
3. Response

This working architecture distinguishes the collection of telemetry, derivation of evidence, and security operations informed by that evidence.
