// Get a reference to the table
var tbody = d3.select("#jobs_table").select("tbody");

// from data.js
var tableData = data;
console.log(data);

  tableData.forEach(function (tableData) {
    console.log(tableData);
    var row = tbody.append("tr");
    var cell=row.append("td")
      cell.html(`<a href='http://${tableData.href}'>${tableData.job_title}</a>`)
    Object.entries(tableData).forEach(function ([key, value]) {
      console.log(key, value);
      if (key !=="href" && key!=="job_title") {
        var cell = row.append("td");
        cell.text(value)
        
      };

    });
    
  });
  $('#jobs_table').DataTable();
$('.dataTables_length').addClass('bs-select');

