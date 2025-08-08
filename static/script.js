function fetchJoke() {
  fetch("/joke")
    .then(res => res.json())
    .then(data => {
      const box = document.getElementById("jokeBox");
      if (data.type === "single") {
        box.innerHTML = data.joke;
      } else {
        box.innerHTML = `<p>${data.setup}</p><p class="mt-2 font-semibold">${data.delivery}</p>`;
      }
    })
    .catch(() => {
      document.getElementById("jokeBox").innerHTML = "Something went wrong!";
    });
}
