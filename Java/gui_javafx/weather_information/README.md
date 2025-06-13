# ☁️ Weather Information App

## 🧾 Introduction

The **Weather Information App** is a Java desktop application developed using **JavaFX** for the graphical user interface and the **OpenWeatherMap API** for real-time weather data retrieval. The application allows users to input the name of any city and fetch its current weather conditions, including temperature, humidity, wind speed, and a graphical representation of the weather. It also maintains a timestamped history of the most recent searches.

This project was developed as part of a programming assignment aimed at reinforcing practical skills in API integration, JSON parsing, JavaFX GUI development, and robust error handling.

---

## 🎯 Objective

The main goal of the project is to:

- Retrieve real-time weather data using a public API (OpenWeatherMap).
- Display the weather information in a clean and user-friendly JavaFX interface.
- Allow unit switching between Celsius and Fahrenheit.
- Maintain a recent search history for user reference.
- Handle errors effectively, such as invalid input or network failures.

---

## 🖼️ Screenshot

<div align="center">

<img src="../../../Assets/images/weather_information/weather.png" width="300"/>
</div>

---

## 🗂️ Project Folder Structure

```
Learning/
└── Java/
    ├── gui_javafx/
    │   └── weather_information/
    │       ├── WeatherApp.java     # Main JavaFX application
    └── lib/
        ├── javafx-sdk-21.0.6/      # JavaFX SDK (required modules)
        └── json-20231013.jar       # JSON library for API response parsing
```

---

## 🛠️ Compilation and Execution

### ✅ Prerequisites

Ensure that you have:

- Java 21 or later installed.
- JavaFX SDK downloaded (version used: 21.0.6).
- `json-20231013.jar` from the [JSON-java library](https://github.com/stleary/JSON-java).

### 🧪 Compile

Use the following command to compile the application:

```bash
javac --module-path /home/anthony/lib/java/javafx-sdk-21.0.6/lib \
      --add-modules javafx.controls,javafx.fxml \
      -cp .:/home/anthony/lib/java/json-20231013.jar \
      -d . \
      gui_javafx/weather_information/*.java
```

### 🚀 Execute

Run the application with the following command:

```bash
java --module-path /home/anthony/lib/java/javafx-sdk-21.0.6/lib \
     --add-modules javafx.controls,javafx.fxml \
     -cp .:/home/anthony/lib/java/json-20231013.jar \
     gui_javafx.weather_information.WeatherApp
```

> Replace `/home/anthony/...` with the appropriate paths on your system if different.

## 🔧 Technologies Used

- Java 21
- JavaFX 21.0.6
- OpenWeatherMap AP- JSON-java (org.json)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
