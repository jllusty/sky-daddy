

//just getting a feel for the syntax and such


service DeDeDe {
  //get info from DeDe?
  //I don't know if that's how this keyword works
  //or anything for that matter
}


struct weatherDataRequest {
  1: required string city;
  2: required string country;
  3: required double latitude;
  4: required double longitude;
  5: required i16 pressure;
  6: required i16 humidity;
  7: required i16 temp;
  8: optional i16 temp_min;
  9: optional i16 temp_max;
  10: optional i16 windSpeed;
  11: optional string windDirection;
  12: optional string weatherDescription;

  //WKT likely better as its own struct
  //map or geometry?
}