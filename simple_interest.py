import sys
if len(sys.argv) != 4:
    print("ERROR: Please provide Principal, Rate of Interest, and Time as parameters.")
    print("Usage: python3 simple_interest.py <PRINCIPAL> <RATE> <TIME>")
    sys.exit(1)
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])
print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("Principal:", principal)
print("Rate of Interest:", rate)
print("Time:", time)
simple_interest = (principal * rate * time) / 100
print("\n===== RESULT =====")
print("Simple Interest:", simple_interest)
