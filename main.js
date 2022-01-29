/////////////////////////////
//// KUTX 98.9, AUSTIN TEXAS
////////////////////////////

// The function below takes the div elements from the playlist
// retrieved on the kutx website from a given day and creates
// objects containing the artist, record, and song title.
// These can then be analyzed by the spotify API

const songs = [];

const playlist = document.querySelector("#playlist");
// console.log([...playlist.children[0].classList].includes("track"));

for (const child of playlist.children) {
  if ([...child.classList].includes("track")) {
    // console.log(child);
    songs.push({
      hour:
        child.children[0].innerText.split(" ")[3] === "AM"
          ? child.children[0].innerText.split(" ")[2].split(":")[0]
          : +child.children[0].innerText.split(" ")[2].split(":")[0] + 12,
      track: child.children[1].innerHTML.trim(),
      artist: child.children[2].innerHTML.trim(),
      record: child.children[4].innerHTML.trim(),
    });
  }
}

///////////////////////
// Query Spotify API
//////////////////////

const spotifySearchArtists = async function (url) {
  try {
    const results = await fetch(url, {
      headers: {
        Authorization:
          "Bearer BQAAG-JFgFzMlPkIZi-hTNXqtMeWK8R7ChA9-wxvQpCZvksBDtKMF1ygI20hNNjukN40duXsKBKdK6-w8is62qp0dQiekaSXyG1uKQSoK3T_HM9i9iQi2rCS3pV3k_C0sMaw1qN9sYzlOYqJ6M678W43yZXPnQTBxcM",
      },
    });
    const resultsParsed = await results.json();
    return resultsParsed;
  } catch (err) {
    console.log(err);
  }
};

// GET POPULARITY OF TRACKS PER SHOW AS QUANTITIES
// CURRENT ISSUE: RETURNING -INFINITY FOR SOME

let popSum = 0;
let artistsCounted = 0;

const generateArtistQuery = (song) => {
  let cleaned = song.artist;
  if (cleaned.includes("&amp;")) {
    return cleaned.split("&amp;")[0].trim();
  }
  cleaned = cleaned.replace(" ", "%25");
  return cleaned;
};

const retrievePopularity = async (songs) => {
  for (const song of songs) {
    // if (song.artist.includes("&amp;")) console.log("got one!");
    // Only search for first artist if it is a collab

    // Retrieving the proper URL by which to query Spotify API
    // Searching by artist
    // Retrieving their id which can then be used to determine their popularity
    const url = `https://api.spotify.com/v1/search?q=artist%3A${generateArtistQuery(
      song
    )}&type=artist`;

    const artistSearch = await spotifySearchArtists(url);

    // if (song.artist.toLowerCase().incudes("shovel")) {
    //   console.log("Whats up!");
    // }
    // Continues for loop early if there's only one match for artist
    if (artistSearch.artists.items.length === 1) {
      popSum += artistSearch.artists.items[0].popularity;
      artistsCounted++;
      continue;
    }

    // Finds best match for artist name input then chooses largest popularity value
    //  among competing matches, assuming the most popular of them is the one being referenced.
    const popularity = Math.max(
      ...artistSearch.artists.items
        .filter(
          (artist) => artist.name.toLowerCase() === song.artist.toLowerCase()
        )
        .map((artist) => artist.popularity)
    );
    if (popularity) {
      popSum += popularity;
      artistsCounted++;
    }

    // If there is more than 1 exact match, return the most popular one
    console.log(song.artist, popularity);
  }
};

retrievePopularity(songs);

/*

Get the stats for each song, as that where the popularity 


*/
