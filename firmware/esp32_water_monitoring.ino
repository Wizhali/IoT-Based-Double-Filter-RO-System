This is a clean ESP32 firmware starter for your RO water-quality monitoring project. Keep the calibration values as placeholders until they match your actual sensors.
/*
 * ============================================================
 * IoT-Based Double-Filter RO System
 * Smart Water Quality Monitoring
 * ============================================================
 *
 * Controller : ESP32
 * Project    : Final Year Project
 * Team Size  : 3
 *
 * Purpose:
 * - Read water-quality sensor values
 * - Monitor pH, TDS, turbidity, temperature and conductivity
 * - Connect ESP32 to Wi-Fi
 * - Send sensor data to a Flask backend
 *
 * IMPORTANT:
 * Calibrate sensor formulas according to the actual
 * sensors used in the hardware prototype.
 * ============================================================
 */

#include <WiFi.h>
#include <HTTPClient.h>

// ------------------------------------------------------------
// Wi-Fi Configuration
// ------------------------------------------------------------

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// Flask server endpoint
const char* SERVER_URL =
    "http://YOUR_COMPUTER_IP:5000/api/water-data";

// ------------------------------------------------------------
// ESP32 Analog Pins
// ------------------------------------------------------------

#define PH_SENSOR_PIN          34
#define TDS_SENSOR_PIN         35
#define TURBIDITY_SENSOR_PIN   32
#define TEMPERATURE_SENSOR_PIN 33
#define CONDUCTIVITY_SENSOR_PIN 25

// ------------------------------------------------------------
// Reading interval
// ------------------------------------------------------------

const unsigned long SENSOR_INTERVAL = 5000;

unsigned long previousMillis = 0;


// ============================================================
// SETUP
// ============================================================

void setup() {

  Serial.begin(115200);

  delay(1000);

  Serial.println();
  Serial.println("======================================");
  Serial.println(" IoT RO Water Quality Monitoring");
  Serial.println(" ESP32 Firmware");
  Serial.println("======================================");

  // Configure sensor pins
  pinMode(PH_SENSOR_PIN, INPUT);
  pinMode(TDS_SENSOR_PIN, INPUT);
  pinMode(TURBIDITY_SENSOR_PIN, INPUT);
  pinMode(TEMPERATURE_SENSOR_PIN, INPUT);
  pinMode(CONDUCTIVITY_SENSOR_PIN, INPUT);

  connectToWiFi();
}


// ============================================================
// MAIN LOOP
// ============================================================

void loop() {

  // Reconnect if Wi-Fi is lost
  if (WiFi.status() != WL_CONNECTED) {

    Serial.println("Wi-Fi connection lost.");

    connectToWiFi();
  }

  // Read sensors at fixed interval
  if (millis() - previousMillis >= SENSOR_INTERVAL) {

    previousMillis = millis();

    // --------------------------------------------------------
    // Read sensor values
    // --------------------------------------------------------

    float pH = readPH();
    float tds = readTDS();
    float turbidity = readTurbidity();
    float temperature = readTemperature();
    float conductivity = readConductivity();

    // --------------------------------------------------------
    // Display readings
    // --------------------------------------------------------

    Serial.println();
    Serial.println("---------- WATER QUALITY ----------");

    Serial.print("pH             : ");
    Serial.println(pH, 2);

    Serial.print("TDS            : ");
    Serial.print(tds, 2);
    Serial.println(" ppm");

    Serial.print("Turbidity      : ");
    Serial.print(turbidity, 2);
    Serial.println(" NTU");

    Serial.print("Temperature    : ");
    Serial.print(temperature, 2);
    Serial.println(" °C");

    Serial.print("Conductivity   : ");
    Serial.print(conductivity, 2);
    Serial.println(" µS/cm");

    Serial.println("-----------------------------------");

    // --------------------------------------------------------
    // Check water quality
    // --------------------------------------------------------

    checkWaterQuality(
      pH,
      tds,
      turbidity,
      temperature,
      conductivity
    );

    // --------------------------------------------------------
    // Send data to backend
    // --------------------------------------------------------

    sendDataToServer(
      pH,
      tds,
      turbidity,
      temperature,
      conductivity
    );
  }
}


// ============================================================
// WIFI CONNECTION
// ============================================================

void connectToWiFi() {

  Serial.print("Connecting to Wi-Fi");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  int attempts = 0;

  while (WiFi.status() != WL_CONNECTED && attempts < 20) {

    delay(500);

    Serial.print(".");

    attempts++;
  }

  Serial.println();

  if (WiFi.status() == WL_CONNECTED) {

    Serial.println("Wi-Fi connected successfully.");

    Serial.print("ESP32 IP Address: ");

    Serial.println(WiFi.localIP());

  } else {

    Serial.println("Wi-Fi connection failed.");
  }
}


