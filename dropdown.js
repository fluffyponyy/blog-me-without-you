function load_Dates() {
  fetch("./post_archive.json")
    .then((response) => response.json())
    .then((json) => {
      alert(JSON.stringify(json));
      archive = JSON.parse(json);

      var year,
        month,
        day = 0;

      for (year in archive) {
        var year_layer = document.createElement("div");
        year_layer.setAttribute("id", "year_layer");
        year_layer.innerHTML = year;
        document.getElementById("date_dropdown").appendChild(year_layer);
        for (month in archive[year]) {
          var month_layer = document.createElement("div");
          month_layer.setAttribute("id", "month_layer");
          month_layer.innerHTML = month;
          year_layer.appendChild(month_layer);
          for (day in archive[year][month]) {
            var day_layer = document.createElement("div");
            day_layer.setAttribute("id", "day_layer");
            day_layer.innerHTML =
              "<a href='" + archive[year][month][day] + "'> " + day + "</a>";
            month_layer.appendChild(day_layer);
          }
        }
      }
    });
}
