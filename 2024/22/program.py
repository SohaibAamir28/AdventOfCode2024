def generate_next_secret(secret_number):
    secret_number ^= (secret_number * 64) % 16777216
    secret_number %= 16777216
    secret_number ^= (secret_number // 32) % 16777216
    secret_number %= 16777216
    secret_number ^= (secret_number * 2048) % 16777216
    secret_number %= 16777216
    return secret_number

def get_price_sequence(initial_secret):
    # Generate all prices at once
    prices = []
    secret = initial_secret
    for _ in range(2001):  # We need 2001 to get 2000 changes
        prices.append(secret % 10)
        secret = generate_next_secret(secret)
    return prices

def find_sequences(prices):
    # Create a dictionary to store where each sequence appears and its corresponding price
    sequences = {}
    changes = []
    
    # Calculate all changes
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])
    
    # For each position, record the 4-change sequence that starts there
    for i in range(len(changes) - 3):
        seq = tuple(changes[i:i+4])  # Convert to tuple so it can be used as dict key
        if seq not in sequences:  # Only keep the first occurrence
            sequences[seq] = prices[i+4]
            
    return sequences

def main():
    with open("2024/22/input.txt", "r") as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]
    
    # Pre-calculate all sequences for each buyer
    buyer_sequences = []
    for secret in initial_secrets:
        prices = get_price_sequence(secret)
        sequences = find_sequences(prices)
        buyer_sequences.append(sequences)
    
    # Find the sequence that appears in most buyers with highest total
    best_total = 0
    best_sequence = None
    
    # Get all unique sequences that appear in any buyer's data
    all_sequences = set()
    for sequences in buyer_sequences:
        all_sequences.update(sequences.keys())
    
    # Check each sequence that actually appears in the data
    for seq in all_sequences:
        total = sum(sequences.get(seq, 0) for sequences in buyer_sequences)
        if total > best_total:
            best_total = total
            best_sequence = seq
    
    print(f"Best sequence: {list(best_sequence)}")
    print(f"Maximum bananas: {best_total}")

if __name__ == "__main__":
    main()

# def generate_2000th_secret(initial_secret):
#     MODULO = 16777216  # 2^24

#     secret = initial_secret
#     for _ in range(2000):
#         # Step 1: Multiply by 64 and mix
#         secret = (secret ^ (secret * 64)) % MODULO

#         # Step 2: Divide by 32 (floor) and mix
#         secret = (secret ^ (secret // 32)) % MODULO

#         # Step 3: Multiply by 2048 and mix
#         secret = (secret ^ (secret * 2048)) % MODULO

#     return secret

# def sum_of_2000th_secrets(input_numbers):
#     total_sum = 0
#     for initial_secret in input_numbers:
#         total_sum += generate_2000th_secret(initial_secret)
#     return total_sum

# # Read input from file
# with open("2024/22/input.txt", "r") as file:
#     input_numbers = [int(line.strip()) for line in file.readlines()]

# # Calculate the sum of the 2000th secret numbers
# result = sum_of_2000th_secrets(input_numbers)
# print("Sum of the 2000th secret numbers:", result)

# # Sum of the 2000th secret numbers: 12664695565