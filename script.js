console.log("script.js is running");


let flashcards = [];
let currentIndex = 0;
let showingAnswer = false;

const cardText = document.getElementById("card-text");
const flipBtn = document.getElementById("flip");
const nextBtn = document.getElementById("next");
const prevBtn = document.getElementById("prev");
const card = document.getElementById("card");

fetch("flashcards.csv")
  .then(res => res.text())
  .then(data => {
    const rows = data.trim().split("\n");

    flashcards = rows.map(row => {
      const [english, turkish] = row.split(",");
      return {
        front: english.trim(),
        back: turkish.trim()
      };
    });

    renderCard();
  })
  .catch(err => {
    cardText.textContent = "Failed to load flashcards.";
    console.error(err);
  });

function renderCard() {
  showingAnswer = false;
  cardText.textContent = flashcards[currentIndex].front;
}

flipBtn.addEventListener("click", flipCard);
card.addEventListener("click", flipCard);

function flipCard() {
  showingAnswer = !showingAnswer;
  cardText.textContent = showingAnswer
    ? flashcards[currentIndex].back
    : flashcards[currentIndex].front;
}

nextBtn.addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % flashcards.length;
  renderCard();
});

prevBtn.addEventListener("click", () => {
  currentIndex =
    (currentIndex - 1 + flashcards.length) % flashcards.length;
  renderCard();
});

