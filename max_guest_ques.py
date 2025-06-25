
def max_guests_on_cruise(E, L):
    current_guests = 0
    max_guests = 0

    for i in range(len(E)):
        current_guests += E[i] - L[i]
        if current_guests > max_guests:
            max_guests = current_guests

    return max_guests

# Example input
T = 5
E = [7, 0, 5, 1, 3]
L = [1, 2, 1, 3, 4]

# Function call
result = max_guests_on_cruise(E, L)
print("Maximum number of guests on cruise at an instance:", result)
