const fs = require("fs");
const { parse } = require("csv-parse");

function readData(){
var data = [];
var match = [];
var geojson = {
  "name":"NewFeatureType",
  "type":"FeatureCollection",
  "features":[]
};

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
    for (let i = 0; i < data.length; i++) {
        var parsed = JSON.parse(JSON.stringify(data[i]));
        if(parsed["word"] == "walk"){
            match.push(data[i]);
        }
    }

    //Building GeoJson object
    for(let i = 0; i < match.length; i++){
    geojson.features.push(
      {
      "type":"Feature",
      "geometry":{
          "type":"Point",
          "coordinates":match[i]["latlon"]
        },
      "properties":{
        "creole_word":match[i]["creole_word"],
        "word":match[i]["word"],
        "creole_language":match[i]["creole_name"],
        "acrolect":match[i]["acrolect"]
        }
      }
    )
  } 

  console.log(geojson)
  return(geojson)
  });
}