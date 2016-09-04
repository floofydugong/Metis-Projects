**Project:** Luther

**Description:** Predicted a Movie's Domestic Box Office Gross in relation to the score given by the chief NY Times critic

# Problem Statement

I will be scraping A.O Scott critic data from rottentomatoes to see if there’s a relationship between the rating that he gives and the overall gross. Given his credentials, I would assume that A.O Scott would have a high influence on the amount that movie grosses over time. Rottentomatoes data is set up so that either a fresh or rotten rating can be given by a certified critic for a certain movie. With this in mind, I will track the data with "1" as indicating "Fresh" and "0" as indicating "Rotten"

The initial pulls from his critic page will include Title, Release Year, Critic Score, and the Movie's URL. From there, I will then loop through the movie urls to obtain run time and genere. The reason why I didn't pull more data was that I saw a lot of the fields were empty for a majority of the movies.

Because of the lack of information, I decided to search the BoxOfficeMojo database and left join the Studio,LifetimeGross,LifetimeTheaters,OpeningGross,OpeningTheaters,ReleaseYear.