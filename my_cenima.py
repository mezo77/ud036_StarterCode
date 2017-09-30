import fresh_tomatoes
import media




#this creates an object of the Movie class and it contains info of the hobbit movie part one
hobbit_1 = media.Movie("The Hobbit: An Unexpected Journey (2012)",
"https://agcrump.files.wordpress.com/2012/12/the-hobbit-part-1-an-unexpected-journey-2012-movie-poster-e1348339281255.jpg",
"https://www.youtube.com/watch?v=SDnYMbYB-nU")

#this creates an object of the Movie class and it contains info of the hobbit movie part two
hobbit_2 = media.Movie("The Hobbit: The Desolation of Smaug (2013)", "https://vignette3.wikia.nocookie.net/lotr/images/f/f8/The-hobbit-the-desolation-of-smaug-poster.jpg/revision/latest?cb=20140227201637", "https://www.youtube.com/watch?v=fnaojlfdUbs")

#this creates an object of the Movie class and it contains info of the hobbit movie part three
hobbit_3 = media.Movie("The Hobbit: The Battle of the Five Armies (2014)",
 "https://images-na.ssl-images-amazon.com/images/M/MV5BODAzMDgxMDc1MF5BMl5BanBnXkFtZTgwMTI0OTAzMjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=iVAgTiBrrDA")


#this creates a Movie object and it containes info about the lord of the rings part 1 movie
the_lord_of_the_rings_1 = media.Movie("The Lord of the Rings: The Fellowship of the Ring (2001)",
   "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4&t=11s")

#this creates a Movie object and it containes info about the lord of the rings part 2 movie
the_lord_of_the_rings_2 = media.Movie("The Lord of the Rings: The Two Towers (2002)",
 "http://saint-epondyle.net/blog/wp-content/uploads/2012/12/clemburtonlesdeuxtours.jpg",
"https://www.youtube.com/watch?v=LbfMDwc4azU")

#this creates a Movie object and it containes info about the lord of the rings part 3 movie
the_lord_of_the_rings_3 = media.Movie("The Lord of the Rings: The Return of the King (2003)",
 "https://s-media-cache-ak0.pinimg.com/originals/8e/77/c3/8e77c3ceeede5d63ee0bfdc19408565b.jpg",
"https://www.youtube.com/watch?v=r5X-hFf6Bwo")

#this creats an object of the Movie class and it contains info of saving private ryan movie
saving_private = media.Movie("Saving Private Ryan (1998)", "http://is5.mzstatic.com/image/thumb/Video/v4/66/83/44/668344c7-a8fa-107c-72f9-b1fdceb226c6/source/1200x630bb.jpg",
"https://www.youtube.com/watch?v=zwhP5b4tD6g")

#this object holds info about enemy at the gate movie
enemy_at_the_gates = media.Movie("Enemy at the Gates (2001)",  "https://images-na.ssl-images-amazon.com/images/M/MV5BYWFlY2E3ODQtZWNiNi00ZGU4LTkzNWEtZTQ2ZTViMWRhYjIzL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY1200_CR87,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=4O-sMh_DO6I")

fury = media.Movie("Fury (2014)",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwMzQxMzY4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=DNHuK1rteF4")

the_shawshank = media.Movie("The Shawshank Redemption (1994)", "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")

mouse_hunt = media.Movie("Mousehunt (1997)","https://images-na.ssl-images-amazon.com/images/M/MV5BMzE0NTRhZWQtZmE5OS00NTI5LWJhMzMtMGU4MzE4MmRlZDE0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR92,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=zgjUMHGjO0k")

braveheart = media.Movie("Braveheart (1995)","https://www.movieposter.com/posters/archive/main/70/MPW-35017"
, "https://www.youtube.com/watch?v=wj0I8xVTV18")

the_fault_in_our_stars = media.Movie("The Fault in Our Stars (2014)","https://i.pinimg.com/736x/1b/af/9a/1baf9a7f2f5465428a5746f6b0eec4c7--star-crossed-hazel-and-augustus.jpg","https://www.youtube.com/watch?v=9ItBvH5J6ss")

me_before_you = media.Movie("Me Before You (2016)", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2NjE4NDE2NV5BMl5BanBnXkFtZTgwOTcwNDE5NzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=Eh993__rOxA")

collateral_beauty = media.Movie("Collateral Beauty (2016)", "https://www.movietard.com/wp-content/uploads/2017/03/Collateral-Beauty-2016.jpg", "https://www.youtube.com/watch?v=isQ5Ycie73U")


#this list holds all Movie objects
movies = [fury, saving_private,
enemy_at_the_gates,the_lord_of_the_rings_1,the_lord_of_the_rings_2,the_lord_of_the_rings_3,hobbit_1,hobbit_3, hobbit_2,
the_shawshank, mouse_hunt,braveheart, collateral_beauty,the_fault_in_our_stars, me_before_you]




fresh_tomatoes.open_movies_page(movies)
