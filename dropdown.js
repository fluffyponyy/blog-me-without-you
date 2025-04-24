function load_Dates() {
  fetch("./post_archive.json")
    .then((response) => response.json())
    .then((json) => {
      alert(JSON.stringify(json));
      archive = JSON.parse(json);

      var year,
        month,
        day = 0;

      archive = {
        2025: {
          4: {
            7: "1.html",
            8: "2.html",
            9: "3.html",
            10: "4.html",
            19: "5.html",
            20: "6.html",
            21: "7.html",
            22: "8.html",
          },
        },
      };

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
