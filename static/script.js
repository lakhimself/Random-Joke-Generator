const jokeBox = document.getElementById("jokeBox");
const spinner = document.getElementById("spinner");
const savedList = document.getElementById("savedJokes");

function fetchJoke() {
  const category = document.getElementById("category").value;
  showSpinner(true);

  fetch(`/joke?category=${category}`)
    .then(res => res.json())
    .then(data => {
      showSpinner(false);
      if (data.type === "single") {
        jokeBox.innerHTML = data.joke;
        jokeBox.setAttribute("data-joke", data.joke);
      } else {
        jokeBox.innerHTML = `<p>${data.setup}</p><p class="mt-2 font-semibold">${data.delivery}</p>`;
        jokeBox.setAttribute("data-joke", `${data.setup} ${data.delivery}`);
      }
    })
    .catch(() => {
      showSpinner(false);
      jokeBox.innerHTML = "Something went wrong.";
    });
}

function showSpinner(show) {
  spinner.classList.toggle("hidden", !show);
}

function saveJoke() {
  const joke = jokeBox.getAttribute("data-joke");
  if (!joke) return;

  let saved = JSON.parse(localStorage.getItem("savedJokes") || "[]");
  if (!saved.includes(joke)) {
    saved.push(joke);
    localStorage.setItem("savedJokes", JSON.stringify(saved));
    renderSavedJokes();
  }
}

function renderSavedJokes() {
  const saved = JSON.parse(localStorage.getItem("savedJokes") || "[]");
  savedList.innerHTML = "";
  saved.forEach(joke => {
    const li = document.createElement("li");
    li.className = "mb-1 border-b pb-1";
    li.textContent = joke;
    savedList.appendChild(li);
  });
}

document.getElementById("darkToggle").onclick = () => {
  document.documentElement.classList.toggle("dark");
  const isDark = document.documentElement.classList.contains("dark");
  localStorage.setItem("darkMode", isDark ? "on" : "off");
};

// Restore dark mode preference
if (localStorage.getItem("darkMode") === "on") {
  document.documentElement.classList.add("dark");
}

renderSavedJokes();
