A={'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Pulp Fiction'}
B={'The Matrix', 'Fight Club', 'Forrest Gump', 'Inception', 'The Shawshank Redemption'}

both_watched=A.intersection(B)
print("\nMovies watched by both users:")
print(both_watched)

unique_to_A=A.difference(B)
print("\nMovies unique to User A:")
print(unique_to_A)

sugestions_for_A=B.difference(A)
print("\nMovies to suggest to User A:")
print(sugestions_for_A)