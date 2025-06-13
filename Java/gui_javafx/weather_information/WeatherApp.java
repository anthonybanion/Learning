package gui_javafx.weather_information;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import org.json.JSONObject;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class WeatherApp extends Application {

    // Your OpenWeatherMap API key
    private static final String API_KEY = "6c6522911d604355da5dd092088f1d5a";

    // List to store city search history
    private final ArrayList<String> history = new ArrayList<>();

    // UI Components
    private final Label temperatureLabel = new Label();
    private final Label humidityLabel = new Label();
    private final Label windLabel = new Label();
    private final Label conditionLabel = new Label();
    private final Label errorLabel = new Label(); // Label to show API or network errors
    private final ImageView weatherIcon = new ImageView();
    private final VBox historyBox = new VBox(5);

    private boolean useCelsius = true;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Input for city name
        TextField cityInput = new TextField();
        cityInput.setPromptText("Enter city");

        // Button to fetch weather
        Button fetchButton = new Button("Get Weather");

        // Toggle for Celsius/Fahrenheit
        ToggleButton unitToggle = new ToggleButton("Use °F");
        unitToggle.setOnAction(e -> useCelsius = !unitToggle.isSelected());

        // Action when fetch button is clicked
        fetchButton.setOnAction(e -> {
            String city = cityInput.getText().trim();
            if (!city.isEmpty()) {
                getWeather(city);
            }
        });

        // Layout for weather info
        VBox weatherInfo = new VBox(10, temperatureLabel, humidityLabel, windLabel, conditionLabel, weatherIcon, errorLabel);
        VBox inputBox = new VBox(10, cityInput, fetchButton, unitToggle);
        VBox layout = new VBox(20, inputBox, weatherInfo, new Label("Search History:"), historyBox);
        layout.setPadding(new Insets(20));

        // Window setup
        primaryStage.setTitle("Weather Information App");
        primaryStage.setScene(new Scene(layout, 400, 600));
        primaryStage.show();
    }

    // Fetch weather data for the given city
    private void getWeather(String city) {
        String unit = useCelsius ? "metric" : "imperial";
        String urlString = "https://api.openweathermap.org/data/2.5/weather?q=" + city +
                "&appid=" + API_KEY + "&units=" + unit;

        // Networking logic in try-catch
        try {
            HttpURLConnection connection = (HttpURLConnection) new URL(urlString).openConnection();
            connection.setRequestMethod("GET");

            int responseCode = connection.getResponseCode();
            InputStream stream = (responseCode == 200)
                    ? connection.getInputStream()
                    : connection.getErrorStream();

            BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
            StringBuilder json = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                json.append(line);
            }

            reader.close();

            // Handle API error
            if (responseCode != 200) {
                JSONObject errorObj = new JSONObject(json.toString());
                showError("API Error: " + errorObj.getString("message"));
                return;
            }

            // Parse and show the data
            parseWeatherData(json.toString(), city);

        } catch (IOException e) {
            showError("Error: Connection failed or invalid city.");
        }
    }

    // Parse the JSON response and update the UI
    private void parseWeatherData(String response, String city) {
        JSONObject obj = new JSONObject(response);
        JSONObject main = obj.getJSONObject("main");
        JSONObject wind = obj.getJSONObject("wind");
        JSONObject weather = obj.getJSONArray("weather").getJSONObject(0);

        double temp = main.getDouble("temp");
        int humidity = main.getInt("humidity");
        double windSpeed = wind.getDouble("speed");
        String condition = weather.getString("main");
        String icon = weather.getString("icon");

        // Update UI on JavaFX thread
        Platform.runLater(() -> {
            temperatureLabel.setText("Temperature: " + temp + (useCelsius ? " °C" : " °F"));
            humidityLabel.setText("Humidity: " + humidity + "%");
            windLabel.setText("Wind Speed: " + windSpeed + (useCelsius ? " m/s" : " mph"));
            conditionLabel.setText("Condition: " + condition);
            errorLabel.setText(""); // clear previous error
            weatherIcon.setImage(new Image("https://openweathermap.org/img/wn/" + icon + "@2x.png"));

            // Save and display history
            String timestamp = LocalDateTime.now().toString();
            history.add(city + " at " + timestamp);
            updateHistoryDisplay();
        });
    }

    // Update the history display VBox
    private void updateHistoryDisplay() {
        historyBox.getChildren().clear();
        for (String record : history) {
            historyBox.getChildren().add(new Label(record));
        }
    }

    // Show errors in the UI
    private void showError(String message) {
        Platform.runLater(() -> {
            errorLabel.setStyle("-fx-text-fill: red;");
            errorLabel.setText(message);
            temperatureLabel.setText("");
            humidityLabel.setText("");
            windLabel.setText("");
            conditionLabel.setText("");
            weatherIcon.setImage(null);
        });
    }
}
