function load_Dates() {
  fetch("./post_archive.json")
    .then((response) => response.json())
    .then((json) => {
      archive = json;

      const content = document.getElementById("date_content");
      if (content.children.length > 0) return;
      content.innerHTML = ""; //  clear only the dynamic part

      for (const year in archive) {
        const year_layer = document.createElement("div");
        year_layer.classList.add("year-layer");
        year_layer.textContent = year;

        const month_container = document.createElement("div");
        month_container.classList.add("month-container");

        year_layer.addEventListener("click", () => {
          //clicking on a year opens the list of months which had any posts
          month_container.classList.toggle("open");
        });

        year_layer.appendChild(month_container);
        content.appendChild(year_layer);

        for (const month in archive[year]) {
          const month_layer = document.createElement("div");
          month_layer.classList.add("month-layer");
          month_layer.textContent = month;

          const day_container = document.createElement("div");
          day_container.classList.add("day-container");

          month_layer.addEventListener("click", (e) => {
            //clicking on a month opens the list of blog posts for those days
            e.stopPropagation();
            day_container.classList.toggle("open");
          });

          month_container.appendChild(month_layer);
          month_container.appendChild(day_container);

          for (const day in archive[year][month]) {
            const day_layer = document.createElement("div");
            day_layer.classList.add("day-layer");
            post_url = `html/individual_pages/${year}${month}${day}.html`; //individual page name
            day_layer.innerHTML = `<a href="${post_url}"> ${month}/${day}</a>`;
            day_container.appendChild(day_layer);
          }
        }
      }
    });
}
