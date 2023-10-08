const fs = require("fs");
const { parse } = require("csv-parse");
const data = [];
const match = [];

fs.createReadStream("Creole_Languages.csv")
  .pipe(
    parse({
      delimiter: ",",
      columns: true,
      ltrim: true,
    })
  )
  .on("data", function (row) {
    // This will push the object row into the array
    data.push(row);
  })
  .on("error", function (error) {
    console.log(error.message);
  })
  .on("end", function () {
    // Here log the result array
    //console.log("parsed csv data:");
    for (let i = 0; i < data.length; i++) {
        var parsed = JSON.parse(JSON.stringify(data[i]));
        if(parsed["word"] == "walk"){
            match.push(data[i]);
        }
    } 
    console.log(match)
  });