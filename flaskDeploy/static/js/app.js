// Get a reference to the table
var tbody = d3.select("#tweet_table").select("tbody");

// from data.js
var tableData = data;
// console.log(data);

columns = ["source","text","created_at","retweet_count","favorite_count","sentiment"]

// create a row for each object in the data
var rows = tbody.selectAll("tr")
    .data(data)
    .enter()
    .append("tr");

// create a cell in each row for each column
var cells = rows.selectAll("td")
    .data(function (row) {
        return columns.map(function (column) {
            return { column: column, value: row[column] };
        });
    })
    .enter()
    .append("td").text(function(d) {return d.value});

$('#tweet_table').DataTable();
$('.dataTables_length').addClass('bs-select');
document.getElementById('tweet_table').style = 'display: block'

