"""Create a list of 5 favorite movies and print them using a loop.
Add a new movie to the list and remove one movie."""
movies=["Darling","Godavari","Radheshyam","Seeta Ramam","Julai"]
for i in movies:
    print(i)

movies.remove("Julai")
movies.append("Hridhayam")
print("Updated list of movies:",movies)