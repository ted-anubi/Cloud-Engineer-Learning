#if/elif/else chains
threat_score = int(input("Enter a threat_score: "))
if threat_score >= 90:
    print("CRITICAL")

elif threat_score >= 70:
    print("HIGH")

elif threat_score >= 50:
    print("MEDIUM")

elif threat_score >= 1:
    print("LOW")

else:
    print("NO THREAT")