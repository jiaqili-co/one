# Orbital periods (in days)
periods = [88, 225, 365.25]
omegas = [360 / p for p in periods]  # Angular velocities (degrees/day)

# Parameters
max_angle_diff = 1.0
max_days = 1000000

def angle_diff(a, b):  # Smallest angular difference between two angles
    return min(abs(a - b) % 360, 360 - abs(a - b) % 360)

def are_aligned(day):  # Check if planets align on a given day
    angles = sorted([(omega * day) % 360 for omega in omegas])
    diffs = [angle_diff(angles[i], angles[(i + 1) % 3]) for i in range(3)]
    return max(diffs) <= max_angle_diff

def find_alignment():  # Find first alignment day
    return next((day for day in range(1, max_days + 1) if are_aligned(day)), -1)

# Run the simulation
alignment_day = find_alignment()
print(f"The planets will align again after {alignment_day} days.")






