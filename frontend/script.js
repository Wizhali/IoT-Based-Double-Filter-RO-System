
// =========================================================
// Smart RO Water Quality Monitoring Dashboard
// =========================================================

// Flask backend API
const API_URL = "/api/water-data";


// ---------------------------------------------------------
// Get latest water-quality data
// ---------------------------------------------------------

async function fetchWaterData() {

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Unable to fetch water-quality data");
        }

        const data = await response.json();

        updateDashboard(data);

    } catch (error) {

        console.error("Error:", error);

        document.getElementById("status").textContent =
            "Backend connection unavailable";

        document.getElementById("alerts").textContent =
            "Waiting for sensor data...";
    }
}


// ---------------------------------------------------------
// Update dashboard
// ---------------------------------------------------------

function updateDashboard(data) {

    document.getElementById("ph").textContent =
        formatValue(data.ph);

    document.getElementById("tds").textContent =
        formatValue(data.tds);

    document.getElementById("turbidity").textContent =
        formatValue(data.turbidity);

    document.getElementById("temperature").textContent =
        formatValue(data.temperature);

    document.getElementById("conductivity").textContent =
        formatValue(data.conductivity);


    // Water quality status
    const statusElement =
        document.getElementById("status");

    statusElement.textContent =
        data.status || "Unknown";


    // Timestamp
    const timestampElement =
        document.getElementById("timestamp");

    if (data.timestamp) {

        const date =
            new Date(data.timestamp);

        timestampElement.textContent =
            "Last updated: " + date.toLocaleString();

    } else {

        timestampElement.textContent =
            "Last updated: --";
    }


    // Alerts
    updateAlerts(data);
}


// ---------------------------------------------------------
// Format sensor values
// ---------------------------------------------------------

function formatValue(value) {

    if (value === null || value === undefined) {
        return "--";
    }

    if (typeof value === "number") {
        return value.toFixed(2);
    }

    return value;
}


// ---------------------------------------------------------
// Display alerts
// ---------------------------------------------------------

function updateAlerts(data) {

    const alertsElement =
        document.getElementById("alerts");


    if (data.warnings && data.warnings.length > 0) {

        alertsElement.innerHTML =
            data.warnings
                .map(function (warning) {
                    return `<p>⚠️ ${warning}</p>`;
                })
                .join("");

    } else {

        alertsElement.textContent =
            "No water-quality alerts.";
    }
}


// ---------------------------------------------------------
// Automatically refresh data
// ---------------------------------------------------------

fetchWaterData();

// Refresh every 5 seconds
setInterval(fetchWaterData, 5000);
