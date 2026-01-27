
const list = document.getElementById("dictionary-list");

fetch("flashcards.csv")
  .then(res => {
    if (!res.ok) throw new Error("CSV not found");
    return res.text();
  })
  .then(data => {
    const rows = data
      .replace(/\uFEFF/g, "")
      .replace(/\r/g, "")
      .split("\n")
      .filter(row => row.trim());

    rows.forEach(row => {
      const firstComma = row.indexOf(",");
      const english = row.slice(0, firstComma).trim();
      const turkish = row.slice(firstComma + 1).trim();

      const li = document.createElement("li");
      li.innerHTML = `<strong>${english}</strong> — ${turkish}`;

      list.appendChild(li);
    });
  })
  .catch(err => {
    console.error(err);
    list.innerHTML = "<li>Failed to load dictionary</li>";
  });