// ============================================================
// pH SENSOR
// ============================================================

float readPH() {

  int rawValue = analogRead(PH_SENSOR_PIN);

  float voltage =
      (rawValue / 4095.0) * 3.3;

  /*
   * IMPORTANT:
   * Replace this calculation with the calibrated
   * formula for your actual pH sensor.
   */

  float pH =
      7.0 + ((2.5 - voltage) * 3.0);

  return pH;
}


// ============================================================
// TDS SENSOR
// ============================================================

float readTDS() {

  int rawValue = analogRead(TDS_SENSOR_PIN);

  float voltage =
      (rawValue / 4095.0) * 3.3;

  /*
   * Replace this formula with the calibrated
   * TDS sensor conversion used in your project.
   */

  float tds = voltage * 500.0;

  return tds;
}


// ============================================================
// TURBIDITY SENSOR
// ============================================================

float readTurbidity() {

  int rawValue =
      analogRead(TURBIDITY_SENSOR_PIN);

  float voltage =
      (rawValue / 4095.0) * 3.3;

  /*
   * Replace this formula with the calibrated
   * turbidity sensor conversion.
   */

  float turbidity =
      (3.3 - voltage) * 100.0;

  if (turbidity < 0) {

    turbidity = 0;
  }

  return turbidity;
}


// ============================================================
// TEMPERATURE SENSOR
// ============================================================

float readTemperature() {

  int rawValue =
      analogRead(TEMPERATURE_SENSOR_PIN);

  float voltage =
      (rawValue / 4095.0) * 3.3;

  /*
   * Replace this formula according to the
   * actual temperature sensor used.
   */

  float temperature =
      voltage * 30.0;

  return temperature;
}


// ============================================================
// CONDUCTIVITY SENSOR
// ============================================================

float readConductivity() {

  int rawValue =
      analogRead(CONDUCTIVITY_SENSOR_PIN);

  float voltage =
      (rawValue / 4095.0) * 3.3;

  /*
   * Replace this formula with the calibrated
   * conductivity sensor conversion.
   */

  float conductivity =
      voltage * 1000.0;

  return conductivity;
}


// ============================================================
// WATER QUALITY CHECK
// ============================================================

void checkWaterQuality(
    float pH,
    float tds,
    float turbidity,
    float temperature,
    float conductivity) {

  bool waterQualitySafe = true;

  /*
   * Example threshold values.
   * Replace them with the limits used
   * in your actual project.
   */

  if (pH < 6.5 || pH > 8.5) {

    waterQualitySafe = false;
  }

  if (tds > 500) {

    waterQualitySafe = false;
  }

  if (turbidity > 5) {

    waterQualitySafe = false;
  }

  if (temperature < 5 || temperature > 35) {

    waterQualitySafe = false;
  }


  if (waterQualitySafe) {

    Serial.println("Water Status : SAFE");

  } else {

    Serial.println("Water Status : WARNING");
  }
}


// ============================================================
// SEND DATA TO FLASK SERVER
// ============================================================

void sendDataToServer(
    float pH,
    float tds,
    float turbidity,
    float temperature,
    float conductivity) {

  if (WiFi.status() != WL_CONNECTED) {

    Serial.println(
      "Data not sent - Wi-Fi unavailable."
    );

    return;
  }

  HTTPClient http;

  http.begin(SERVER_URL);

  http.addHeader(
    "Content-Type",
    "application/json"
  );


  // ----------------------------------------------------------
  // Create JSON data
  // ----------------------------------------------------------

  String jsonData = "{";

  jsonData += "\"ph\":";
  jsonData += String(pH, 2);

  jsonData += ",\"tds\":";
  jsonData += String(tds, 2);

  jsonData += ",\"turbidity\":";
  jsonData += String(turbidity, 2);

  jsonData += ",\"temperature\":";
  jsonData += String(temperature, 2);

  jsonData += ",\"conductivity\":";
  jsonData += String(conductivity, 2);

  jsonData += "}";


  Serial.println();
  Serial.println("Sending data to server:");

  Serial.println(jsonData);


  // ----------------------------------------------------------
  // HTTP POST
  // ----------------------------------------------------------

  int responseCode =
      http.POST(jsonData);


  if (responseCode > 0) {

    Serial.print("HTTP Response Code: ");

    Serial.println(responseCode);

    String response =
        http.getString();

    Serial.println("Server Response:");

    Serial.println(response);

  } else {

    Serial.print("HTTP Error: ");

    Serial.println(responseCode);
  }


  http.end();
}
