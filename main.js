/////////////////////////////
//// KUTX 98.9, AUSTIN TEXAS
////////////////////////////

// The function below takes the div elements from the playlist
// retrieved on the kutx website from a given day and creates
// objects containing the artist, record, and song title.
// These can then be analyzed by the spotify API

const songs = [];

const playlist = document.querySelector("#playlist");
console.log([...playlist.children[0].classList].includes("track"));

for (const child of playlist.children) {
  if ([...child.classList].includes("track")) {
    console.log(child);
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

console.log(songs);
//   console.log(tracks);
//   // Retrieve only the children whose parent class is track
//   //  Extract data from there
//   // child.filter(child => child.classlist.includes('track'));
// }
// // console.log(playlist.children[0].children[0].innerText);
