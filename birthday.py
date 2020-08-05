import random
from list_fns import has_duplicates

def random_sample(sample_size):
    t = []
    for i in range(sample_size):
        x = random.randint(1, 365)
        t.append(x)
    return t

def simulation(num_simulations, sample_size):
    count = 0
    for i in range(num_simulations):
        t = random_sample(sample_size)
        if has_duplicates(t):
            count += 1
    return count

num_simulations = 1000
sample_size = 23
count = simulation(num_simulations, sample_size)

print(f"{num_simulations} run with sample size {sample_size}")
print(f"A total of {count} matches were found.")
est = count / num_simulations * 100
print(f"So the estimated probability of matching birthdays is {est:.2f}%")
