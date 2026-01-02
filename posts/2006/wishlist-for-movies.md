---
title: Wishlist for movies
date: "2006-12-18T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 160
---

I watch a lot of movies. Over the last year, I've watched over 250 movies (and read 50 books, but that's another story). Other than making time to watch movies, **my biggest problem is figuring out what to watch next**.

The [IMDb top 250](http://www.imdb.com/chart/top) is a good guideline, and I'm running my way down the list. [Twofifty.org](http://twofifty.org) has been useful to track what I've seen as well. But I have interests outside of the IMDb Top 250, and **I need a way of tracking these**.

I started a "to watch" Excel sheet. But there were three problems:

1. I would forget what the movie was about
2. I wouldn't know what to watch next
3. I'd have to manually delete movies I'd seen

So **I wrote a program to do this automatically** and create a movie wishlist. I just write the names of movies I want to see, and the program finds these movies on IMDb, gets their ratings and links them. It also goes through my "seen" movies and strikes out stuff I've seen.

So I can just click on the movie to see what it's about. I can sort by rating or votes to decide what to see next. And I don't have to manually strike out anything.

These are the movies I want to see.

## IMDb Top 250

> Movies from the IMDb Top 250. You can track movies you've seen on this list at 250.s-anand.net.

| Rating | Votes  | Year | Name                                                                                                         |
| ------ | ------ | ---- | ------------------------------------------------------------------------------------------------------------ |
| 9.1    | 184462 | 1972 | [The Godfather](http://www.imdb.com/title/tt0068646/)                                                        |
| 9.1    | 222355 | 1994 | [The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)                                             |
| 8.9    | 104446 | 1974 | [The Godfather: Part II](http://www.imdb.com/title/tt0071562/)                                               |
| 8.8    | 167348 | 2003 | [The Lord of the Rings: The Return of the King](http://www.imdb.com/title/tt0167260/)                        |
| 8.8    | 51126  | 1966 | [Buono, il brutto, il cattivo, Il](http://www.imdb.com/title/tt0060196/)                                     |
| 8.8    | 89621  | 1942 | [Casablanca](http://www.imdb.com/title/tt0034583/)                                                           |
| 8.8    | 133063 | 1993 | [Schindler's List](http://www.imdb.com/title/tt0108052/)                                                     |
| 8.7    | 189910 | 1994 | [Pulp Fiction](http://www.imdb.com/title/tt0110912/)                                                         |
| 8.7    | 48352  | 1954 | [Shichinin no samurai](http://www.imdb.com/title/tt0047478/)                                                 |
| 8.7    | 142585 | 1980 | [Star Wars: Episode V - The Empire Strikes Back](http://www.imdb.com/title/tt0080684/)                       |
| 8.7    | 179427 | 1977 | [Star Wars](http://www.imdb.com/title/tt0076759/)                                                            |
| 8.7    | 96495  | 1975 | [One Flew Over the Cuckoo's Nest](http://www.imdb.com/title/tt0073486/)                                      |
| 8.7    | 56917  | 1954 | [Rear Window](http://www.imdb.com/title/tt0047396/)                                                          |
| 8.7    | 210181 | 2001 | [The Lord of the Rings: The Fellowship of the Ring](http://www.imdb.com/title/tt0120737/)                    |
| 8.6    | 42912  | 1957 | [12 Angry Men](http://www.imdb.com/title/tt0050083/)                                                         |
| 8.6    | 122980 | 1981 | [Raiders of the Lost Ark](http://www.imdb.com/title/tt0082971/)                                              |
| 8.6    | 139737 | 1995 | [The Usual Suspects](http://www.imdb.com/title/tt0114814/)                                                   |
| 8.6    | 53478  | 2002 | [Cidade de Deus](http://www.imdb.com/title/tt0317248/)                                                       |
| 8.6    | 85885  | 1964 | [Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb](http://www.imdb.com/title/tt0057012/) |
| 8.6    | 165925 | 2002 | [The Lord of the Rings: The Two Towers](http://www.imdb.com/title/tt0167261/)                                |
| 8.6    | 72218  | 1960 | [Psycho](http://www.imdb.com/title/tt0054215/)                                                               |
| 8.6    | 97798  | 1990 | [Goodfellas](http://www.imdb.com/title/tt0099685/)                                                           |
| 8.6    | 79898  | 1941 | [Citizen Kane](http://www.imdb.com/title/tt0033467/)                                                         |
| 8.6    | 28071  | 1968 | [C'era una volta il West](http://www.imdb.com/title/tt0064116/)                                              |
| 8.6    | 48162  | 1959 | [North by Northwest](http://www.imdb.com/title/tt0053125/)                                                   |
| 8.6    | 128067 | 2000 | [Memento](http://www.imdb.com/title/tt0209144/)                                                              |
| 8.5    | 121934 | 1991 | [The Silence of the Lambs](http://www.imdb.com/title/tt0102926/)                                             |
| 8.5    | 41966  | 1962 | [Lawrence of Arabia](http://www.imdb.com/title/tt0056172/)                                                   |
| 8.5    | 54159  | 1946 | [It's a Wonderful Life](http://www.imdb.com/title/tt0038650/)                                                |
| 8.5    | 23989  | 1950 | [Sunset Blvd.](http://www.imdb.com/title/tt0043014/)                                                         |
| 8.5    | 87688  | 2001 | [Fabuleux destin d'Amélie Poulain, Le](http://www.imdb.com/title/tt0211915/)                                 |
| 8.5    | 164764 | 1999 | [Fight Club](http://www.imdb.com/title/tt0137523/)                                                           |
| 8.5    | 147050 | 1999 | [American Beauty](http://www.imdb.com/title/tt0169547/)                                                      |
| 8.5    | 192905 | 1999 | [The Matrix](http://www.imdb.com/title/tt0133093/)                                                           |
| 8.5    | 46127  | 1958 | [Vertigo](http://www.imdb.com/title/tt0052357/)                                                              |
| 8.4    | 88542  | 1979 | [Apocalypse Now](http://www.imdb.com/title/tt0078788/)                                                       |
| 8.4    | 67656  | 1976 | [Taxi Driver](http://www.imdb.com/title/tt0075314/)                                                          |
| 8.4    | 88315  | 2004 | [Eternal Sunshine of the Spotless Mind](http://www.imdb.com/title/tt0338013/)                                |
| 8.4    | 124843 | 1995 | [Se7en](http://www.imdb.com/title/tt0114369/)                                                                |
| 8.4    | 20663  | 1957 | [Paths of Glory](http://www.imdb.com/title/tt0050825/)                                                       |
| 8.4    | 79502  | 1994 | [Léon](http://www.imdb.com/title/tt0110413/)                                                                 |
| 8.4    | 42176  | 1962 | [To Kill a Mockingbird](http://www.imdb.com/title/tt0056592/)                                                |
| 8.4    | 36284  | 1974 | [Chinatown](http://www.imdb.com/title/tt0071315/)                                                            |
| 8.4    | 90124  | 1998 | [American History X](http://www.imdb.com/title/tt0120586/)                                                   |
| 8.4    | 28044  | 2004 | [Untergang, Der](http://www.imdb.com/title/tt0363163/)                                                       |
| 8.4    | 25776  | 1949 | [The Third Man](http://www.imdb.com/title/tt0041959/)                                                        |
| 8.4    | 50593  | 2002 | [The Pianist](http://www.imdb.com/title/tt0253474/)                                                          |
| 8.3    | 83635  | 1975 | [Monty Python and the Holy Grail](http://www.imdb.com/title/tt0071853/)                                      |
| 8.3    | 17778  | 1931 | [M](http://www.imdb.com/title/tt0022100/)                                                                    |
| 8.3    | 14759  | 1948 | [The Treasure of the Sierra Madre](http://www.imdb.com/title/tt0040897/)                                     |
| 8.3    | 38774  | 1981 | [Boot, Das](http://www.imdb.com/title/tt0082096/)                                                            |
| 8.3    | 41643  | 2001 | [Sen to Chihiro no kamikakushi](http://www.imdb.com/title/tt0245429/)                                        |
| 8.3    | 30184  | 1957 | [The Bridge on the River Kwai](http://www.imdb.com/title/tt0050212/)                                         |
| 8.3    | 90722  | 1997 | [L.A. Confidential](http://www.imdb.com/title/tt0119488/)                                                    |
| 8.3    | 85925  | 1979 | [Alien](http://www.imdb.com/title/tt0078748/)                                                                |
| 8.3    | 26448  | 1941 | [The Maltese Falcon](http://www.imdb.com/title/tt0033870/)                                                   |
| 8.3    | 90761  | 1971 | [A Clockwork Orange](http://www.imdb.com/title/tt0066921/)                                                   |
| 8.3    | 75787  | 2000 | [Requiem for a Dream](http://www.imdb.com/title/tt0180093/)                                                  |
| 8.3    | 31146  | 2004 | [Hotel Rwanda](http://www.imdb.com/title/tt0395169/)                                                         |
| 8.3    | 17544  | 1927 | [Metropolis](http://www.imdb.com/title/tt0017136/)                                                           |
| 8.3    | 73473  | 1980 | [The Shining](http://www.imdb.com/title/tt0081505/)                                                          |
| 8.3    | 16538  | 1944 | [Double Indemnity](http://www.imdb.com/title/tt0036775/)                                                     |
| 8.3    | 97378  | 1992 | [Reservoir Dogs](http://www.imdb.com/title/tt0105236/)                                                       |
| 8.3    | 134982 | 1998 | [Saving Private Ryan](http://www.imdb.com/title/tt0120815/)                                                  |
| 8.3    | 27965  | 1952 | [Singin' in the Rain](http://www.imdb.com/title/tt0045152/)                                                  |
| 8.3    | 17350  | 1950 | [Rashômon](http://www.imdb.com/title/tt0042876/)                                                             |
| 8.3    | 94965  | 2005 | [Sin City](http://www.imdb.com/title/tt0401792/)                                                             |
| 8.3    | 39024  | 1980 | [Raging Bull](http://www.imdb.com/title/tt0081398/)                                                          |
| 8.3    | 15107  | 1936 | [Modern Times](http://www.imdb.com/title/tt0027977/)                                                         |
| 8.3    | 19253  | 1962 | [The Manchurian Candidate](http://www.imdb.com/title/tt0056218/)                                             |
| 8.3    | 84850  | 1986 | [Aliens](http://www.imdb.com/title/tt0090605/)                                                               |
| 8.3    | 16306  | 1940 | [Rebecca](http://www.imdb.com/title/tt0032976/)                                                              |
| 8.2    | 28511  | 1963 | [The Great Escape](http://www.imdb.com/title/tt0057115/)                                                     |
| 8.2    | 34487  | 1959 | [Some Like It Hot](http://www.imdb.com/title/tt0053291/)                                                     |
| 8.2    | 17935  | 1950 | [All About Eve](http://www.imdb.com/title/tt0042192/)                                                        |
| 8.2    | 16059  | 1958 | [Touch of Evil](http://www.imdb.com/title/tt0052311/)                                                        |
| 8.2    | 41966  | 2006 | [The Departed](http://www.imdb.com/title/tt0407887/)                                                         |
| 8.2    | 52849  | 2004 | [Million Dollar Baby](http://www.imdb.com/title/tt0405159/)                                                  |
| 8.2    | 85137  | 1968 | [2001: A Space Odyssey](http://www.imdb.com/title/tt0062622/)                                                |
| 8.2    | 49539  | 1984 | [Amadeus](http://www.imdb.com/title/tt0086879/)                                                              |
| 8.2    | 14918  | 1957 | [Sjunde inseglet, Det](http://www.imdb.com/title/tt0050976/)                                                 |
| 8.2    | 51923  | 1997 | [Vita è bella, La](http://www.imdb.com/title/tt0118799/)                                                     |
| 8.2    | 65784  | 1975 | [Jaws](http://www.imdb.com/title/tt0073195/)                                                                 |
| 8.2    | 32450  | 1973 | [The Sting](http://www.imdb.com/title/tt0070735/)                                                            |
| 8.2    | 15343  | 1951 | [Strangers on a Train](http://www.imdb.com/title/tt0044079/)                                                 |
| 8.2    | 128564 | 1994 | [Forrest Gump](http://www.imdb.com/title/tt0109830/)                                                         |
| 8.2    | 97414  | 2005 | [Batman Begins](http://www.imdb.com/title/tt0372784/)                                                        |
| 8.2    | 104569 | 1991 | [Terminator 2: Judgment Day](http://www.imdb.com/title/tt0103064/)                                           |
| 8.2    | 18649  | 1954 | [On the Waterfront](http://www.imdb.com/title/tt0047296/)                                                    |
| 8.2    | 16240  | 1939 | [Mr. Smith Goes to Washington](http://www.imdb.com/title/tt0031679/)                                         |
| 8.2    | 51662  | 1939 | [The Wizard of Oz](http://www.imdb.com/title/tt0032138/)                                                     |
| 8.2    | 123256 | 1995 | [Braveheart](http://www.imdb.com/title/tt0112573/)                                                           |
| 8.2    | 100529 | 2003 | [Kill Bill: Vol. 1](http://www.imdb.com/title/tt0266697/)                                                    |
| 8.2    | 58991  | 2004 | [The Incredibles](http://www.imdb.com/title/tt0317705/)                                                      |
| 8.2    | 96362  | 1982 | [Blade Runner](http://www.imdb.com/title/tt0083658/)                                                         |
| 8.2    | 23828  | 1980 | [The Elephant Man](http://www.imdb.com/title/tt0080678/)                                                     |
| 8.2    | 67115  | 1987 | [Full Metal Jacket](http://www.imdb.com/title/tt0093058/)                                                    |
| 8.2    | 15854  | 1960 | [The Apartment](http://www.imdb.com/title/tt0053604/)                                                        |
| 8.2    | 14094  | 1946 | [The Big Sleep](http://www.imdb.com/title/tt0038355/)                                                        |
| 8.2    | 14985  | 1946 | [Notorious](http://www.imdb.com/title/tt0038787/)                                                            |
| 8.2    | 11295  | 1931 | [City Lights](http://www.imdb.com/title/tt0021749/)                                                          |
| 8.2    | 16974  | 1952 | [High Noon](http://www.imdb.com/title/tt0044706/)                                                            |
| 8.2    | 20215  | 1988 | [Nuovo cinema Paradiso](http://www.imdb.com/title/tt0095765/)                                                |
| 8.2    | 88881  | 2001 | [Donnie Darko](http://www.imdb.com/title/tt0246578/)                                                         |
| 8.2    | 85567  | 1996 | [Fargo](http://www.imdb.com/title/tt0116282/)                                                                |
| 8.1    | 17257  | 1985 | [Ran](http://www.imdb.com/title/tt0089881/)                                                                  |
| 8.2    | 70672  | 2004 | [Crash](http://www.imdb.com/title/tt0375679/)                                                                |
| 8.1    | 65782  | 2003 | [Finding Nemo](http://www.imdb.com/title/tt0266543/)                                                         |
| 8.1    | 113151 | 1983 | [Star Wars: Episode VI - Return of the Jedi](http://www.imdb.com/title/tt0086190/)                           |
| 8.1    | 15524  | 1940 | [The Great Dictator](http://www.imdb.com/title/tt0032553/)                                                   |
| 8.1    | 29150  | 1984 | [Once Upon a Time in America](http://www.imdb.com/title/tt0087843/)                                          |
| 8.1    | 19982  | 1967 | [Cool Hand Luke](http://www.imdb.com/title/tt0061512/)                                                       |
| 8.1    | 29393  | 1997 | [Mononoke-hime](http://www.imdb.com/title/tt0119698/)                                                        |
| 8.1    | 4971   | 1953 | [Salaire de la peur, Le](http://www.imdb.com/title/tt0046268/)                                               |
| 8.1    | 128380 | 1999 | [The Sixth Sense](http://www.imdb.com/title/tt0167404/)                                                      |
| 8.1    | 71598  | 2005 | [V for Vendetta](http://www.imdb.com/title/tt0434409/)                                                       |
| 8.1    | 42862  | 1992 | [Unforgiven](http://www.imdb.com/title/tt0105695/)                                                           |
| 8.1    | 82116  | 1989 | [Indiana Jones and the Last Crusade](http://www.imdb.com/title/tt0097576/)                                   |
| 8.1    | 74045  | 2004 | [Kill Bill: Vol. 2](http://www.imdb.com/title/tt0378194/)                                                    |
| 8.1    | 28501  | 1959 | [Ben-Hur](http://www.imdb.com/title/tt0052618/)                                                              |
| 8.1    | 30306  | 1977 | [Annie Hall](http://www.imdb.com/title/tt0075686/)                                                           |
| 8.1    | 94218  | 1985 | [Back to the Future](http://www.imdb.com/title/tt0088763/)                                                   |
| 8.1    | 29692  | 2003 | [Oldboy](http://www.imdb.com/title/tt0364569/)                                                               |
| 8.1    | 66145  | 2000 | [Wo hu cang long](http://www.imdb.com/title/tt0190332/)                                                      |
| 8.1    | 10398  | 1956 | [The Killing](http://www.imdb.com/title/tt0049406/)                                                          |
| 8.1    | 46140  | 1979 | [Life of Brian](http://www.imdb.com/title/tt0079470/)                                                        |
| 8.1    | 13435  | 1961 | [Yojimbo](http://www.imdb.com/title/tt0055630/)                                                              |
| 8.1    | 70896  | 1987 | [The Princess Bride](http://www.imdb.com/title/tt0093779/)                                                   |
| 8.1    | 86551  | 1999 | [The Green Mile](http://www.imdb.com/title/tt0120689/)                                                       |
| 8      | 40031  | 1978 | [The Deer Hunter](http://www.imdb.com/title/tt0077416/)                                                      |
| 8      | 3949   | 1957 | [Notti di Cabiria, Le](http://www.imdb.com/title/tt0050783/)                                                 |
| 8      | 49695  | 1986 | [Platoon](http://www.imdb.com/title/tt0091763/)                                                              |
| 8      | 38832  | 1967 | [The Graduate](http://www.imdb.com/title/tt0061722/)                                                         |
| 8      | 11218  | 1934 | [It Happened One Night](http://www.imdb.com/title/tt0025316/)                                                |
| 8      | 27831  | 1969 | [Butch Cassidy and the Sundance Kid](http://www.imdb.com/title/tt0064115/)                                   |
| 8      | 14890  | 1965 | [Per qualche dollaro in più](http://www.imdb.com/title/tt0059578/)                                           |
| 8      | 128183 | 2000 | [Gladiator](http://www.imdb.com/title/tt0172495/)                                                            |
| 8      | 5469   | 1949 | [Kind Hearts and Coronets](http://www.imdb.com/title/tt0041546/)                                             |
| 8      | 18306  | 1951 | [The African Queen](http://www.imdb.com/title/tt0043265/)                                                    |
| 8      | 22068  | 1982 | [Gandhi](http://www.imdb.com/title/tt0083987/)                                                               |
| 8      | 24537  | 2000 | [Amores perros](http://www.imdb.com/title/tt0245712/)                                                        |
| 8      | 55368  | 1999 | [Toy Story 2](http://www.imdb.com/title/tt0120363/)                                                          |
| 8      | 10971  | 1948 | [Ladri di biciclette](http://www.imdb.com/title/tt0040522/)                                                  |
| 8      | 10525  | 1938 | [The Adventures of Robin Hood](http://www.imdb.com/title/tt0029843/)                                         |
| 8      | 4339   | 1966 | [Battaglia di Algeri, La](http://www.imdb.com/title/tt0058946/)                                              |
| 8      | 5198   | 1955 | [Diaboliques, Les](http://www.imdb.com/title/tt0046911/)                                                     |
| 8      | 8785   | 1943 | [Shadow of a Doubt](http://www.imdb.com/title/tt0036342/)                                                    |
| 8      | 12066  | 1963 | [8½](http://www.imdb.com/title/tt0056801/)                                                                   |
| 8      | 44522  | 1998 | [Lola rennt](http://www.imdb.com/title/tt0130827/)                                                           |
| 8      | 4657   | 1945 | [Brief Encounter](http://www.imdb.com/title/tt0037558/)                                                      |
| 8      | 11097  | 1955 | [The Night of the Hunter](http://www.imdb.com/title/tt0048424/)                                              |
| 8      | 14968  | 1969 | [The Wild Bunch](http://www.imdb.com/title/tt0065214/)                                                       |
| 8      | 42667  | 1986 | [Stand by Me](http://www.imdb.com/title/tt0092005/)                                                          |
| 8      | 14680  | 1974 | [The Conversation](http://www.imdb.com/title/tt0071360/)                                                     |
| 8      | 9327   | 1927 | [The General](http://www.imdb.com/title/tt0017925/)                                                          |
| 8      | 8405   | 1957 | [Smultronstället](http://www.imdb.com/title/tt0050986/)                                                      |
| 8      | 79214  | 1988 | [Die Hard](http://www.imdb.com/title/tt0095016/)                                                             |
| 8      | 10873  | 1950 | [Harvey](http://www.imdb.com/title/tt0042546/)                                                               |
| 8      | 13632  | 1933 | [Duck Soup](http://www.imdb.com/title/tt0023969/)                                                            |
| 8      | 22845  | 1975 | [Dog Day Afternoon](http://www.imdb.com/title/tt0072890/)                                                    |
| 8      | 12634  | 1922 | [Nosferatu, eine Symphonie des Grauens](http://www.imdb.com/title/tt0013442/)                                |
| 8      | 19894  | 1970 | [Patton](http://www.imdb.com/title/tt0066206/)                                                               |
| 8      | 28779  | 1989 | [Glory](http://www.imdb.com/title/tt0097441/)                                                                |
| 8      | 14235  | 1951 | [The Day the Earth Stood Still](http://www.imdb.com/title/tt0043456/)                                        |
| 8      | 6339   | 1920 | [Cabinet des Dr. Caligari., Das](http://www.imdb.com/title/tt0010323/)                                       |
| 7.9    | 39670  | 1939 | [Gone with the Wind](http://www.imdb.com/title/tt0031381/)                                                   |
| 7.9    | 39526  | 2002 | [Ying xiong](http://www.imdb.com/title/tt0299977/)                                                           |
| 7.9    | 23629  | 1960 | [Spartacus](http://www.imdb.com/title/tt0054331/)                                                            |
| 7.9    | 62267  | 1993 | [Groundhog Day](http://www.imdb.com/title/tt0107048/)                                                        |
| 7.9    | 39383  | 2004 | [Finding Neverland](http://www.imdb.com/title/tt0308644/)                                                    |
| 7.9    | 61792  | 1995 | [Toy Story](http://www.imdb.com/title/tt0114709/)                                                            |
| 7.9    | 3925   | 1946 | [Belle et la bête, La](http://www.imdb.com/title/tt0038348/)                                                 |
| 7.9    | 71725  | 1996 | [Trainspotting](http://www.imdb.com/title/tt0117951/)                                                        |
| 7.9    | 9082   | 1925 | [The Gold Rush](http://www.imdb.com/title/tt0015864/)                                                        |
| 7.9    | 14380  | 1940 | [The Philadelphia Story](http://www.imdb.com/title/tt0032904/)                                               |
| 7.9    | 63539  | 1999 | [Magnolia](http://www.imdb.com/title/tt0175880/)                                                             |
| 7.9    | 48051  | 1973 | [The Exorcist](http://www.imdb.com/title/tt0070047/)                                                         |
| 7.9    | 27304  | 1983 | [A Christmas Story](http://www.imdb.com/title/tt0085334/)                                                    |
| 7.9    | 10956  | 1940 | [The Grapes of Wrath](http://www.imdb.com/title/tt0032551/)                                                  |
| 7.9    | 47185  | 2003 | [Mystic River](http://www.imdb.com/title/tt0327056/)                                                         |
| 7.9    | 73754  | 1998 | [The Big Lebowski](http://www.imdb.com/title/tt0118715/)                                                     |
| 7.9    | 90560  | 2001 | [Shrek](http://www.imdb.com/title/tt0126029/)                                                                |
| 7.9    | 25035  | 2005 | [Cinderella Man](http://www.imdb.com/title/tt0352248/)                                                       |
| 7.9    | 55120  | 2003 | [Big Fish](http://www.imdb.com/title/tt0319061/)                                                             |
| 7.9    | 19395  | 2004 | [Before Sunset](http://www.imdb.com/title/tt0381681/)                                                        |
| 7.9    | 83678  | 1995 | [Twelve Monkeys](http://www.imdb.com/title/tt0114746/)                                                       |
| 7.9    | 64508  | 1995 | [Heat](http://www.imdb.com/title/tt0113277/)                                                                 |
| 7.9    | 17702  | 1933 | [King Kong](http://www.imdb.com/title/tt0024216/)                                                            |
| 7.9    | 5399   | 1961 | [Judgment at Nuremberg](http://www.imdb.com/title/tt0055031/)                                                |
| 7.9    | 33275  | 1994 | [Ed Wood](http://www.imdb.com/title/tt0109707/)                                                              |
| 7.9    | 11628  | 1961 | [The Hustler](http://www.imdb.com/title/tt0054997/)                                                          |
| 7.9    | 18639  | 2005 | [Wallace & Gromit in The Curse of the Were-Rabbit](http://www.imdb.com/title/tt0312004/)                     |
| 7.9    | 4284   | 1947 | [Out of the Past](http://www.imdb.com/title/tt0039689/)                                                      |
| 7.9    | 6894   | 1938 | [The Lady Vanishes](http://www.imdb.com/title/tt0030341/)                                                    |
| 7.9    | 8491   | 1946 | [The Best Years of Our Lives](http://www.imdb.com/title/tt0036868/)                                          |
| 7.9    | 80411  | 1984 | [The Terminator](http://www.imdb.com/title/tt0088247/)                                                       |
| 7.9    | 35489  | 2005 | [Walk the Line](http://www.imdb.com/title/tt0358273/)                                                        |
| 7.9    | 7168   | 1935 | [Bride of Frankenstein](http://www.imdb.com/title/tt0026138/)                                                |
| 7.9    | 68102  | 2000 | [Snatch.](http://www.imdb.com/title/tt0208092/)                                                              |
| 7.9    | 10110  | 1967 | [In the Heat of the Night](http://www.imdb.com/title/tt0061811/)                                             |
| 7.9    | 6578   | 1972 | [Sleuth](http://www.imdb.com/title/tt0069281/)                                                               |
| 7.9    | 10025  | 1953 | [Stalag 17](http://www.imdb.com/title/tt0046359/)                                                            |
| 7.9    | 12599  | 1988 | [Hotaru no haka](http://www.imdb.com/title/tt0095327/)                                                       |
| 7.9    | 2851   | 1955 | [Du rififi chez les hommes](http://www.imdb.com/title/tt0048021/)                                            |
| 7.9    | 3138   | 1963 | [Tengoku to jigoku](http://www.imdb.com/title/tt0057565/)                                                    |
| 7.9    | 30458  | 1974 | [Young Frankenstein](http://www.imdb.com/title/tt0072431/)                                                   |
| 7.9    | 19629  | 2002 | [Hable con ella](http://www.imdb.com/title/tt0287467/)                                                       |
| 7.9    | 17937  | 1967 | [Bonnie and Clyde](http://www.imdb.com/title/tt0061418/)                                                     |
| 7.9    | 20784  | 1999 | [The Straight Story](http://www.imdb.com/title/tt0166896/)                                                   |
| 7.9    | 27961  | 1982 | [The Thing](http://www.imdb.com/title/tt0084787/)                                                            |
| 7.9    | 5523   | 1957 | [Kumonosu jô](http://www.imdb.com/title/tt0050613/)                                                          |
| 7.9    | 17362  | 1979 | [Manhattan](http://www.imdb.com/title/tt0079522/)                                                            |
| 7.9    | 9798   | 1959 | [Quatre cents coups, Les](http://www.imdb.com/title/tt0053198/)                                              |
| 7.9    | 26699  | 1996 | [Sling Blade](http://www.imdb.com/title/tt0117666/)                                                          |
| 7.9    | 2500   | 1985 | [Idi i smotri](http://www.imdb.com/title/tt0091251/)                                                         |
| 7.9    | 19071  | 1968 | [Rosemary's Baby](http://www.imdb.com/title/tt0063522/)                                                      |
| 7.9    | 50785  | 1998 | [Lock, Stock and Two Smoking Barrels](http://www.imdb.com/title/tt0120735/)                                  |
| 7.9    | 9863   | 1931 | [Frankenstein](http://www.imdb.com/title/tt0021884/)                                                         |
| 7.9    | 7344   | 1957 | [Witness for the Prosecution](http://www.imdb.com/title/tt0051201/)                                          |
| 7.9    | 5931   | 1959 | [Anatomy of a Murder](http://www.imdb.com/title/tt0052561/)                                                  |
| 7.9    | 15382  | 1944 | [Arsenic and Old Lace](http://www.imdb.com/title/tt0036613/)                                                 |
| 7.9    | 55431  | 2001 | [Monsters, Inc.](http://www.imdb.com/title/tt0198781/)                                                       |
| 7.9    | 51862  | 1983 | [Scarface](http://www.imdb.com/title/tt0086250/)                                                             |
| 7.9    | 4368   | 1945 | [The Lost Weekend](http://www.imdb.com/title/tt0037884/)                                                     |
| 7.9    | 9878   | 1930 | [All Quiet on the Western Front](http://www.imdb.com/title/tt0020629/)                                       |
| 7.9    | 103979 | 2003 | [Pirates of the Caribbean: The Curse of the Black Pearl](http://www.imdb.com/title/tt0325980/)               |
| 7.9    | 13597  | 1953 | [Roman Holiday](http://www.imdb.com/title/tt0046250/)                                                        |
| 7.8    | 10291  | 1962 | [The Man Who Shot Liberty Valance](http://www.imdb.com/title/tt0056217/)                                     |
| 7.8    | 14367  | 1956 | [The Searchers](http://www.imdb.com/title/tt0049730/)                                                        |
| 7.8    | 9651   | 1995 | [Haine, La](http://www.imdb.com/title/tt0113247/)                                                            |
| 7.8    | 17450  | 2006 | [The Prestige](http://www.imdb.com/title/tt0482571/)                                                         |
| 7.8    | 14644  | 1965 | [Doctor Zhivago](http://www.imdb.com/title/tt0059113/)                                                       |
| 7.8    | 10117  | 1987 | [Himmel über Berlin, Der](http://www.imdb.com/title/tt0093191/)                                              |
| 7.8    | 12756  | 1938 | [Bringing Up Baby](http://www.imdb.com/title/tt0029947/)                                                     |
| 7.8    | 41725  | 1985 | [Brazil](http://www.imdb.com/title/tt0088846/)                                                               |
| 7.8    | 6755   | 1972 | [Aguirre, der Zorn Gottes](http://www.imdb.com/title/tt0068182/)                                             |
| 7.8    | 2934   | 1943 | [The Ox-Bow Incident](http://www.imdb.com/title/tt0036244/)                                                  |
| 7.8    | 14248  | 1951 | [A Streetcar Named Desire](http://www.imdb.com/title/tt0044081/)                                             |
| 7.8    | 28118  | 1968 | [Planet of the Apes](http://www.imdb.com/title/tt0063442/)                                                   |
| 7.8    | 3709   | 1969 | [Z](http://www.imdb.com/title/tt0065234/)                                                                    |
| 7.8    | 13300  | 1971 | [Harold and Maude](http://www.imdb.com/title/tt0067185/)                                                     |
| 7.8    | 2485   | 1952 | [Umberto D.](http://www.imdb.com/title/tt0045274/)                                                           |
| 7.8    | 11329  | 1954 | [Dial M for Murder](http://www.imdb.com/title/tt0046912/)                                                    |
| 7.8    | 6930   | 1952 | [Ikiru](http://www.imdb.com/title/tt0044741/)                                                                |
| 7.8    | 5368   | 1960 | [Inherit the Wind](http://www.imdb.com/title/tt0053946/)                                                     |
| 7.8    | 18010  | 1976 | [All the President's Men](http://www.imdb.com/title/tt0074119/)                                              |
| 7.8    | 10957  | 2001 | [No Man's Land](http://www.imdb.com/title/tt0283509/)                                                        |
| 7.8    | 11178  | 1975 | [The Man Who Would Be King](http://www.imdb.com/title/tt0073341/)                                            |
| 7.8    | 9683   | 1940 | [His Girl Friday](http://www.imdb.com/title/tt0032599/)                                                      |
| 7.8    | 4079   | 1967 | [In Cold Blood](http://www.imdb.com/title/tt0061809/)                                                        |

## Alfred Hitchcock movies

| Rating | Votes | Year | Name                                                              |
| ------ | ----- | ---- | ----------------------------------------------------------------- |
| 6.6    | 3334  | 1976 | [Family Plot](http://www.imdb.com/title/tt0074512/)               |
| 7.5    | 5771  | 1972 | [Frenzy](http://www.imdb.com/title/tt0068611/)                    |
| 6.5    | 3827  | 1966 | [Torn Curtain](http://www.imdb.com/title/tt0061107/)              |
| 7.2    | 6659  | 1964 | [Marnie](http://www.imdb.com/title/tt0058329/)                    |
| 7.8    | 27315 | 1963 | [The Birds](http://www.imdb.com/title/tt0056869/)                 |
| 8.6    | 72264 | 1960 | [Psycho](http://www.imdb.com/title/tt0054215/)                    |
| 8.6    | 48162 | 1959 | [North by Northwest](http://www.imdb.com/title/tt0053125/)        |
| 8.5    | 46135 | 1958 | [Vertigo](http://www.imdb.com/title/tt0052357/)                   |
| 7.4    | 3054  | 1956 | [The Wrong Man](http://www.imdb.com/title/tt0051207/)             |
| 7.5    | 8243  | 1956 | [The Man Who Knew Too Much](http://www.imdb.com/title/tt0049470/) |
| 7.2    | 5430  | 1955 | [The Trouble with Harry](http://www.imdb.com/title/tt0048750/)    |
| 7.5    | 8567  | 1955 | [To Catch a Thief](http://www.imdb.com/title/tt0048728/)          |
| 8.7    | 56930 | 1954 | [Rear Window](http://www.imdb.com/title/tt0047396/)               |
| 8      | 11338 | 1954 | [Dial M for Murder](http://www.imdb.com/title/tt0046912/)         |
| 7      | 2411  | 1953 | [I Confess](http://www.imdb.com/title/tt0045897/)                 |
| 8.3    | 15361 | 1951 | [Strangers on a Train](http://www.imdb.com/title/tt0044079/)      |
| 6.9    | 1874  | 1950 | [Stage Fright](http://www.imdb.com/title/tt0042994/)              |
| 8      | 11769 | 1948 | [Rope](http://www.imdb.com/title/tt0040746/)                      |
| 6.3    | 1842  | 1947 | [The Paradine Case](http://www.imdb.com/title/tt0039694/)         |
| 8.3    | 15004 | 1946 | [Notorious](http://www.imdb.com/title/tt0038787/)                 |
| 7.6    | 7240  | 1945 | [Spellbound](http://www.imdb.com/title/tt0038109/)                |
| 8      | 22    | 1945 | [Watchtower Over Tomorrow](http://www.imdb.com/title/tt0187589/)  |
| 7.8    | 4277  | 1944 | [Lifeboat](http://www.imdb.com/title/tt0037017/)                  |
| 6.7    | 262   | 1944 | [Bon Voyage](http://www.imdb.com/title/tt0036659/)                |
| 5.8    | 252   | 1944 | [Aventure malgache](http://www.imdb.com/title/tt0036621/)         |
| 8.2    | 8789  | 1943 | [Shadow of a Doubt](http://www.imdb.com/title/tt0036342/)         |
| 7.3    | 3185  | 1942 | [Saboteur](http://www.imdb.com/title/tt0035279/)                  |
| 7.6    | 4717  | 1941 | [Suspicion](http://www.imdb.com/title/tt0034248/)                 |
| 6.5    | 1624  | 1941 | [Mr. & Mrs. Smith](http://www.imdb.com/title/tt0033922/)          |
| 7.7    | 3035  | 1940 | [Foreign Correspondent](http://www.imdb.com/title/tt0032484/)     |
| 8.4    | 16312 | 1940 | [Rebecca](http://www.imdb.com/title/tt0032976/)                   |
| 8.1    | 6899  | 1938 | [The Lady Vanishes](http://www.imdb.com/title/tt0030341/)         |
| 7.1    | 1366  | 1937 | [Young and Innocent](http://www.imdb.com/title/tt0029811/)        |
| 7.2    | 2142  | 1936 | [Sabotage](http://www.imdb.com/title/tt0028212/)                  |
| 6.7    | 1407  | 1936 | [Secret Agent](http://www.imdb.com/title/tt0028231/)              |
| 8      | 11050 | 1935 | [The 39 Steps](http://www.imdb.com/title/tt0026029/)              |

## Cary Grant movies

| Rating | Votes | Year | Name                                                                         |
| ------ | ----- | ---- | ---------------------------------------------------------------------------- |
| 6.5    | 694   | 1966 | [Walk Don't Run](http://www.imdb.com/title/tt0061170/)                       |
| 7.2    | 2190  | 1964 | [Father Goose](http://www.imdb.com/title/tt0058092/)                         |
| 8      | 13093 | 1963 | [Charade](http://www.imdb.com/title/tt0056923/)                              |
| 6.5    | 1581  | 1962 | [That Touch of Mink](http://www.imdb.com/title/tt0056575/)                   |
| 6.7    | 869   | 1960 | [The Grass Is Greener](http://www.imdb.com/title/tt0053877/)                 |
| 7.2    | 2454  | 1959 | [Operation Petticoat](http://www.imdb.com/title/tt0053143/)                  |
| 8.6    | 48184 | 1959 | [North by Northwest](http://www.imdb.com/title/tt0053125/)                   |
| 6.5    | 1521  | 1958 | [Houseboat](http://www.imdb.com/title/tt0051745/)                            |
| 6.8    | 1590  | 1958 | [Indiscreet](http://www.imdb.com/title/tt0051773/)                           |
| 5.5    | 328   | 1957 | [Kiss Them for Me](http://www.imdb.com/title/tt0050599/)                     |
| 5.3    | 501   | 1957 | [The Pride and the Passion](http://www.imdb.com/title/tt0050858/)            |
| 7.2    | 4655  | 1957 | [An Affair to Remember](http://www.imdb.com/title/tt0050105/)                |
| 7.5    | 8567  | 1955 | [To Catch a Thief](http://www.imdb.com/title/tt0048728/)                     |
| 5.5    | 303   | 1953 | [Dream Wife](http://www.imdb.com/title/tt0045706/)                           |
| 7.1    | 2054  | 1952 | [Monkey Business](http://www.imdb.com/title/tt0044916/)                      |
| 6.3    | 214   | 1952 | [Room for One More](http://www.imdb.com/title/tt0045102/)                    |
| 7.4    | 1052  | 1951 | [People Will Talk](http://www.imdb.com/title/tt0043915/)                     |
| 6.3    | 314   | 1950 | [Crisis](http://www.imdb.com/title/tt0042352/)                               |
| 6.9    | 1635  | 1949 | [I Was a Male War Bride](http://www.imdb.com/title/tt0041498/)               |
| 6      | 411   | 1948 | [Every Girl Should Be Married](http://www.imdb.com/title/tt0040331/)         |
| 7.2    | 2178  | 1948 | [Mr. Blandings Builds His Dream House](http://www.imdb.com/title/tt0040613/) |
| 7.5    | 2671  | 1947 | [The Bishop's Wife](http://www.imdb.com/title/tt0039190/)                    |
| 7.2    | 1387  | 1947 | [The Bachelor and the Bobby-Soxer](http://www.imdb.com/title/tt0039169/)     |
| 8.3    | 15004 | 1946 | [Notorious](http://www.imdb.com/title/tt0038787/)                            |
| 6.1    | 504   | 1946 | [Night and Day](http://www.imdb.com/title/tt0038776/)                        |
| 6.3    | 314   | 1944 | [None But the Lonely Heart](http://www.imdb.com/title/tt0037135/)            |
| 8      | 15390 | 1944 | [Arsenic and Old Lace](http://www.imdb.com/title/tt0036613/)                 |
| 5.8    | 112   | 1944 | [Once Upon a Time](http://www.imdb.com/title/tt0037150/)                     |
| 7.2    | 973   | 1943 | [Destination Tokyo](http://www.imdb.com/title/tt0035799/)                    |
| 7.2    | 453   | 1943 | [Mr. Lucky](http://www.imdb.com/title/tt0036174/)                            |
| 6.3    | 403   | 1942 | [Once Upon a Honeymoon](http://www.imdb.com/title/tt0035151/)                |
| 7.7    | 1042  | 1942 | [The Talk of the Town](http://www.imdb.com/title/tt0035417/)                 |
| 7.6    | 4717  | 1941 | [Suspicion](http://www.imdb.com/title/tt0034248/)                            |
| 7      | 1126  | 1941 | [Penny Serenade](http://www.imdb.com/title/tt0034012/)                       |
| 8.1    | 14383 | 1940 | [The Philadelphia Story](http://www.imdb.com/title/tt0032904/)               |
| 6.2    | 105   | 1940 | [The Howards of Virginia](http://www.imdb.com/title/tt0032612/)              |
| 7.2    | 1685  | 1940 | [My Favorite Wife](http://www.imdb.com/title/tt0029284/)                     |
| 8      | 9692  | 1940 | [His Girl Friday](http://www.imdb.com/title/tt0032599/)                      |
| 6.9    | 446   | 1939 | [In Name Only](http://www.imdb.com/title/tt0031477/)                         |
| 7.5    | 1828  | 1939 | [Only Angels Have Wings](http://www.imdb.com/title/tt0031762/)               |
| 7.6    | 2972  | 1939 | [Gunga Din](http://www.imdb.com/title/tt0031398/)                            |
| 7.8    | 2243  | 1938 | [Holiday](http://www.imdb.com/title/tt0030241/)                              |
| 8      | 12761 | 1938 | [Bringing Up Baby](http://www.imdb.com/title/tt0029947/)                     |
| 7.9    | 2719  | 1937 | [The Awful Truth](http://www.imdb.com/title/tt0028597/)                      |
| 6.6    | 181   | 1937 | [The Toast of New York](http://www.imdb.com/title/tt0029675/)                |
| 7.4    | 1354  | 1937 | [Topper](http://www.imdb.com/title/tt0029682/)                               |
| 5.6    | 56    | 1937 | [When You're in Love](http://www.imdb.com/title/tt0029761/)                  |
| 5.9    | 39    | 1936 | [Wedding Present](http://www.imdb.com/title/tt0028486/)                      |
| 6.1    | 313   | 1936 | [The Amazing Quest of Ernest Bliss](http://www.imdb.com/title/tt0027286/)    |
| 6.3    | 218   | 1936 | [Suzy](http://www.imdb.com/title/tt0028330/)                                 |
| 6.2    | 49    | 1936 | [Big Brown Eyes](http://www.imdb.com/title/tt0027357/)                       |
| 6.1    | 597   | 1935 | [Sylvia Scarlett](http://www.imdb.com/title/tt0027067/)                      |
| 4.9    | 39    | 1935 | [The Last Outpost](http://www.imdb.com/title/tt0026607/)                     |
| 6.1    | 33    | 1935 | [Wings in the Dark](http://www.imdb.com/title/tt0027221/)                    |
| 6.4    | 23    | 1935 | [Enter Madame](http://www.imdb.com/title/tt0026315/)                         |
| 4.9    | 25    | 1934 | [Ladies Should Listen](http://www.imdb.com/title/tt0025363/)                 |
| 5.4    | 44    | 1934 | [Kiss and Make-Up](http://www.imdb.com/title/tt0025351/)                     |
| 6.1    | 124   | 1934 | [Born to Be Bad](http://www.imdb.com/title/tt0024906/)                       |
| 6.5    | 37    | 1934 | [Thirty Day Princess](http://www.imdb.com/title/tt0025880/)                  |
| 6.4    | 301   | 1933 | [Alice in Wonderland](http://www.imdb.com/title/tt0023753/)                  |
| 7.1    | 424   | 1933 | [I'm No Angel](http://www.imdb.com/title/tt0024166/)                         |
| 5.3    | 26    | 1933 | [Gambling Ship](http://www.imdb.com/title/tt0024048/)                        |
| 7      | 105   | 1933 | [The Eagle and the Hawk](http://www.imdb.com/title/tt0023973/)               |
| 5.9    | 34    | 1933 | [The Woman Accused](http://www.imdb.com/title/tt0024781/)                    |
| 6.7    | 762   | 1933 | [She Done Him Wrong](http://www.imdb.com/title/tt0024548/)                   |
| 6.3    | 34    | 1932 | [Madame Butterfly](http://www.imdb.com/title/tt0023169/)                     |
| 6.2    | 30    | 1932 | [Hot Saturday](http://www.imdb.com/title/tt0023028/)                         |
| 7.2    | 618   | 1932 | [Blonde Venus](http://www.imdb.com/title/tt0022698/)                         |
| 5.6    | 54    | 1932 | [Devil and the Deep](http://www.imdb.com/title/tt0022814/)                   |
| 5.9    | 37    | 1932 | [Merrily We Go to Hell](http://www.imdb.com/title/tt0023213/)                |
| 5.2    | 52    | 1932 | [Singapore Sue](http://www.imdb.com/title/tt0022387/)                        |
| 6.3    | 20    | 1932 | [Sinners in the Sun](http://www.imdb.com/title/tt0023479/)                   |
| 6.9    | 37    | 1932 | [This Is the Night](http://www.imdb.com/title/tt0023584/)                    |

## Audrey Hepburn movies

| Rating | Votes | Year | Name                                                             |
| ------ | ----- | ---- | ---------------------------------------------------------------- |
| 6.4    | 2457  | 1976 | [Robin and Marian](http://www.imdb.com/title/tt0075147/)         |
| 7.8    | 4936  | 1967 | [Wait Until Dark](http://www.imdb.com/title/tt0062467/)          |
| 7.4    | 1878  | 1967 | [Two for the Road](http://www.imdb.com/title/tt0062407/)         |
| 7.3    | 2495  | 1966 | [How to Steal a Million](http://www.imdb.com/title/tt0060522/)   |
| 7.8    | 16442 | 1964 | [My Fair Lady](http://www.imdb.com/title/tt0058385/)             |
| 5.8    | 970   | 1964 | [Paris - When It Sizzles](http://www.imdb.com/title/tt0058453/)  |
| 8      | 13093 | 1963 | [Charade](http://www.imdb.com/title/tt0056923/)                  |
| 7.4    | 1768  | 1961 | [The Children's Hour](http://www.imdb.com/title/tt0054743/)      |
| 7.7    | 17252 | 1961 | [Breakfast at Tiffany's](http://www.imdb.com/title/tt0054698/)   |
| 6.8    | 974   | 1960 | [The Unforgiven](http://www.imdb.com/title/tt0054428/)           |
| 7.5    | 1716  | 1959 | [The Nun's Story](http://www.imdb.com/title/tt0053131/)          |
| 5.1    | 375   | 1959 | [Green Mansions](http://www.imdb.com/title/tt0052864/)           |
| 7.3    | 1658  | 1957 | [Love in the Afternoon](http://www.imdb.com/title/tt0050658/)    |
| 7      | 2617  | 1957 | [Funny Face](http://www.imdb.com/title/tt0050419/)               |
| 6.6    | 1231  | 1955 | [War and Peace](http://www.imdb.com/title/tt0049934/)            |
| 7.7    | 8236  | 1954 | [Sabrina](http://www.imdb.com/title/tt0047437/)                  |
| 8      | 13601 | 1953 | [Roman Holiday](http://www.imdb.com/title/tt0046250/)            |
| 6.4    | 49    | 1952 | [The Secret People](http://www.imdb.com/title/tt0044014/)        |
| 5.2    | 32    | 1951 | [Nous irons à Monte Carlo](http://www.imdb.com/title/tt0043865/) |
| 5.1    | 26    | 1951 | [Young Wives' Tale](http://www.imdb.com/title/tt0044225/)        |
| 7.9    | 2602  | 1951 | [The Lavender Hill Mob](http://www.imdb.com/title/tt0044829/)    |
| 7      | 147   | 1951 | [Laughter in Paradise](http://www.imdb.com/title/tt0043727/)     |
| 5.4    | 20    | 1951 | [One Wild Oat](http://www.imdb.com/title/tt0043884/)             |
| 4.7    | 20    | 1951 | [Monte Carlo Baby](http://www.imdb.com/title/tt0043818/)         |

## Al Pacino movies

| Rating | Votes  | Year | Name                                                             |
| ------ | ------ | ---- | ---------------------------------------------------------------- |
| 6.1    | 6358   | 2005 | [Two for the Money](http://www.imdb.com/title/tt0417217/)        |
| 7.2    | 5368   | 2004 | [The Merchant of Venice](http://www.imdb.com/title/tt0379889/)   |
| 6.5    | 19214  | 2003 | [The Recruit](http://www.imdb.com/title/tt0292506/)              |
| 6.2    | 11123  | 2002 | [S1m0ne](http://www.imdb.com/title/tt0258153/)                   |
| 7.2    | 31120  | 2002 | [Insomnia](http://www.imdb.com/title/tt0278504/)                 |
| 7.6    | 102    | 2000 | [Chinese Coffee](http://www.imdb.com/title/tt0118852/)           |
| 6.4    | 26493  | 1999 | [Any Given Sunday](http://www.imdb.com/title/tt0146838/)         |
| 7.9    | 39006  | 1999 | [The Insider](http://www.imdb.com/title/tt0140352/)              |
| 7.1    | 37111  | 1997 | [The Devil's Advocate](http://www.imdb.com/title/tt0118971/)     |
| 7.6    | 29318  | 1997 | [Donnie Brasco](http://www.imdb.com/title/tt0119008/)            |
| 6.1    | 5750   | 1996 | [City Hall](http://www.imdb.com/title/tt0115907/)                |
| 8      | 64528  | 1995 | [Heat](http://www.imdb.com/title/tt0113277/)                     |
| 6.1    | 713    | 1995 | [Two Bits](http://www.imdb.com/title/tt0114753/)                 |
| 7.6    | 20888  | 1993 | [Carlito's Way](http://www.imdb.com/title/tt0106519/)            |
| 7.5    | 23352  | 1992 | [Scent of a Woman](http://www.imdb.com/title/tt0105323/)         |
| 7.8    | 15873  | 1992 | [Glengarry Glen Ross](http://www.imdb.com/title/tt0104348/)      |
| 6.3    | 5459   | 1991 | [Frankie and Johnny](http://www.imdb.com/title/tt0101912/)       |
| 7.4    | 35075  | 1990 | [The Godfather: Part III](http://www.imdb.com/title/tt0099674/)  |
| 5.7    | 13293  | 1990 | [Dick Tracy](http://www.imdb.com/title/tt0099422/)               |
| 7.9    | 68     | 1990 | [The Local Stigmatic](http://www.imdb.com/title/tt0097769/)      |
| 6.6    | 7199   | 1989 | [Sea of Love](http://www.imdb.com/title/tt0098273/)              |
| 4.5    | 1406   | 1985 | [Revolution](http://www.imdb.com/title/tt0089913/)               |
| 8      | 51894  | 1983 | [Scarface](http://www.imdb.com/title/tt0086250/)                 |
| 5.7    | 1292   | 1982 | [Author! Author!](http://www.imdb.com/title/tt0083598/)          |
| 5.6    | 1938   | 1980 | [Cruising](http://www.imdb.com/title/tt0080569/)                 |
| 7.1    | 4040   | 1979 | [...And Justice for All](http://www.imdb.com/title/tt0078718/)   |
| 8.1    | 22859  | 1975 | [Dog Day Afternoon](http://www.imdb.com/title/tt0072890/)        |
| 9      | 104479 | 1974 | [The Godfather: Part II](http://www.imdb.com/title/tt0071562/)   |
| 7.6    | 9924   | 1973 | [Serpico](http://www.imdb.com/title/tt0070666/)                  |
| 7      | 1718   | 1973 | [Scarecrow](http://www.imdb.com/title/tt0070643/)                |
| 9.1    | 184538 | 1972 | [The Godfather](http://www.imdb.com/title/tt0068646/)            |
| 6.9    | 1620   | 1971 | [The Panic in Needle Park](http://www.imdb.com/title/tt0067549/) |
| 6.6    | 180    | 1969 | [Me, Natalie](http://www.imdb.com/title/tt0064651/)              |

## Ingrid Bergman movies

| Rating | Votes | Year | Name                                                                 |
| ------ | ----- | ---- | -------------------------------------------------------------------- |
| 8      | 2005  | 1978 | [Höstsonaten](http://www.imdb.com/title/tt0077711/)                  |
| 7.2    | 5902  | 1974 | [Murder on the Orient Express](http://www.imdb.com/title/tt0071877/) |
| 6.7    | 1499  | 1969 | [Cactus Flower](http://www.imdb.com/title/tt0064117/)                |
| 6.8    | 1590  | 1958 | [Indiscreet](http://www.imdb.com/title/tt0051773/)                   |
| 7.1    | 1492  | 1956 | [Anastasia](http://www.imdb.com/title/tt0048947/)                    |
| 6.2    | 402   | 1948 | [Joan of Arc](http://www.imdb.com/title/tt0040491/)                  |
| 8.3    | 15004 | 1946 | [Notorious](http://www.imdb.com/title/tt0038787/)                    |
| 7.4    | 1364  | 1945 | [The Bells of St. Mary's](http://www.imdb.com/title/tt0037536/)      |
| 6.2    | 222   | 1945 | [Saratoga Trunk](http://www.imdb.com/title/tt0038053/)               |
| 7.6    | 7240  | 1945 | [Spellbound](http://www.imdb.com/title/tt0038109/)                   |
| 7.8    | 3865  | 1944 | [Gaslight](http://www.imdb.com/title/tt0036855/)                     |
| 7.1    | 1535  | 1943 | [For Whom the Bell Tolls](http://www.imdb.com/title/tt0035896/)      |
| 8.8    | 89653 | 1942 | [Casablanca](http://www.imdb.com/title/tt0034583/)                   |
| 6.7    | 1265  | 1941 | [Dr. Jekyll and Mr. Hyde](http://www.imdb.com/title/tt0033553/)      |

## Howard Hawks movies

| Rating | Votes | Year | Name                                                                  |
| ------ | ----- | ---- | --------------------------------------------------------------------- |
| 6.5    | 1501  | 1970 | [Rio Lobo](http://www.imdb.com/title/tt0066301/)                      |
| 7.5    | 3466  | 1966 | [El Dorado](http://www.imdb.com/title/tt0061619/)                     |
| 5.5    | 169   | 1965 | [Red Line 7000](http://www.imdb.com/title/tt0059641/)                 |
| 6.9    | 853   | 1964 | [Man's Favorite Sport?](http://www.imdb.com/title/tt0058324/)         |
| 7.2    | 2177  | 1962 | [Hatari!](http://www.imdb.com/title/tt0056059/)                       |
| 7.9    | 9973  | 1959 | [Rio Bravo](http://www.imdb.com/title/tt0053221/)                     |
| 6.4    | 612   | 1955 | [Land of the Pharaohs](http://www.imdb.com/title/tt0048283/)          |
| 7.1    | 3676  | 1953 | [Gentlemen Prefer Blondes](http://www.imdb.com/title/tt0045810/)      |
| 7.2    | 340   | 1952 | [O. Henry's Full House](http://www.imdb.com/title/tt0044981/)         |
| 7.1    | 2054  | 1952 | [Monkey Business](http://www.imdb.com/title/tt0044916/)               |
| 7.1    | 606   | 1952 | [The Big Sky](http://www.imdb.com/title/tt0044419/)                   |
| 7.4    | 3926  | 1951 | [The Thing from Another World](http://www.imdb.com/title/tt0044121/)  |
| 6.9    | 1635  | 1949 | [I Was a Male War Bride](http://www.imdb.com/title/tt0041498/)        |
| 7.1    | 427   | 1948 | [A Song Is Born](http://www.imdb.com/title/tt0040820/)                |
| 7.9    | 5541  | 1948 | [Red River](http://www.imdb.com/title/tt0040724/)                     |
| 8.3    | 14099 | 1946 | [The Big Sleep](http://www.imdb.com/title/tt0038355/)                 |
| 8.1    | 5937  | 1944 | [To Have and Have Not](http://www.imdb.com/title/tt0037382/)          |
| 6.7    | 100   | 1943 | [Corvette K-225](http://www.imdb.com/title/tt0035757/)                |
| 5.5    | 678   | 1943 | [The Outlaw](http://www.imdb.com/title/tt0036241/)                    |
| 7.1    | 439   | 1943 | [Air Force](http://www.imdb.com/title/tt0035616/)                     |
| 7.8    | 1604  | 1941 | [Ball of Fire](http://www.imdb.com/title/tt0033373/)                  |
| 8.1    | 3244  | 1941 | [Sergeant York](http://www.imdb.com/title/tt0034167/)                 |
| 8      | 9692  | 1940 | [His Girl Friday](http://www.imdb.com/title/tt0032599/)               |
| 7.5    | 1828  | 1939 | [Only Angels Have Wings](http://www.imdb.com/title/tt0031762/)        |
| 8      | 12761 | 1938 | [Bringing Up Baby](http://www.imdb.com/title/tt0029947/)              |
| 6.9    | 271   | 1936 | [Come and Get It](http://www.imdb.com/title/tt0027459/)               |
| 6.9    | 144   | 1936 | [Ceiling Zero](http://www.imdb.com/title/tt0026191/)                  |
| 6.7    | 246   | 1935 | [Barbary Coast](http://www.imdb.com/title/tt0026097/)                 |
| 7.9    | 711   | 1934 | [Twentieth Century](http://www.imdb.com/title/tt0025919/)             |
| 6.6    | 194   | 1934 | [Viva Villa!](http://www.imdb.com/title/tt0025948/)                   |
| 6.5    | 139   | 1933 | [The Prizefighter and the Lady](http://www.imdb.com/title/tt0024475/) |
| 6.1    | 160   | 1933 | [Today We Live](http://www.imdb.com/title/tt0024675/)                 |
| 6.4    | 142   | 1932 | [Tiger Shark](http://www.imdb.com/title/tt0023594/)                   |
| 6.3    | 158   | 1932 | [The Crowd Roars](http://www.imdb.com/title/tt0022792/)               |
| 7.9    | 3775  | 1932 | [Scarface](http://www.imdb.com/title/tt0023427/)                      |

## Frank Capra movies

| Rating | Votes | Year | Name                                                                  |
| ------ | ----- | ---- | --------------------------------------------------------------------- |
| 7.2    | 1105  | 1961 | [Pocketful of Miracles](http://www.imdb.com/title/tt0055312/)         |
| 6.1    | 447   | 1959 | [A Hole in the Head](http://www.imdb.com/title/tt0052896/)            |
| 5.6    | 229   | 1951 | [Here Comes the Groom](http://www.imdb.com/title/tt0043633/)          |
| 5.7    | 112   | 1950 | [Riding High](http://www.imdb.com/title/tt0042893/)                   |
| 7.4    | 602   | 1948 | [State of the Union](http://www.imdb.com/title/tt0040834/)            |
| 8.6    | 54216 | 1946 | [It's a Wonderful Life](http://www.imdb.com/title/tt0038650/)         |
| 8      | 15390 | 1944 | [Arsenic and Old Lace](http://www.imdb.com/title/tt0036613/)          |
| 7.5    | 2493  | 1941 | [Meet John Doe](http://www.imdb.com/title/tt0033891/)                 |
| 8.3    | 16247 | 1939 | [Mr. Smith Goes to Washington](http://www.imdb.com/title/tt0031679/)  |
| 7.9    | 4303  | 1938 | [You Can't Take It with You](http://www.imdb.com/title/tt0030993/)    |
| 7.7    | 2914  | 1937 | [Lost Horizon](http://www.imdb.com/title/tt0029162/)                  |
| 7.9    | 3355  | 1936 | [Mr. Deeds Goes to Town](http://www.imdb.com/title/tt0027996/)        |
| 6.2    | 187   | 1934 | [Broadway Bill](http://www.imdb.com/title/tt0024916/)                 |
| 8.2    | 11222 | 1934 | [It Happened One Night](http://www.imdb.com/title/tt0025316/)         |
| 7.5    | 542   | 1933 | [Lady for a Day](http://www.imdb.com/title/tt0024240/)                |
| 7.2    | 348   | 1933 | [The Bitter Tea of General Yen](http://www.imdb.com/title/tt0023814/) |
| 7.3    | 164   | 1932 | [American Madness](http://www.imdb.com/title/tt0022626/)              |
| 6.4    | 85    | 1932 | [Forbidden](http://www.imdb.com/title/tt0022905/)                     |
| 6.8    | 456   | 1931 | [Platinum Blonde](http://www.imdb.com/title/tt0022268/)               |
| 7.2    | 234   | 1931 | [The Miracle Woman](http://www.imdb.com/title/tt0022153/)             |

## Disney movies

| Rating | Votes | Year | Name                                                                |
| ------ | ----- | ---- | ------------------------------------------------------------------- |
| \-     | \-    | 1937 | [Snow White And The Seven Dwarfs](-)                                |
| \-     | \-    | 1940 | [Pinocchio](-)                                                      |
| \-     | \-    | 1940 | [Fantasia](-)                                                       |
| \-     | \-    | 1941 | [The Reluctant Dragon](-)                                           |
| \-     | \-    | 1941 | [Dumbo](-)                                                          |
| \-     | \-    | 1942 | [Bambi](-)                                                          |
| \-     | \-    | 1943 | [Saludos Amigos](-)                                                 |
| \-     | \-    | 1943 | [Victory Through Air Power](-)                                      |
| \-     | \-    | 1945 | [The Three Caballeros](-)                                           |
| \-     | \-    | 1946 | [Make Mine Music](-)                                                |
| \-     | \-    | 1946 | [Song Of The South](-)                                              |
| \-     | \-    | 1947 | [Fun & Fancy Free](-)                                               |
| \-     | \-    | 1948 | [Melody Time](-)                                                    |
| \-     | \-    | 1949 | [So Dear To My Heart](-)                                            |
| \-     | \-    | 1949 | [The Adventures Of Ichabod And Mister Toad](-)                      |
| \-     | \-    | 1950 | [Cinderella](-)                                                     |
| \-     | \-    | 1951 | [Alice In Wonderland](-)                                            |
| \-     | \-    | 1953 | [Peter Pan](-)                                                      |
| \-     | \-    | 1955 | [Lady And The Tramp](-)                                             |
| \-     | \-    | 1959 | [Sleeping Beauty](-)                                                |
| \-     | \-    | 1961 | [One Hundred And One Dalmatians](-)                                 |
| \-     | \-    | 1963 | [The Sword In The Stone](-)                                         |
| \-     | \-    | 1964 | [Mary Poppins](-)                                                   |
| \-     | \-    | 1967 | [The Jungle Book](-)                                                |
| \-     | \-    | 1970 | [The Aristocats](-)                                                 |
| \-     | \-    | 1971 | [Bedknobs And Broomsticks](-)                                       |
| \-     | \-    | 1973 | [Robin Hood](-)                                                     |
| \-     | \-    | 1977 | [The Many Adventures Of Winnie The Pooh](-)                         |
| \-     | \-    | 1977 | [The Rescuers](-)                                                   |
| \-     | \-    | 1977 | [Pete's Dragon](-)                                                  |
| \-     | \-    | 1981 | [The Fox And The Hound](-)                                          |
| \-     | \-    | 1985 | [Return To Oz](-)                                                   |
| \-     | \-    | 1985 | [The Black Cauldron](-)                                             |
| \-     | \-    | 1986 | [The Great Mouse Detective](-)                                      |
| \-     | \-    | 1988 | [Oliver & Company](-)                                               |
| \-     | \-    | 1989 | [The Little Mermaid](-)                                             |
| \-     | \-    | 1990 | [DuckTales: The Movie (Treasure Of The Lost Lamp)](-)               |
| \-     | \-    | 1990 | [The Rescuers Down Under](-)                                        |
| \-     | \-    | 1991 | [Beauty And The Beast](-)                                           |
| \-     | \-    | 1992 | [Aladdin](-)                                                        |
| \-     | \-    | 1994 | [The Lion King](-)                                                  |
| \-     | \-    | 1995 | [A Goofy Movie](-)                                                  |
| \-     | \-    | 1995 | [Pocahontas](-)                                                     |
| \-     | \-    | 1996 | [James And The Giant Peach](-)                                      |
| \-     | \-    | 1996 | [The Hunchback Of Notre Dame](-)                                    |
| \-     | \-    | 1997 | [Hercules](-)                                                       |
| \-     | \-    | 1998 | [Mulan](-)                                                          |
| \-     | \-    | 1999 | [Doug's 1st Movie](-)                                               |
| \-     | \-    | 1999 | [Tarzan](-)                                                         |
| \-     | \-    | 1999 | [Fantasia 2000](-)                                                  |
| \-     | \-    | 2000 | [The Tigger Movie](-)                                               |
| \-     | \-    | 2000 | [Dinosaur](-)                                                       |
| \-     | \-    | 2000 | [The Emperor's New Groove](-)                                       |
| \-     | \-    | 2001 | [Recess: School's Out](-)                                           |
| \-     | \-    | 2001 | [Atlantis: The Lost Empire](-)                                      |
| \-     | \-    | 2002 | [Return To Never Land](-)                                           |
| \-     | \-    | 2002 | [Lilo & Stitch](-)                                                  |
| \-     | \-    | 2002 | [Treasure Planet](-)                                                |
| \-     | \-    | 2003 | [The Jungle Book 2](-)                                              |
| \-     | \-    | 2003 | [Piglet's BIG Movie](-)                                             |
| \-     | \-    | 2003 | [Brother Bear](-)                                                   |
| \-     | \-    | 2004 | [Teacher's Pet](-)                                                  |
| \-     | \-    | 2004 | [Home On The Range](-)                                              |
| \-     | \-    | 2005 | [Pooh's Heffalump Movie](-)                                         |
| \-     | \-    | 2005 | [Chicken Little](-)                                                 |
| \-     | \-    | 2005 | [The Chronicles Of Narnia: The Lion, The Witch And The Wardrobe](-) |
| \-     | \-    | 2005 | [Fraidy Cat](-)                                                     |
| \-     | \-    | 2006 | [The Wild](-)                                                       |
| \-     | \-    | 2007 | [Meet The Robinsons](-)                                             |
| \-     | \-    | 2007 | [Enchanted](-)                                                      |
| \-     | \-    | 2007 | [A Christmas Carol](-)                                              |

## Pixar movies

| Rating | Votes | Year | Name                 |
| ------ | ----- | ---- | -------------------- |
| \-     | \-    | 1995 | [Toy Story](-)       |
| \-     | \-    | 1998 | [A Bug's Life](-)    |
| \-     | \-    | 1999 | [Toy Story 2](-)     |
| \-     | \-    | 2001 | [Monsters, Inc.](-)  |
| \-     | \-    | 2003 | [Finding Nemo](-)    |
| \-     | \-    | 2004 | [The Incredibles](-) |
| \-     | \-    | 2005 | [A Bug's Life II](-) |
| \-     | \-    | 2006 | [Cars](-)            |
| \-     | \-    | 2007 | [Ratatouille](-)     |
| \-     | \-    | 2007 | [Ray Gun](-)         |

## Other movies to see

| Rating | Votes | Year | Name                                                            |
| ------ | ----- | ---- | --------------------------------------------------------------- |
| 7.8    | 9004  | 1962 | [The Longest Day](http://www.imdb.com/title/tt0056197/)         |
| 7.8    | 33786 | 1991 | [Beauty and the Beast](http://www.imdb.com/title/tt0101414/)    |
| 7.8    | 48940 | 2001 | [The Others](http://www.imdb.com/title/tt0230600/)              |
| 7.8    | 38293 | 1990 | [Dances with Wolves](http://www.imdb.com/title/tt0099348/)      |
| 7.7    | 8054  | 2006 | [The Illusionist](http://www.imdb.com/title/tt0443543/)         |
| 7.6    | 30627 | 1989 | [When Harry Met Sally...](http://www.imdb.com/title/tt0098635/) |
| 7.5    | 16445 | 2003 | [Seabiscuit](http://www.imdb.com/title/tt0329575/)              |
| 7.4    | 25291 | 1997 | [Grosse Pointe Blank](http://www.imdb.com/title/tt0119229/)     |
| 7.1    | 16656 | 2003 | [Runaway Jury](http://www.imdb.com/title/tt0313542/)            |
| 7      | 4929  | 1980 | [Dressed to Kill](http://www.imdb.com/title/tt0080661/)         |
| 7      | 5106  | 1981 | [Blow Out](http://www.imdb.com/title/tt0082085/)                |
| 7      | 29891 | 1998 | [Ronin](http://www.imdb.com/title/tt0122690/)                   |
| 6.8    | 6526  | 1989 | [Casualties of War](http://www.imdb.com/title/tt0097027/)       |
| 6.6    | 9335  | 1987 | [Roxanne](http://www.imdb.com/title/tt0093886/)                 |
| 6.6    | 796   | 1963 | [The Prize](http://www.imdb.com/title/tt0057426/)               |
| 6.5    | 534   | 1995 | [Above Suspicion](http://www.imdb.com/title/tt0109034/)         |
| 6.1    | 632   | 1996 | [Infinity](http://www.imdb.com/title/tt0116635/)                |

---

## Comments

<!-- wp-comments-start -->

- **Raja** _28 Feb 2007 1:14 am_:
  This is cool stuff...Hats Off

<!-- wp-comments-end -->
