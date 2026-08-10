#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// =====================================================
// Wi-Fi Configuration
// =====================================================

const char* WIFI_SSID = "siri";
const char* WIFI_PASSWORD = "2323232";

// Replace with the IP address of the computer
// running your Flask backend.
const char* SERVER_URL =
    "http://YOUR_COMPUTER_IP:5000/api/predict";


// =====================================================
// Sensor Pins
// =====================================================

const int PH_PIN = 34;
const int TDS_PIN = 35;
const int TURBIDITY_PIN = 32;
const int TEMPERATURE_PIN = 33;


// =====================================================
// Setup
// =====================================================

void setup() {

  Serial.begin(115200);

  delay(1000);

  Serial.println();
  Serial.println("================================");
  Serial.println("IoT Water Quality Monitoring");
  Serial.println("================================");

  // Connect to Wi-Fi
  WiFi.begin(
      WIFI_SSID,
      WIFI_PASSWORD
  );

  Serial.print("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");
  }

  Serial.println();

  Serial.println("Wi-Fi connected!");

  Serial.print("ESP32 IP Address: ");

  Serial.println(
      WiFi.localIP()
  );
}


// =====================================================
// Read pH
// =====================================================

float readPH() {

  int rawValue = analogRead(PH_PIN);

  float voltage =
      rawValue * (3.3 / 4095.0);

  // Basic example conversion.
  // Calibrate this according to your actual
  // pH sensor before real deployment.

  float ph =
      7.0 + ((2.5 - voltage) * 3.0);

  return ph;
}


// =====================================================
// Read TDS
// =====================================================

float readTDS() {

  int rawValue =
      analogRead(TDS_PIN);

  float voltage =
      rawValue * (3.3 / 4095.0);

  // Basic placeholder conversion.
  // Replace with your sensor's calibrated
  // TDS conversion formula.

  float tds =
      voltage * 500.0;

  return tds;
}


// =====================================================
// Read Turbidity
// =====================================================

float readTurbidity() {

  int rawValue =
      analogRead(TURBIDITY_PIN);

  float voltage =
      rawValue * (3.3 / 4095.0);

  // Basic example conversion.
  // Calibrate according to the actual
  // turbidity sensor.

  float turbidity =
      (3.3 - voltage) * 25.0;

  if (turbidity < 0) {

    turbidity = 0;
  }

  return turbidity;
}


// =====================================================
// Read Temperature
// =====================================================

float readTemperature() {

  int rawValue =
      analogRead(TEMPERATURE_PIN);

  float voltage =
      rawValue * (3.3 / 4095.0);

  // Placeholder conversion.
  // Replace with the calibration formula
  // for your actual temperature sensor.

  float temperature =
      voltage * 10.0;

  return temperature;
}


// =====================================================
// Send Data to Flask
// =====================================================

void sendWaterQualityData(
    float ph,
    float tds,
    float turbidity,
    float temperature
) {

  if (WiFi.status() != WL_CONNECTED) {

    Serial.println(
        "Wi-Fi disconnected."
    );

    return;
  }


  HTTPClient http;

  http.begin(SERVER_URL);

  http.addHeader(
      "Content-Type",
      "application/json"
  );


  // Create JSON payload
  StaticJsonDocument<256> json;

  json["ph"] = ph;

  json["tds"] = tds;

  json["turbidity"] = turbidity;

  json["temperature"] = temperature;


  String requestBody;

  serializeJson(
      json,
      requestBody
  );


  Serial.println();
  Serial.println("Sending data:");

  Serial.println(
      requestBody
  );


  int httpResponseCode =
      http.POST(requestBody);


  if (httpResponseCode > 0) {

    Serial.print(
        "HTTP Response: "
    );

    Serial.println(
        httpResponseCode
    );


    String response =
        http.getString();


    Serial.println(
        "Server response:"
    );

    Serial.println(
        response
    );

  } else {

    Serial.print(
        "HTTP request failed: "
    );

    Serial.println(
        httpResponseCode
    );
  }


  http.end();
}


// =====================================================
// Main Loop
// =====================================================

void loop() {

  float ph =
      readPH();

  float tds =
      readTDS();

  float turbidity =
      readTurbidity();

  float temperature =
      readTemperature();


  // Display sensor readings
  Serial.println();
  Serial.println(
      "========== SENSOR DATA =========="
  );

  Serial.print("pH: ");
  Serial.println(ph);

  Serial.print("TDS: ");
  Serial.print(tds);
  Serial.println(" ppm");

  Serial.print("Turbidity: ");
  Serial.print(turbidity);
  Serial.println(" NTU");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");


  // Send readings to Flask
  sendWaterQualityData(
      ph,
      tds,
      turbidity,
      temperature
  );


  // Wait 10 seconds
  delay(10000);
}
