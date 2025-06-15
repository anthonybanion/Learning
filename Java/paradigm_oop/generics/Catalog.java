/**
 * 
 * This class represents a generic catalog for managing library items.
 * 
 * File: Catalog.java
 * Author: Anthony Bañon
 * Created: 2025-05-24
 * Last Updated: 2025-05-24
 */


package paradigm_oop.generics;
import java.util.ArrayList;


// Generic Catalog class to manage library items
public class Catalog<T> {
    private ArrayList<T> items;

    public Catalog() {
        items = new ArrayList<>();
    }

    // Adds a new item to the catalog
    public void addItem(T item) {
        items.add(item);
    }

    // Removes an item by matching itemID if present
    public boolean removeItem(String itemID) {
        for (T item : items) {
            if (item instanceof LibraryItem) {
                if (((LibraryItem<?>) item).getItemID().equals(itemID)) {
                    items.remove(item);
                    return true;
                }
            }
        }
        return false;
    }

    // Displays all items in the catalog
    public void displayItems() {
        if (items.isEmpty()) {
            System.out.println("Catalog is empty.");
        } else {
            for (T item : items) {
                System.out.println(item.toString());
            }
        }
    }
}
