package introduction.programing;
/* Description: This program demonstrates the usage of interfaces in Java. 
 * File name: Vehicles.java
 * Creation date: 17/03/2025
 * Last update: 17/03/2025
 * 
*Brief: It defines a Vehicle interface with common attributes for all vehicles, 
        and three interfaces for car, motorcycle, and truck-specific attributes. 
        It also defines classes for car, motorcycle, and truck that implement the corresponding interfaces. 
        The main method creates instances of each vehicle type and displays their information using the 
        displayVehicleInfo method.*/


// Main class demonstrating the usage of vehicle classes
public class Vehicles {
    // Vehicle interface defining common attributes for all vehicles
    public interface Vehicle {
        String getBrand();
        String getModel();
        int getYear();
    }

        // Interface for car-specific attributes
    public interface CarVehicle extends Vehicle {
        int getNumberOfDoors();
        String getFuelType();
    }

    // Interface for motorcycle-specific attributes
    public interface MotorVehicle extends Vehicle {
        int getNumberOfWheels();
        String getMotorcycleType();
    }

    // Interface for truck-specific attributes
    public interface TruckVehicle extends Vehicle {
        double getLoadCapacity();
        String getTransmissionType();
    }

        // Car class implementing CarVehicle interface
    public static class Car implements CarVehicle {
        private String brand, model, fuelType;
        private int year, numberOfDoors;

        public Car(String brand, String model, int year, int numberOfDoors, String fuelType) {
            this.brand = brand;
            this.model = model;
            this.year = year;
            this.numberOfDoors = numberOfDoors;
            this.fuelType = fuelType;
        }
        
        @Override
        public String getBrand() { return brand; }
        @Override
        public String getModel() { return model; }
        @Override
        public int getYear() { return year; }
        @Override
        public int getNumberOfDoors() { return numberOfDoors; }
        @Override
        public String getFuelType() { return fuelType; }
    }

        // Motorcycle class implementing MotorVehicle interface
    public static class Motorcycle implements MotorVehicle {
        private String brand, model, motorcycleType;
        private int year, numberOfWheels;

        public Motorcycle(String brand, String model, int year, int numberOfWheels, String motorcycleType) {
            this.brand = brand;
            this.model = model;
            this.year = year;
            this.numberOfWheels = numberOfWheels;
            this.motorcycleType = motorcycleType;
        }

        @Override
        public String getBrand() { return brand; }
        @Override
        public String getModel() { return model; }
        @Override
        public int getYear() { return year; }
        @Override
        public int getNumberOfWheels() { return numberOfWheels; }
        @Override
        public String getMotorcycleType() { return motorcycleType; }
    }


        // Truck class implementing TruckVehicle interface
    public static class Truck implements TruckVehicle {
        private String brand, model, transmissionType;
        private int year;
        private double loadCapacity;
        
        public Truck(String brand, String model, int year, double loadCapacity, String transmissionType) {
            this.brand = brand;
            this.model = model;
            this.year = year;
            this.loadCapacity = loadCapacity;
            this.transmissionType = transmissionType;
        }
        
        @Override
        public String getBrand() { return brand; }
        @Override
        public String getModel() { return model; }
        @Override
        public int getYear() { return year; }
        @Override
        public double getLoadCapacity() { return loadCapacity; }
        @Override
        public String getTransmissionType() { return transmissionType; }
    }



    public static void main(String[] args) {
        Car car = new Car("Toyota", "Corolla", 2022, 4, "Gasoline");
        Motorcycle moto = new Motorcycle("Yamaha", "YZF-R1", 2021, 2, "Sport");
        Truck truck = new Truck("Volvo", "FH16", 2020, 18, "Automatic");

        displayVehicleInfo(car);
        displayVehicleInfo(moto);
        displayVehicleInfo(truck);
    }
    
    public static void displayVehicleInfo(Vehicle vehicle) {
        System.out.println("Vehicle: " + vehicle.getBrand() + " " + vehicle.getModel() + " (" + vehicle.getYear() + ")");
    }
}