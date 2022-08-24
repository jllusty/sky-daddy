
using namespace std;
using namespace js::node; // if this is necessary at all???? probably not, idfk

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
  3: required i16 pressure;
  4: required i16 humidity;
  5: required i16 temp;
  6: optional i16 temp_min;
  7: optional i16 temp_max;
  8: optional i16 windSpeed;
  9: optional string windDirection;
  10: optional string weatherDescription;
  11: required geometry WKT;
  //WKT likely better as its own struct
  //map or geometry?
}