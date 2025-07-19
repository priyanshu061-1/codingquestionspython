n = int(input())
movie_ids = list(map(int, input().split()))

frequency = {}

for movie_id in movie_ids:
    if movie_id in frequency:
        frequency[movie_id] += 1
    else:
        frequency[movie_id] = 1

# Print all frequencies
for movie_id in frequency:
    print(movie_id, frequency[movie_id])
6